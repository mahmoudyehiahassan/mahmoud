# Generated by Django 2.0.6 on 2018-12-16 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20180911_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='First_Photo_Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.FileField(upload_to='documents')),
                ('Titile', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HomeProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainPhoto', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('subPhoto', models.FileField(upload_to='documents/')),
                ('Title', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='HomeSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Photo', models.FileField(upload_to='documents/')),
                ('PhotoTitile', models.CharField(max_length=100)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=300)),
                ('project_nature', models.CharField(max_length=30)),
                ('royal_side', models.CharField(max_length=150)),
                ('consultant', models.CharField(max_length=150)),
                ('executive_status', models.CharField(max_length=150)),
                ('youtube_url', models.CharField(max_length=500)),
                ('add_Date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OurNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NewsTitile', models.CharField(max_length=100)),
                ('NewsDescription', models.CharField(max_length=180)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hospitals', models.IntegerField(default=0)),
                ('Banks', models.IntegerField(default=0)),
                ('Hotels', models.IntegerField(default=0)),
                ('Malls', models.IntegerField(default=0)),
                ('Administration_Buildings', models.IntegerField(default=0)),
                ('Private_Schools', models.IntegerField(default=0)),
                ('General_Schools', models.IntegerField(default=0)),
                ('Factories', models.IntegerField(default=0)),
                ('Residential_Projects', models.IntegerField(default=0)),
                ('Compound', models.IntegerField(default=0)),
                ('Colleges_Institutes', models.IntegerField(default=0)),
            ],
        ),
    ]
