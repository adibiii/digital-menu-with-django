from django.shortcuts import render, redirect, get_object_or_404

from basket.models import Basket
from lorca.models import Category


# Create your views here.


def index(request):
    return redirect('home', 0)


def home(request, table_id):
    basket_id = request.COOKIES.get('basket_id', None)
    categories = Category.objects.filter(is_active=True)
    if basket_id is None:
        basket = Basket.objects.create(table=table_id)
        context = {'categories': categories, 'basket': basket, 'table_id': table_id}
        response = render(request, 'lorca/mymenue.html', context=context)
        response.set_cookie('basket_id', basket.id)
        return response
    else:
        basket = get_object_or_404(Basket, pk=basket_id)
        if basket.state == 2 or basket.state == 3 or basket.is_paid:
            basket = Basket.objects.create(table=table_id)
            context = {'categories': categories, 'basket': basket, 'table_id': table_id}
            response = render(request, 'lorca/mymenue.html', context=context)
            response.set_cookie('basket_id', basket.id)
            return response
        context = {'categories': categories, 'basket': basket, 'table_id': table_id}
        return render(request, 'lorca/mymenue.html', context=context)







