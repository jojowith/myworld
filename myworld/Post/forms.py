from django.forms import modelformset_factory, TextInput, Textarea
from django import forms
from .models import PostInfo


# class CustomTextInput(TextInput):
#    input_type = 'text'
#    input_class = 'custom-text-input'


# class CustomTextarea(Textarea):
#    input_class = 'custom-textarea'


# PostInfoFormSet = modelformset_factory(
#    PostInfo,
#    fields=("title", "brief", "body", "linkage", "Cover", "image", "video"),
#    extra=1,
#    widgets={
#        'title': CustomTextInput(attrs={'class': 'custom-title-input'}),
#        'brief': CustomTextarea(attrs={'class': 'custom-brief-textarea'}),
#        # 可以添加更多的自定義小部件
#    }
# )
class PostInfoForm(forms.ModelForm):
    class Meta:
        model = PostInfo
        fields = ['title', 'brief', 'body', 'linkage', 'Cover', 'image', 'video']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'brief': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            'title': "標題",
            'brief': "簡介",
            'body': "正文內容",
            'linkage': "URL連結",
            'Cover': "封面照片",
            'image': "圖片",
            'video': "影片",
        }
