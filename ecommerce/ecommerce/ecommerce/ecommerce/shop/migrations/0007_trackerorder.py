# Generated by Django 3.0.6 on 2020-06-07 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_myuserproductorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='trackerOrder',
            fields=[
                ('updateId', models.AutoField(primary_key=True, serialize=False)),
                ('orderId', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=5000)),
                ('timeStamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]