from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    name = models.CharField(max_length=200)
    description = models.TextField()
    compound = models.TextField(null=True)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name


class Recipe(models.Model):
    products = models.ManyToManyField(Product, related_name='recipes', blank=True)

    image = models.ImageField(null=True)
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    short_description = models.TextField(max_length=100)
    description = models.TextField()
