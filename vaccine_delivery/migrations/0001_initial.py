# Generated by Django 3.1.5 on 2021-01-25 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DistrictModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('active', models.IntegerField()),
                ('population_2020', models.IntegerField()),
                ('batch_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StateModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100)),
                ('active', models.IntegerField()),
                ('population_2020', models.IntegerField()),
                ('accessibility', models.IntegerField()),
                ('children', models.IntegerField()),
                ('senior_citizen', models.IntegerField()),
                ('all_health_workers_percent', models.FloatField()),
                ('death_rate', models.FloatField()),
                ('ratio_vacant_beds', models.FloatField()),
                ('batch_no', models.IntegerField()),
                ('percentage_vaccine_delivery', models.FloatField()),
            ],
            options={
                'ordering': ['batch_no', 'percentage_vaccine_delivery'],
            },
        ),
    ]
