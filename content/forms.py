from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    text = forms.CharField(label='Your Comment', widget=forms.Textarea)