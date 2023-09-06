# Generated by Django 4.1.7 on 2023-08-13 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_delete_checkout_checkoutdb_address_checkoutdb_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointmentdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Doctor_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Date', models.CharField(blank=True, max_length=100, null=True)),
                ('Time', models.CharField(blank=True, max_length=100, null=True)),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Phone', models.IntegerField(blank=True, null=True)),
                ('Message', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]