# Generated by Django 4.1 on 2022-08-06 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=150)),
                ('blog_text', models.CharField(max_length=300)),
                ('blog_image', models.ImageField(upload_to='event_images/')),
                ('blog_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]