# Generated by Django 4.0.4 on 2022-05-07 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0010_remove_freezersdata_log_freezersdata_isactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='freezerwarehouse',
            name='emailRecpents',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
