# Generated by Django 3.2.4 on 2021-06-19 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route_planner', '0002_pollutionarea_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollutionarea',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]