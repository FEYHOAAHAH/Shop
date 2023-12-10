# Generated by Django 4.2.8 on 2023-12-10 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('seller', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('category', models.CharField(max_length=255)),
                ('application_area', models.CharField(max_length=255)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('rating', models.FloatField()),
            ],
        ),
    ]
