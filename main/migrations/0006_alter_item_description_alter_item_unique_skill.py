# Generated by Django 4.2.5 on 2023-09-06 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_item_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='unique_skill',
            field=models.TextField(blank=True),
        ),
    ]
