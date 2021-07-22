# Generated by Django 3.2.4 on 2021-07-20 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4)),
                ('password', models.CharField(max_length=4)),
                ('pay', models.DecimalField(decimal_places=1, default=0, max_digits=8)),
            ],
            options={
                'db_table': 'payment',
            },
        ),
    ]
