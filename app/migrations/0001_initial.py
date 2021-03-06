# Generated by Django 3.0.5 on 2020-04-11 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Earthquake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('latitude', models.DecimalField(decimal_places=5, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=5, max_digits=10)),
                ('depth', models.DecimalField(decimal_places=5, max_digits=10)),
                ('magnitude', models.DecimalField(decimal_places=5, max_digits=10)),
            ],
        ),
    ]
