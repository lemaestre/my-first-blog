# Generated by Django 5.0.3 on 2024-03-21 15:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_comment_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-timestamp']},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 3, 21, 15, 0, 22, 274413, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
