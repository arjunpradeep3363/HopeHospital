# Generated by Django 4.1.7 on 2023-08-11 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_contactdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicineCartdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Medicine_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.CharField(blank=True, max_length=300, null=True)),
                ('Total_Price', models.IntegerField(blank=True, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]