# Generated by Django 3.0.7 on 2020-07-28 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GPQuants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='currencies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstCurrencyChoice', models.TextField()),
                ('secondCurrencyChoice', models.TextField()),
            ],
        ),
    ]
