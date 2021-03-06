# Generated by Django 3.2.6 on 2021-09-11 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]
