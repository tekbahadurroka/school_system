# Generated by Django 4.2.4 on 2023-09-03 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0014_alter_course_create_date_alter_course_update_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_notification',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]