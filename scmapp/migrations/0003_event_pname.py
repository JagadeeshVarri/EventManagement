# Generated by Django 3.2 on 2021-05-03 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scmapp', '0002_auto_20200404_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='pname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]