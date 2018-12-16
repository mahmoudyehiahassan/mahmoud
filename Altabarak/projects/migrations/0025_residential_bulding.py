# Generated by Django 2.0.6 on 2018-12-16 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0024_hospital'),
    ]

    operations = [
        migrations.CreateModel(
            name='Residential_bulding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=300)),
                ('project_nature', models.CharField(max_length=30)),
                ('royal_side', models.CharField(max_length=150)),
                ('consultant', models.CharField(max_length=150)),
                ('executive_status', models.CharField(max_length=150)),
                ('youtube_url', models.CharField(max_length=500)),
                ('add_Date', models.DateField()),
            ],
        ),
    ]
