# Generated by Django 5.1.2 on 2024-10-25 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_product_compound_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
