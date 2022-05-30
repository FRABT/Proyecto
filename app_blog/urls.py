from unicodedata import name
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
    path('searchform/',views.search_form, name='SearchForm'),
    path('blogsform/',views.blog_forms_view, name='BlogForm'),
    path('commentsform/',views.comment_forms_view, name='CommentForm'),
]