# Generated by Django 4.1.3 on 2022-11-10 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_lesson_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='image',
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]
