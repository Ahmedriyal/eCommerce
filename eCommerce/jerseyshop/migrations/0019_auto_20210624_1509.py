# Generated by Django 3.2.4 on 2021-06-24 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jerseyshop', '0018_auto_20210624_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubjerseydetails',
            name='price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ntjerseydetails',
            name='price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
