from django.views import View
from django.shortcuts import render, redirect
from myStore.models import Cutomer
from django.contrib.auth.hashers import make_password, check_password

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        filled_value={
            'email':email
        }
        error_message=None
        customer=Cutomer.getCustomerByEmail(email)
        if customer:
            flag=check_password(password, customer.password)
            if flag:
                request.session['cutomer_id']=customer.id
                request.session['email']=customer.email
                request.session['name']=customer.first_name
                return redirect('/')
            else:
                error_message="Password Invalid!!!"
        else:
            error_message="Email Invalid!!!"
        print(customer)
        print(email, password)
        return render(request, 'login.html', {'error':error_message, 'values':filled_value})

# def Login(request):
#     if request.method == 'GET':
#         return render(request, 'login.html')
#     else:
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         filled_value={
#             'email':email
#         }
#         error_message=None
#         customer=Cutomer.getCustomerByEmail(email)
#         if customer:
#             flag=check_password(password, customer.password)
#             if flag:
#                 return redirect('/')
#             else:
#                 error_message="Password Invalid!!!"
#         else:
#             error_message="Email Invalid!!!"
#         print(customer)
#         print(email, password)
#         return render(request, 'login.html', {'error':error_message, 'values':filled_value})
        
    