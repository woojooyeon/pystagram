from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import SignupForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()

def signup(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, '회원가입되었습니다.')

            next_url = request.GET.get('next','blog:index')
            return redirect(next_url)
    else:
        #form = UserCreationForm()
        form = SignupForm()
    return render(request, 'form.html', {
        'form': form,
    })

@login_required
def profile_detail(request):
    profile, is_created = UserProfile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile_detail.html',{
        'profile': profile,
    })

@login_required
def profile_edit(request):
    profile, is_created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile 정보가 업데이트되었습니다.')
            next_url = request.GET.get('next', 'accounts.views.profile_detail')
            return redirect(next_url)
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'form.html', {
        'form': form,
    })

@login_required
def user_follow(request, username):
    to_user = get_object_or_404(User, username=username)
    is_follow = request.user.is_follow(to_user)

    if request.method == 'POST':
        if not is_follow:
            messages.success(request, '{}님을 팔로우했습니다.'.format(to_user))
            request.user.follow(to_user)
        else:
            messages.success(request, '{}님을 이미 팔로우하고 있습니다.'.format(to_user))
        next_url = request.GET.get('next', '/')
        return redirect(next_url)

    return render(request, 'confirm_form.html', {
        'form_legend': '{} 팔로우'.format(to_user),
        'form_desc': '{}님을 팔로우하시겠습니까?'.format(to_user),
        'submit_label': '팔로우하기',
    })


@login_required
def user_unfollow(request, username):
    to_user = get_object_or_404(User, username=username)
    is_follow = request.user.is_follow(to_user)

    if request.method == 'POST':
        request.user.unfollow(to_user)
        messages.success(request, '{}님을 언팔했습니다.'.format(to_user))

        next_url = request.GET.get('next', '/')
        return redirect(next_url)

    return render(request, 'confirm_form.html', {
        'form_legend': '{} 언팔로우'.format(to_user),
        'form_desc': '{}님을 언팔로우하시겠습니까?'.format(to_user),
        'submit_label': '언팔로우하기',
    })