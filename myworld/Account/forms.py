from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from UserProfile.models import Profile

class ProfilePicForm(forms.ModelForm):
    profile_image= forms.ImageField(label="變更大頭貼")

    class Meta:
        model= Profile
        fields=('profile_image', )




class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget.attrs.update({
            'class': 'form-control',
            'required': '',
            'name': 'first_name',
            'id': 'first_name',
            'type': 'text',
            'placeholder': '用戶名稱',
            'maxlength': "16",
            'minlength': "6",
        })

        self.fields["username"].widget.attrs.update({
            'class': 'form-control',
            'required': '',
            'name': 'username',
            'id': 'username',
            'type': 'text',
            'placeholder': '帳戶登入名稱',
            'aria-label': '帳戶登入名稱',
            'maxlength': "16",
            'minlength': "6",
        })

        self.fields["password1"].widget.attrs.update({
            'class': 'form-control',
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'placeholder': '密碼',
            'maxlength': '22',
            'minlength': '8'
        })

        self.fields["password2"].widget.attrs.update({
            'class': 'form-control',
            'required': '',
            'name': 'password2',
            'id': 'password2',
            'type': 'password',
            'placeholder': '確認密碼',
            'maxlength': '22',
            'minlength': '8'
        })

    first_name = forms.CharField(max_length=20, label=False)
    username = forms.CharField(max_length=20, label=False)

    class Meta:
        model = User
        fields = ('first_name', 'username', 'password1', 'password2')
