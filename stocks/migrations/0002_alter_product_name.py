# Generated by Django 3.2.21 on 2023-11-08 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='paracetamol', max_length=25),
        ),
    ]
