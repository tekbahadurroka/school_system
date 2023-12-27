# Generated by Django 4.2.4 on 2023-09-03 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0013_alter_course_create_date_alter_course_update_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='create_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='create_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='create_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='create_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
    ]