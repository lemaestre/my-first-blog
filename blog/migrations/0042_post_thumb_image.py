# Generated by Django 5.0.3 on 2024-05-25 01:35

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0041_alter_post_options_alter_post_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumb_image',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Thumbnail'),
        ),
    ]