from django.contrib import admin
from django.urls import path
from . import views
from .views import List,Detail,Create,Update,Delete,UserList
urlpatterns = [
    path("",List.as_view(),name="home"),
    path("user/<str:username>",UserList.as_view(),name="UserList"),
    path("post/<int:pk>/",Detail.as_view(),name="post_detail"),
    path("post/new",Create.as_view(),name="createView"),
    path("post/<int:pk>/update",Update.as_view(),name="update_view"),
    path("post/<int:pk>/delete",Delete.as_view(),name="DeleteView"),
    path("about/",views.about,name='about'),
]
