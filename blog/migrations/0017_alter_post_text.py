# Generated by Django 5.0.3 on 2024-03-29 09:00

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Body'),
        ),
    ]
