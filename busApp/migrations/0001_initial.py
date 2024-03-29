# Generated by Django 3.0.3 on 2022-02-28 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookings',
            fields=[
                ('bookingId', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=150)),
                ('lastname', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('fro', models.CharField(max_length=150)),
                ('destination', models.CharField(max_length=100)),
                ('bill', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='bustype',
            fields=[
                ('bustype', models.CharField(max_length=150, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('categories', models.CharField(max_length=150, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('state', models.CharField(max_length=150, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='route',
            fields=[
                ('routeId', models.AutoField(primary_key=True, serialize=False)),
                ('route', models.CharField(max_length=150)),
                ('fee', models.PositiveIntegerField()),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status1', to='busApp.status')),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=150)),
                ('lastname', models.CharField(max_length=150)),
                ('languages', models.CharField(max_length=250)),
                ('photo', models.ImageField(null=True, upload_to='static')),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=100)),
                ('jobtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speciality', to='busApp.category')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status', to='busApp.status')),
            ],
        ),
        migrations.CreateModel(
            name='bus',
            fields=[
                ('busId', models.AutoField(primary_key=True, serialize=False)),
                ('platenumber', models.CharField(max_length=150)),
                ('seats', models.CharField(max_length=50)),
                ('bustype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type', to='busApp.bustype')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driverr', to='busApp.employee')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route1', to='busApp.route')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status2', to='busApp.status')),
            ],
        ),
    ]
