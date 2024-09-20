from django.contrib import admin
from django.urls import path
from .views import home, login, signup, cart

urlpatterns = [
    path('', home.Home.as_view(), name='homePage'),
    path('signup/', signup.SignUp.as_view(), name='signup' ),
    path('login/', login.Login.as_view(), name='login'),
    path('logout',login.logout, name='logout'),
    path('cart',cart.Cart.as_view(), name='cart')
]
