# Generated by Django 3.2 on 2021-05-03 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scmapp', '0004_auto_20210503_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
