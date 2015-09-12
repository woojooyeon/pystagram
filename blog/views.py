from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Category, Post, Comment, Photograph
# from pystagram import settings
from django.conf import settings
from blog.forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages


def owner_required(model_class, field_name='pk'):
    def wrap_outer(view_fn):
        def wrap(request, *args, **kwargs):
            field_value = kwargs[field_name]
            object = get_object_or_404(model_class, **{ field_name : field_value })
            # 로그인한 사용자가 스태프가 아니거나 수정하려는 사용자와 작성한 유저가 다르면 에러
            if (not request.user.is_staff) and object.author != request.user:
                return HttpResponseForbidden('invalid user')
            return view_fn(request, *args, **kwargs)
        return wrap
    return wrap_outer

def index(request):
    count = request.session.get('index_page_count', 0) + 1
    request.session['index_page_count'] = count

    post_list = Post.objects.all()
    #post_list = Post.timeline(request.user)
    #messages.error(request, '기본으로 뜹니다요.')
    messages.debug(request, 'debug도 뜹니다요.')

    lorempixel_categories = (
        "abstract", "animals", "business", "cats", "city", "food", "night",
        "life", "fashion", "people", "nature", "sports", "technics", "transport",
    )

    return render(request, 'blog/index.html', {
        'count': count,
        'post_list': post_list,
        'lorempixel_categories': lorempixel_categories,
    })

def author_wall(request, username):
    author = get_object_or_404(User, username=username)
    is_follow = request.user.is_follow(author)
    post_list = Post.objects.filter(author=author)
    return render(request, 'blog/author_wall.html', {
        'author': author,
        'is_follow': is_follow,
        'post_list': post_list,
    })

def detail(request, pk=None, uuid=None):
  # try:
  #     post = Post.objects.get(pk=pk)
  # except Post.DoesNotExist:
  #     raise Http404
    if pk:
        post = get_object_or_404(Post, pk=pk)
    elif uuid:
        post = get_object_or_404(Post, uuid=uuid)
    else:
        raise Http404

    return render(request, 'blog/detail.html', {
        'post': post,
    })


    '''
    if int(pk) == 0:
        pass
    response = HttpResponse('page not found')
    response['X-Custom-Header'] = 'hello world'
    response.status_code = 404
    response.content_type = 'text/html'
    return response
    '''

@login_required
def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.ip = request.META['REMOTE_ADDR']
            post.save()

            #만약 폼에서 지정하지 못한 필수 필드가 있다면 아래와 같이
            #서버딴에서 필수 필드의 기본값을 설정하여 주는 방법으로 해결
            # post = form.save(commit=False)
            # post.category = get_object_or_404(Category, pk=1)
            # post.save()

            #return redirect('blog:detail', post.pk)

            #models.py에서 get_absolute_url 함수가 정의된 경우 post만 넘겨도 가능하다.
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'blog/form.html', {
        'form': form,
    })

# def new(request):
#     if request.method == "POST":   # "GET", "POST"
#         category_id = request.POST["category_id"]
#         title = request.POST["title"]
#         content = request.POST["content"]

#         category = get_object_or_404(Category, pk=category_id)

#         post = Post(category=category, title=title, content=content)
#         post.save()

#         return redirect('blog:detail', post.pk)
#     else:
#         pass


#     return render(request, 'blog/form.html', {
#     })

@login_required
@owner_required(Post, 'pk')
def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # 수정하려는 사용자와 작성한 유저가 다르면 에러
    if post.author != request.user:
        pass

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()

            # post = form.save(commit=False)
            # post.author = request.user
            # post.save()


            #만약 폼에서 지정하지 못한 필수 필드가 있다면 아래와 같이
            #서버딴에서 필수 필드의 기본값을 설정하여 주는 방법으로 해결
            # post = form.save(commit=False)
            # post.category = get_object_or_404(Category, pk=1)
            # post.save()

            #return redirect('blog:detail', post.pk)

            #models.py에서 get_absolute_url 함수가 정의된 경우 post만 넘겨도 가능하다.
            return redirect(post)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/form.html', {
        'form': form,
    })

@login_required
@owner_required(Post)
def new_old(request):
    if request.method == "POST":  # "GET", "POST"
        category_id = request.POST["category_id"]
        title = request.POST["title"]
        content = request.POST["content"]

        category = get_object_or_404(Category, pk=category_id)

        post = Post(category=category, title=title, content=content)
        post.save()

        #return redirect('blog:detail', post.pk)
        #models.py에서 get_absolute_url 함수가 정의된 경우 post만 넘겨도 가능하다.
        return redirect(post)

    return render(request, 'blog/form.html', {
    })

@login_required
def comment_new(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = get_object_or_404(Post, pk=pk)
            comment.save()
            messages.success(request, '새 댓글이 저장되었습니다.')
            #return redirect('blog:detail', pk)

            #models.py에서 get_absolute_url 함수가 정의된 경우 post만 넘겨도 가능하다.
            return redirect(comment.post)
    else:
        form = CommentForm()
    return render(request, 'form.html', {
        'form': form,
    })

@login_required
@owner_required(Comment, 'pk')
def comment_edit(request, post_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, '댓글이 수정되었습니다.')
            #return redirect('blog:detail', post_pk)

            #models.py에서 get_absolute_url 함수가 정의된 경우 post만 넘겨도 가능하다.
            return redirect(comment.post)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'form.html', {
        'form': form,
    })

@login_required
@owner_required(Comment, 'pk')
def comment_delete(request, post_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        comment.delete()
        messages.success(request, '댓글을 삭제 했습니다.')
        #return redirect('blog:detail', post_pk)

        #models.py에서 get_absolute_url 함수가 정의된 경우 post만 넘겨도 가능하다.
        return redirect(post)

    return render(request, 'blog/comment_delete_confirm.html', {
        'comment' : comment,
    })

def photos(request):
    photos = Photograph.objects.all()
    return render(request, 'blog/photos.html', {
        'photos': photos,
    })
