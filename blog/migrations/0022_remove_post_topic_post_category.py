# Generated by Django 5.0.3 on 2024-03-31 06:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='topic',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category'),
        ),
    ]
