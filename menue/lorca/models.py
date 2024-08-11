from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=60)
    fname = models.CharField(max_length=60)

    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='categories/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=60)
    fname = models.CharField(max_length=60)

    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to='items/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name



