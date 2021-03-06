# Generated by Django 3.0.11 on 2020-11-24 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='ammount',
        ),
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='appointment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='appointment.Appointment'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
