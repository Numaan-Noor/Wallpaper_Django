from django.urls import path
from .views import index, contact, single, gallery
from django.conf.urls import url

urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact'),
    # path('single', single, name='single'),
    url(r'^single/(?P<pk>[0-9]+)/$', single, name='single'),
    url(r'^gallery/(?P<pk>[0-9]+)/$', gallery, name='gallery'),
    # path('gallery', gallery, name='gallery')
]