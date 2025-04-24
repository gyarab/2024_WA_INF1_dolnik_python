from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field, Submit

class CommentForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    text = forms.CharField(label='Your Comment', widget=forms.Textarea)

class LoginForm(forms.Form):
    username = forms.CharField(label='Uživatelské jméno', max_length=100)
    password = forms.CharField(label='Heslo', widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Field('username'),
                Field('password'),
            ),
            Submit('submit', 'Přihlásit se', css_class='btn-primary')
        )   