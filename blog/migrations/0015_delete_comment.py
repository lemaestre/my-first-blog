# Generated by Django 5.0.3 on 2024-03-22 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_comment_text'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
