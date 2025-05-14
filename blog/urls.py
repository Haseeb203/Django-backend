from django.urls import path
from . import views

urlpatterns = [
    path("" , views.starting_page , name="starting-page"),
    path("posts/" , views.all_posts , name="posts") , 
    path("posts/<slug:slug>" , views.single_post , name="single-post")
]
