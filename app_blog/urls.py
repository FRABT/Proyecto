from django.urls import path
from app_blog import views

app_name='app_blog'

urlpatterns = [
    path('', views.index, name='Home'),
    path('user/',views.user, name='User'),
    path('blogs/',views.blog, name='Blogs'),
    path('comments/',views.comment, name='Comments'),
    path('userform/',views.user_forms_view, name='UserForm'),
    path('usersearch/',views.user_search, name='UserSearch'),
]