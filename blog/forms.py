from django import forms
from blog.models import Article, Image

# class ArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         fields = '__all__'

# class ImageForm(forms.FileInput):
#     image = forms.ImageField(required=True)
    
#     class Meta:
#         model = Image

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class UploadFileForm(forms.Form):
    title = forms.CharField(label='Title', max_length=200)
    images = MultipleFileField(label='Images', required=False)
