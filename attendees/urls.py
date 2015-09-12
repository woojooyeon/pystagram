from django.conf.urls import url, patterns

urlpatterns = [
    url(r'^$', 'attendees.views.index'),
]