# Generated by Django 2.2 on 2019-05-24 18:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_auto_20190524_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Сума'),
        ),
    ]
