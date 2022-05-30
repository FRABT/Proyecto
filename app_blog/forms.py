from django import forms


class UserForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(max_length=30, min_length=8, label='Password')
    nick = forms.CharField(max_length=20, label='Nick')


class BlogForm(forms.Form):
    date = forms.DateField(label='Blog_Date')
    title = forms.CharField(max_length=50, min_length=10, label='Blog_Title')
    body = forms.CharField(max_length=500, label='Blog_Body')


class CommentForm(forms.Form):
    date = forms.DateField(label='Comment_Date')
    title = forms.CharField(max_length=50, min_length=10, label='Comment_Title')
    body = forms.CharField(max_length=500, label='Comment_Body')