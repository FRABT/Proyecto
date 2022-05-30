from django import forms


class UserForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(max_length=30, min_length=8, label='Password')
    nick = forms.CharField(max_length=20, label='Nick')


class BlogForm(forms.Form):
    date = forms.DateField(label='Date')
    title = forms.CharField(max_length=50, min_length=10, label='Title')
    body = forms.CharField(max_length=500, label='Body')


class CommentForm(forms.Form):
    date = forms.DateField(label='Date')
    title = forms.CharField(max_length=50, min_length=10, label='Title')
    body = forms.CharField(max_length=500, label='Body')