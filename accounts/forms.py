from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import UserProfile

class SignupForm(UserCreationForm):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        if email:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('이미 등록된 이메일입니다.')
        return email

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    # class Meta:
    #     model = User
    #     fields = ('username', 'email')



class QuizLoginForm(AuthenticationForm):
    answer = forms.CharField(help_text='3+3=?')

    #clean_변수명
    def clean_answer(self):
        #get(첫번째 인자는 파라미터이름, 두번째 인자는 값이 넘어오지 않을경우 default로 설정할 값)
        answer = self.cleaned_data.get('answer', '').strip()#좌우 공백 제거
        if answer:
            if answer != '6':
                raise forms.ValidationError('땡~~!!!')
            pass
        return answer

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('biography',)

