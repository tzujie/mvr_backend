# Generated by Django 4.2.3 on 2023-07-15 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=20)),
            ],
            options={"db_table": "account",},
        ),
    ]
