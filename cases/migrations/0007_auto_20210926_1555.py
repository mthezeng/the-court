# Generated by Django 3.2.7 on 2021-09-26 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0006_auto_20210926_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='opinion',
            name='text',
        ),
        migrations.AddField(
            model_name='case',
            name='syllabus_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='opinion',
            name='text_link',
            field=models.URLField(blank=True),
        ),
    ]
