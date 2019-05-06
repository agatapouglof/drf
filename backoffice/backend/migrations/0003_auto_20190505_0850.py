# Generated by Django 2.2 on 2019-05-05 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20190423_1112'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='gcauser',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='gcauser',
            name='date_joined',
        ),
        migrations.AlterField(
            model_name='gcauser',
            name='email',
            field=models.EmailField(help_text='email address', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='gcauser',
            name='first_name',
            field=models.CharField(blank=True, help_text='first name', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='gcauser',
            name='is_active',
            field=models.BooleanField(default=True, help_text='active status'),
        ),
        migrations.AlterField(
            model_name='gcauser',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='staff status'),
        ),
        migrations.AlterField(
            model_name='gcauser',
            name='last_name',
            field=models.CharField(blank=True, help_text='last name', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='gcauser',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
