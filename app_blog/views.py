from django.shortcuts import render
from app_blog.models import User, Blog, Comment
from app_blog.forms import UserForm, BlogForm, CommentForm


def index(request):
    return render(request, "app_blog/home.html")


def user(request):
    users = User.objects.all()

    context_dict = {
        'users' : users
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_blog/user.html"
    )


def blog(request):
    blogs = Blog.objects.all()

    context_dict = {
        'blogs' : blogs
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_blog/blog.html"
    )


def comment(request):
    comments = Comment.objects.all()

    context_dict = {
        'comments' : comments
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_blog/comment.html"
    )


def user_forms_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            data = user_form.cleaned_data
            user = User(
                nick=data['nick'],
                email=data['email'],
                password=data['password'],
            )
            user.save()

            users = User.objects.all()
            context_dict = {
                'users': users
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_blog/user.html"
            )

    user_form = UserForm(request.POST)
    context_dict = {
        'user_form': user_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_blog/user_forms.html'
    )


def user_search(request):
    context_dict = dict()
    if request.GET['text_search']:
        search_param = request.GET['text_search']
        users = User.objects.filter(nick__contains=search_param)
        context_dict = {
            'users': users
        }
    elif request.GET['email_search']:
        search_param = request.GET['email_search']
        users = User.objects.filter(email__contains=search_param)
        context_dict = {
            'users': users
        }
    
    return render(
        request=request,
        context=context_dict,
        template_name="app_blog/user_search.html",
    )