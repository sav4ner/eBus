# Generated by Django 3.0.3 on 2022-03-09 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busApp', '0003_auto_20220308_1952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookings',
            old_name='firstname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='bookings',
            old_name='lastname',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='bookings',
            name='email',
        ),
    ]
