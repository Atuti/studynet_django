# Generated by Django 4.1.3 on 2022-11-10 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]
