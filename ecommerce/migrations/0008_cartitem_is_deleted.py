# Generated by Django 3.2.16 on 2023-06-21 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_alter_cartitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
