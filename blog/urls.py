from django.conf.urls import url, patterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #url(r'^$', 'blog.views.index', name='index'),
    #url(r'^(?P<uuid>[0-9a-z]{32})/$', 'blog.views.detail', name='detail'),
    #url(r'^(?P<pk>\d+)/$', 'blog.views.detail', name='detail'),
    #url(r'^new/$', 'blog.views.new', name='new'),
    #url(r'^edit/(?P<pk>\d+)/$', 'blog.views.edit', name='edit'),

    #url(r'^(?P<pk>\d+)/comments/new/$', 'blog.views.comment_new', name='comment_new'),
    # url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', 'blog.views.comment_edit', name='comment_edit'),
    # url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/delete/$', 'blog.views.comment_delete', name='comment_delete'),

    url(r'^photos/$', 'blog.views.photos', name='photos'),
]

urlpatterns += [
    url(r'^$', 'blog.views_cbv.index', name='index'),
    url(r'^(?P<uuid>[0-9a-z]{32})/$', 'blog.views_cbv.detail', name='detail'),
    url(r'^(?P<pk>\d+)/$', 'blog.views_cbv.detail', name='detail'),
    url(r'^new/$', 'blog.views_cbv.new', name='new'),
    url(r'^edit/(?P<pk>\d+)/$', 'blog.views_cbv.edit', name='edit'),
    url(r'^(?P<pk>\d+)/comments/new/$', 'blog.views_cbv.comment_new', name='comment_new'),
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', 'blog.views_cbv.comment_edit', name='comment_edit'),
    url(r'^(?P<post_pk>\d+)/comments/(?P<pk>\d+)/delete/$', 'blog.views_cbv.comment_delete', name='comment_delete'),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)