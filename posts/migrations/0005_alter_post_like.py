# Generated by Django 3.2.6 on 2021-08-13 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like',
            field=models.IntegerField(blank=True, default=0, verbose_name='like_count'),
        ),
    ]
