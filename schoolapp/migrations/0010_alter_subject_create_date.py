# Generated by Django 4.2.4 on 2023-08-31 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0009_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='create_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
