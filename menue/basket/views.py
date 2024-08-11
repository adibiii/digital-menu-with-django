from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from basket.models import Basket, BasketLine
from lorca.models import Item


# Create your views here.
@require_POST
def add(request, table_id):
    basket_id = request.COOKIES.get('basket_id', None)
    basket = get_object_or_404(Basket, pk=basket_id)
    if basket.state == 2 or basket.state == 3 or basket.is_paid:
        return redirect('home', table_id)
    item_id = request.POST.get('item_id', None)
    quantity = request.POST.get('quantity', 1)
    item = get_object_or_404(Item, pk=item_id)
    if item in [basketline.item for basketline in basket.basket_lines.all()]:
        basket_line = basket.basket_lines.filter(item=item).first()
        basket_line.quantity += int(quantity)
        basket_line.save()
        messages.success(request, "Your message has been submitted.")
        return redirect('home', table_id)
    basket_line = BasketLine.objects.create(basket=basket, item=item, quantity=quantity)
    messages.success(request, "Your message has been submitted.")
    return redirect('home', table_id)


def orders_list(request, table_id):
    basket_id = request.COOKIES.get('basket_id', None)
    basket = get_object_or_404(Basket, pk=basket_id)
