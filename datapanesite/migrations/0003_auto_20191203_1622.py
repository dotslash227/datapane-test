# Generated by Django 2.0 on 2019-12-03 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datapanesite', '0002_entries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entries',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]