# Generated by Django 3.1.7 on 2021-06-27 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20210624_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='Searched_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=400)),
            ],
        ),
    ]
