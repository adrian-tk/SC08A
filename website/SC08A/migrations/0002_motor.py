# Generated by Django 4.0.6 on 2022-07-26 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SC08A', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_no', models.SmallIntegerField()),
                ('value', models.FloatField()),
            ],
        ),
    ]
