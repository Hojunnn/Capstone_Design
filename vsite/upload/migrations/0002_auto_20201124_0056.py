# Generated by Django 3.1.3 on 2020-11-23 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='category',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='name',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
