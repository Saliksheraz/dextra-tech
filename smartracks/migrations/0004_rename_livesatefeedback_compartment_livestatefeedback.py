# Generated by Django 4.0.4 on 2022-06-15 21:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smartracks', '0003_compartment_smartenable_alter_warehouse_serverstate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='compartment',
            old_name='livesatefeedback',
            new_name='livestatefeedback',
        ),
    ]
