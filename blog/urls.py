"""
 Created by plank-abhijit on 14/1/17.
"""
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
