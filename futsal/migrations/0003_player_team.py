# Generated by Django 2.1.1 on 2019-03-02 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futsal', '0002_auto_20190302_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.CharField(default='abc', max_length=20),
        ),
    ]