# Generated by Django 4.0.4 on 2022-06-15 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartracks', '0002_warehouse_serverstate_compartment'),
    ]

    operations = [
        migrations.AddField(
            model_name='compartment',
            name='smartenable',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='serverState',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]