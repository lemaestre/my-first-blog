# Generated by Django 5.0.3 on 2024-04-16 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_alter_post_snippet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='tslug',
            new_name='slug',
        ),
    ]