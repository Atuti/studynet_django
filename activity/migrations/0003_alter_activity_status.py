# Generated by Django 4.1.3 on 2022-11-22 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_alter_activity_options_alter_activity_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='status',
            field=models.CharField(choices=[('started', 'Started'), ('done', 'Done'), ('undone', 'Undone')], default='started', max_length=10),
        ),
    ]