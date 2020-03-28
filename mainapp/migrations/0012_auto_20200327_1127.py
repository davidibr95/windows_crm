# Generated by Django 3.0.3 on 2020-03-27 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20200327_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaserecord',
            name='cancellation',
        ),
        migrations.RemoveField(
            model_name='purchaserecord',
            name='installation_date',
        ),
        migrations.RemoveField(
            model_name='purchaserecord',
            name='memory_type',
        ),
        migrations.RemoveField(
            model_name='purchaserecord',
            name='module_type',
        ),
        migrations.AddField(
            model_name='purchaserecord',
            name='extra_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='purchaserecord',
            name='kwh',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]