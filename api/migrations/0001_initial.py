# Generated by Django 3.0.3 on 2022-04-15 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('widget', models.CharField(max_length=40000)),
            ],
        ),
    ]