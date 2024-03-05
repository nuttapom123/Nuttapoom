# Generated by Django 5.0.2 on 2024-03-02 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_foood_special_pice_alter_foood_is_special'),
        ('myapp', '0003_alter_subscription_food'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='food',
        ),
        migrations.AddField(
            model_name='subscription',
            name='food_set',
            field=models.ManyToManyField(to='foods.foood'),
        ),
    ]
