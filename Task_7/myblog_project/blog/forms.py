from django import forms
from .models import Comment

# [cite_start]Форма для відправки email [cite: 224-228]
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

# [cite_start]Форма для коментарів [cite: 332-335]
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']