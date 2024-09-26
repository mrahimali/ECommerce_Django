from django.views import View
from django.shortcuts import render, redirect
from myStore.models import Product, Order,Cutomer


class CheckOut(View):
    def post(self, request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer=request.session.get('customer')
        cart=request.session.get('cart')
        products=Product.get_products_by_ids(list(cart.keys()))
        # products=list(Prod)
        for product in products:
            order=Order(customer=Cutomer(id=customer), 
                        product=product, 
                        price=product.price, 
                        quantity=cart.get(str(product.id)),
                        address=address, 
                        phone=phone)
            print(order.placeOrder())
        # print(address, phone, customer, cart, products)
        request.session['cart']={}

        return redirect('cart')