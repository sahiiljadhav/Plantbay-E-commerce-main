# Generated by Django 5.0.6 on 2024-07-04 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0003_item_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
