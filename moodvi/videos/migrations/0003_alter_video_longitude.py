# Generated by Django 4.1.5 on 2023-01-23 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_save_comment_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
        ),
    ]
