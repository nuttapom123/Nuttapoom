# Generated by Django 5.0.2 on 2024-03-02 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foood',
            name='special_pice',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='foood',
            name='is_special',
            field=models.BooleanField(default=False),
        ),
    ]
