# Generated by Django 4.0.5 on 2022-11-01 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dserver', '0002_alter_humidity_time_alter_remnant_w_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='humidity',
            name='TIME',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='remnant_w',
            name='TIME',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='TIME',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]