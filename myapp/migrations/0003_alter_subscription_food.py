# Generated by Django 5.0.2 on 2024-03-02 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_foood_special_pice_alter_foood_is_special'),
        ('myapp', '0002_subscription_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='food',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='foods.foood'),
        ),
    ]
