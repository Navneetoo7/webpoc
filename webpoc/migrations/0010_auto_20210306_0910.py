# Generated by Django 3.1.7 on 2021-03-06 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpoc', '0009_auto_20210306_0901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='transactionID',
        ),
        migrations.AddField(
            model_name='customer',
            name='id',
            field=models.AutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
