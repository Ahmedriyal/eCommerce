# Generated by Django 3.2.4 on 2021-06-21 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jerseyshop', '0007_auto_20210620_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubjerseydetails',
            name='authenticity',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='clubjerseydetails',
            name='small_image1',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='clubjerseydetails',
            name='small_image2',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='clubjerseydetails',
            name='small_image3',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='clubjerseydetails',
            name='small_image4',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='clubjerseydetails',
            name='team_badge',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ntjerseydetails',
            name='authenticity',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ntjerseydetails',
            name='small_image1',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='ntjerseydetails',
            name='small_image2',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='ntjerseydetails',
            name='small_image3',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='ntjerseydetails',
            name='small_image4',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='ntjerseydetails',
            name='team_badge',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='clubjerseydetails',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='ntjerseydetails',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
