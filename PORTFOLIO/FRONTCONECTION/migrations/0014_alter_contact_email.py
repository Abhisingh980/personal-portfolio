# Generated by Django 5.1 on 2024-08-15 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FRONTCONECTION', '0013_alter_contact_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
