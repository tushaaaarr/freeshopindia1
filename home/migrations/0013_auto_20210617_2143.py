# Generated by Django 3.1.7 on 2021-06-17 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20210617_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_product2',
            name='price',
            field=models.IntegerField(),
        ),
    ]
