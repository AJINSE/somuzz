# Generated by Django 2.2.3 on 2020-02-06 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='message',
            field=models.CharField(default='bhhjkk', max_length=300),
            preserve_default=False,
        ),
    ]
