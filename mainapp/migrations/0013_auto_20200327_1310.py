# Generated by Django 3.0.3 on 2020-03-27 13:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_auto_20200327_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaserecord',
            name='kwh2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Kw/H'),
        ),
        migrations.AddField(
            model_name='purchaserecord',
            name='manufacturer2',
            field=models.CharField(max_length=255, null=True, verbose_name='Manufacturer'),
        ),
        migrations.AlterField(
            model_name='purchaserecord',
            name='alignment',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='purchaserecord',
            name='date_sent',
            field=models.DateField(blank=True, null=True, verbose_name='AG geschickt/AG Sent'),
        ),
        migrations.AlterField(
            model_name='purchaserecord',
            name='declined',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='purchaserecord',
            name='module_area',
            field=models.FloatField(blank=True, default=0, help_text='Area in meter squared (m2)', null=True, validators=[django.core.validators.MinValueValidator(0, 'Should be above 0')]),
        ),
        migrations.AlterField(
            model_name='purchaserecord',
            name='module_count',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='purchaserecord',
            name='offer_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='purchaserecord',
            name='price_without_tax',
            field=models.FloatField(default=0, help_text='Price in Euro (€)', null=True, validators=[django.core.validators.MinValueValidator(0, 'Should be above 0')]),
        ),
        migrations.AlterField(
            model_name='purchaserecord',
            name='reseller_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='purchaserecord',
            name='roof_tilt',
            field=models.FloatField(blank=True, help_text='in Degrees', null=True),
        ),
        migrations.AlterField(
            model_name='purchaserecord',
            name='roof_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]