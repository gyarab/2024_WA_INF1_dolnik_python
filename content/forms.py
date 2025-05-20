from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field, Submit

class CommentForm(forms.Form):
# The username will be taken from the logged-in user, so no field is needed here.
    text = forms.CharField(label='Your Comment', widget=forms.Textarea)

class LoginForm(forms.Form):
    username = forms.CharField(label='Uživatelské jméno', max_length=100)
    password = forms.CharField(label='Heslo', widget=forms.PasswordInput)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        # Set up the form layout using crispy-forms for the login popup
        self.helper.layout = Layout(
            Row(
            Field('username', placeholder='Enter your username', wrapper_class='form-group', label='Username'),
            Field('password', placeholder='Enter your password', wrapper_class='form-group', label='Password'),
            ),
            Submit('submit', 'Log in', css_class='btn-primary')
        )
class RegistrationForm(forms.Form):
    username = forms.CharField(label='Uživatelské jméno', max_length=100)
    password = forms.CharField(label='Heslo', widget=forms.PasswordInput)
    email = forms.EmailField(label='E-mail')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        # Set up the form layout using crispy-forms for the registration popup
        self.helper.layout = Layout(
            Row(
            Field('username', placeholder='Enter your username', wrapper_class='form-group', label='Username'),
            Field('password', placeholder='Enter your password', wrapper_class='form-group', label='Password'),
            Field('email', placeholder='Enter your email', wrapper_class='form-group', label='Email'),
            ),
            Submit('submit', 'Register', css_class='btn-primary')
        )
