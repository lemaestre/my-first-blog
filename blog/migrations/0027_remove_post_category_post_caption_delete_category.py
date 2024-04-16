# Generated by Django 5.0.3 on 2024-04-04 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_alter_post_head_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.AddField(
            model_name='post',
            name='caption',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Caption'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
