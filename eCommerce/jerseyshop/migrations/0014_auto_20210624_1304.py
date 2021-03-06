# Generated by Django 3.2.4 on 2021-06-24 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jerseyshop', '0013_auto_20210624_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='jersey',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='club_jersey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jerseyshop.clubjerseydetails'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='national_jersey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jerseyshop.ntjerseydetails'),
        ),
        migrations.DeleteModel(
            name='Jersey',
        ),
    ]
