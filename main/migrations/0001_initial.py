# Generated by Django 4.2.5 on 2023-09-10 03:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('item_id', models.UUIDField(default=uuid.UUID('854ae550-53cd-4bff-9c18-2bc31bca4075'), editable=False, primary_key=True, serialize=False, unique=True)),
                ('item_type', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.IntegerField(default=1)),
                ('power', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('unique_skill', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
