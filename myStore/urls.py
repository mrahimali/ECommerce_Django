from django.contrib import admin
from django.urls import path
from .views import home, login, signup, cart, checkOut, order
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', home.Home.as_view(), name='homePage'),
    path('signup/', signup.SignUp.as_view(), name='signup' ),
    path('login/', login.Login.as_view(), name='login'),
    path('logout',login.logout, name='logout'),
    path('cart',cart.Cart.as_view(), name='cart'),
    path('check-out', checkOut.CheckOut.as_view(), name='check-out'),
    path('orders', auth_middleware(order.OrderView.as_view()), name='orders'),
]
