# Generated by Django 5.0.6 on 2024-07-14 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0019_alter_address_options_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='one_click_purchase',
        ),
    ]