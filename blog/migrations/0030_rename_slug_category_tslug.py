# Generated by Django 5.0.3 on 2024-04-04 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='slug',
            new_name='tslug',
        ),
    ]
