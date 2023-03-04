from django import forms
from django.forms import Form
from django.contrib.auth.models import User


class LoginForm(Form):
    username = forms.CharField(max_length=100, label='Имя')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

    def clean(self):
        username = self.data['username']
        user = User.objects.filter(username=username).first()
        if not user:
            raise  forms.ValidationError('Пользователь не найден')
        validate_user = user.check_password(self.cleaned_data['password'])
        if not validate_user:
            raise  forms.ValidationError('Пароль неверный')

        return self.cleaned_data


class UserRegistrationForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Логін"
        self.fields['first_name'].label = "Ім'я"
        self.fields['last_name'].label = "Фамілія"
        self.fields['email'].label = "Електронна пошта"
        self.fields['password'].label = "Введіть пароль"
        self.fields['password2'].label = "Підтвердження паролю"

    
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username', 'first_name','last_name', 'email')
        help_texts = {
            'username': None,
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']

