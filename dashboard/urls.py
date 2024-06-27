from django.urls import path

from . import views


urlpatterns = [
    path('test', views.dashboard, name='dashboard'), # testing url
    path('postproduct', views.postproduct, name='postproduct'), # post product url
    path('postcategory', views.postcategory, name='postcategory'), # post category url
]