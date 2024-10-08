# Generated by Django 5.1 on 2024-08-18 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FRONTCONECTION', '0025_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='description',
            field=models.TextField(blank=True, default='No description available', null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='html_url',
            field=models.URLField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/posts/'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
