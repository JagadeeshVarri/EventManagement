# Generated by Django 3.2 on 2021-05-03 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scmapp', '0003_event_pname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=25)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='scmapp.category'),
        ),
    ]
