from django import forms
from django.contrib.auth import authenticate, get_user_model


User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("The user doesn't exist")

            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")

            if not user.is_active:
                raise forms.ValidationError("The user is not active") 

        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterform(forms.ModelForm):
    email = forms.EmailField(label="Email Address")
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]

    def clean_reg(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email_id = User.objects.filter(email=email)

        if email_id.exists():
            raise forms.ValidationError("This emailid already exists")

        return email
