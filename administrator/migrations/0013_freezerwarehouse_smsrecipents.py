# Generated by Django 4.0.4 on 2022-05-07 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0012_rename_emailrecpents_freezerwarehouse_emailrecipents'),
    ]

    operations = [
        migrations.AddField(
            model_name='freezerwarehouse',
            name='smsRecipents',
            field=models.CharField(max_length=200, null=True),
        ),
    ]