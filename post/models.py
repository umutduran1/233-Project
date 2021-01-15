from django.db import models
from ckeditor.fields import RichTextField
import uuid
from django.utils.text import slugify

class Post(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,verbose_name='ID')
    user   = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    title = models.CharField(max_length=120,verbose_name="Başlık")
    content = RichTextField(verbose_name='İçerik')
    img = models.ImageField(verbose_name='Resim',null=True,blank=True)
    date = models.DateTimeField(verbose_name='Tarih',auto_now_add=True)
    comment = models.IntegerField(verbose_name='Yorum Sayısı',default=0)
    like = models.IntegerField(verbose_name='Beğeni Sayısı',default=0)



    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Posts'



class Likes(models.Model):
    
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return str(self.date)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Beğeniler'

class Comments(models.Model):

    user = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    comment = RichTextField(verbose_name='Yorum')
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
    
        return str(self.date)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Yorumlar'