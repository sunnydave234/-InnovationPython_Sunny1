from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('createBlog/', views.createBlog, name='createBlog'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.loginPage, name='logout'),
    path('updateBlog/<str:pk>', views.updateBlog, name='updateBlog'),
    path('deleteBlog/<str:pk>', views.deleteBlog, name='deleteBlog'),
]