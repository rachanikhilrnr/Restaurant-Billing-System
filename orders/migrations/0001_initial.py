# Generated by Django 4.2.2 on 2023-06-13 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customerorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starters', models.TextField()),
                ('lunch', models.TextField()),
                ('beverages', models.TextField()),
            ],
        ),
    ]
