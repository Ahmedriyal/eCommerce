# Generated by Django 3.2.4 on 2021-06-24 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jerseyshop', '0019_auto_20210624_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubjerseydetails',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ntjerseydetails',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
