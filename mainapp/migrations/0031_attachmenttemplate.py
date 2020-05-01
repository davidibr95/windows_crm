# Generated by Django 3.0.3 on 2020-05-01 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0030_tasks_private'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttachmentTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('offer', 'offer'), ('offer confirmation', 'offer confirmation'), ('install', 'install'), ('invoice', 'invoice')], max_length=32, unique=True, verbose_name='type')),
                ('subject', models.CharField(max_length=256, verbose_name='subject')),
                ('body', models.TextField()),
            ],
        ),
    ]