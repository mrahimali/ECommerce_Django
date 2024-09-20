from django.views import View
from django.shortcuts import render, redirect
from myStore.models import Cutomer
from myStore.models import Product


class Cart(View):
    def get(self, request):
        print(list(request.session.get('cart').keys()))
        ids=list(request.session.get('cart').keys())
        products=Product.get_products_by_ids(ids)
        print(products)
        return render(request, 'cart.html',{'products':products})