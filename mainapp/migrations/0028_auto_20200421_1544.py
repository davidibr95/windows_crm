# Generated by Django 3.0.3 on 2020-04-21 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0027_customer_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callnotes',
            name='created',
            field=models.DateTimeField(null=True),
        ),
    ]
