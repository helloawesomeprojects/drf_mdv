# Generated by Django 4.1.5 on 2023-01-23 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('file', models.FileField(null=True, upload_to='videos/')),
                ('latitude', models.DecimalField(decimal_places=6, default=0, max_digits=9)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=9)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('distance', models.DecimalField(decimal_places=6, default=0, max_digits=12, null=True)),
                ('is_liked', models.DecimalField(decimal_places=0, default=0, max_digits=1, null=True)),
                ('is_saved', models.DecimalField(decimal_places=0, default=0, max_digits=1, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
