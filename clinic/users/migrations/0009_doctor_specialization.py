# Generated by Django 3.0.11 on 2020-11-24 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20201124_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='specialization',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Specialization'),
        ),
    ]
