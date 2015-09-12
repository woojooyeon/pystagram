"""my_pystagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from photos import urls as photos_urls
from blog import urls as blog_urls
from attendees import urls as attendees_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^photos/', include(photos_urls)),
    url(r'^blog/', include(blog_urls, namespace='blog')),
    url(r'^attendees/', include(attendees_urls)),
    #아래와 같이 더 디테일한 경로가 리스트상에서 먼저 있으면 그 경로의 템플릿으로
    #이동 만약없다면 아래 accouts 에서 include된 urls에서 템플릿 탐색
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    #accounts 앱의 template 에 view경로를 탐색
    url(r'^accounts/', include('accounts.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),



    # url(r'^photos/$', 'photos.views.index'),
    # url(r'^photos/(?P<pk>\d+)/$', 'photos.views.detail'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
