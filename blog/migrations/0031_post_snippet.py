# Generated by Django 5.0.3 on 2024-04-15 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_rename_slug_category_tslug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Snippet'),
        ),
    ]
