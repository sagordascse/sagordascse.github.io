# Generated by Django 3.0.6 on 2020-06-06 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200528_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='myUserProductOrder',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_json', models.CharField(default='', max_length=1000)),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(default='', max_length=100)),
                ('zip_code', models.CharField(default='', max_length=15)),
                ('phone_number', models.CharField(default='', max_length=15)),
            ],
        ),
    ]