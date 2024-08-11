from django.db import models

from lorca.models import Item


# Create your models here.


class Basket(models.Model):
    NOT_CONFIRMED = 1
    CONFIRMED = 2
    READY = 3
    ATTRIBUTE_TYPE_FIELDS = [
        (NOT_CONFIRMED, 'not confirmed'),
        (CONFIRMED, 'confirmed'),
        (READY, 'ready')
    ]
    user = models.CharField(max_length=60, blank=True, null=True)
    table = models.SmallIntegerField()
    is_paid = models.BooleanField(default=False)
    state = models.SmallIntegerField(default=NOT_CONFIRMED, choices=ATTRIBUTE_TYPE_FIELDS)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}'


class BasketLine(models.Model):
    item = models.ForeignKey(Item, on_delete=models.PROTECT, related_name='orders')
    basket = models.ForeignKey(Basket, on_delete=models.PROTECT, related_name='basket_lines')
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.item.name
