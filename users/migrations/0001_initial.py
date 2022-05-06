# Generated by Django 3.1.7 on 2022-05-06 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50, null=True)),
                ('mobile', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=300, null=True)),
                ('gender', models.CharField(max_length=100)),
                ('picture', models.ImageField(null=True, upload_to='')),
                ('firstName', models.CharField(max_length=30, null=True)),
                ('secondName', models.CharField(max_length=30, null=True)),
                ('website', models.CharField(max_length=30, null=True)),
                ('facebook', models.CharField(max_length=30, null=True)),
                ('insta', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]