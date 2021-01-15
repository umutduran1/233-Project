from django import forms
from .models import Post,Comments
from ckeditor.fields import RichTextField

class CreatePost(forms.ModelForm):

    title = forms.CharField(max_length=120,label='Başlık')
    content = RichTextField()
    img = forms.ImageField(label='Resim')
    class Meta:
        model = Post

        fields = ['title','content','img']

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comments

        fields = ['comment']
