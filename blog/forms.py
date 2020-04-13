from django import forms

from .models import Blogpost


class BlogpostForm(forms.ModelForm):
    blog_user = forms.CharField(label='Name',
                                widget=forms.TextInput(attrs={"placeholder": "Your name"}))
    blog_title = forms.CharField(label='Title',
                                 widget=forms.TextInput(attrs={"placeholder": "Title of this blog"}))
    blog_text = forms.CharField(label='',
                                widget=forms.Textarea(
                                      attrs={
                                          "placeholder": "Enter blog text here",
                                          "rows": 20,
                                          "cols": 120
                                      }))
    blog_date = forms.DateField(label='Date',
                                widget=forms.TextInput(
                                      attrs={"placeholder": "YYYY-MM-DD"}))

    class Meta:
        model = Blogpost
        fields = [
            'blog_user',
            'blog_title',
            'blog_text',
            'blog_date'
        ]
