# Generated by Django 5.1.2 on 2024-10-24 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='Product',
            field=models.ManyToManyField(blank=True, related_name='recipes', to='menu.product'),
        ),
    ]