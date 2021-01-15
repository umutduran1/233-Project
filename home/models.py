from django.db import models

# Create your models here.


class Contact(models.Model):

    full_name = models.CharField(verbose_name='Ad Soyad',max_length=120)
    email = models.EmailField(verbose_name='Email Adresi')
    msg = models.TextField(verbose_name='Mesaj')
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):

        return self.full_name

    class Meta:

        ordering = ['-date']
        verbose_name_plural = 'İletişim'