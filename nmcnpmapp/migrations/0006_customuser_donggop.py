# Generated by Django 4.2.7 on 2023-11-06 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nmcnpmapp', '0005_customuser_dongphi_customuser_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='donggop',
            field=models.BooleanField(default=False),
        ),
    ]
