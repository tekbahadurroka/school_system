# Generated by Django 4.2.4 on 2023-09-05 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0019_alter_staff_leave_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff_leave',
            name='day',
        ),
    ]
