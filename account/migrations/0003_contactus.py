# Generated by Django 4.1.1 on 2022-10-02 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_registeredparthers'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=300)),
                ('phone_number', models.CharField(max_length=100)),
                ('org_name', models.CharField(max_length=200)),
                ('org_size', models.IntegerField()),
                ('job', models.TextField()),
                ('hear', models.TextField()),
                ('message', models.TextField()),
                ('country', models.CharField(max_length=100)),
            ],
        ),
    ]
