# Generated by Django 3.0.11 on 2020-11-24 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_doctor_specialization'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specialization',
            old_name='specialization',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='user_type',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_type',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='gender',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'male'), (2, 'female'), (3, 'unspecified')], null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='doctor'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'male'), (2, 'female'), (3, 'unspecified')], null=True),
        ),
    ]
