# Generated by Django 2.2 on 2021-01-11 02:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20210111_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment',
            field=ckeditor.fields.RichTextField(default='asdsad', verbose_name='Yorum'),
            preserve_default=False,
        ),
    ]