from django.conf.urls import include, url
# from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import QuizLoginForm
urlpatterns = [
    url(r'^login/$', 'django.contrib.auth.views.login',{
        #아래와 같이 설정할 경우 템플릿폴더 registration내에 login.html을 만들 필요가 없다.
        'template_name': 'form.html',
        'authentication_form': QuizLoginForm,
    }),
    # url(r'^login/$', 'django.contrib.auth.views.login',{
    #     'authentication_form': AuthenticationForm,
    # }),
    url(r'^profile/$', 'accounts.views.profile_detail'),
    url(r'^signup/$', 'accounts.views.signup'),
    url(r'^profile/edit/$', 'accounts.views.profile_edit'),

    url(r'^(?P<username>\w+)/follow/$', 'accounts.views.user_follow', name='user_follow'),
    url(r'^(?P<username>\w+)/unfollow/$', 'accounts.views.user_unfollow', name='user_unfollow'),
]
