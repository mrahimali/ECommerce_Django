from django.shortcuts import render, redirect
from myStore.models import Cutomer
from django.contrib.auth.hashers import make_password

from django.views import View


class SignUp(View):
    def get(self, request):
        return render(request, 'signup.html')
    def post(self, request):
        postData=request.POST
        first_name=postData.get('fname')
        last_name=postData.get('lname')
        email=postData.get('email')
        phone=postData.get('phone')
        password=postData.get('password')


        filled_values={
            'fname':first_name,
            'lname':last_name,
            'phone':phone,
            'email':email,
        }
        # Validation
        error_message=None

        cutomer=Cutomer(first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                password=password
                )
        error_message=self.validateCustomer(cutomer)
        

        if not error_message:
            
            cutomer.password=make_password(cutomer.password)

            cutomer.register()
            return redirect('homePage')
            # cutomer.save()
        else:
            data={
                'values':filled_values,
                'error':error_message
            }
            return render(request, 'signup.html', data)
        

    def validateCustomer(self,cutomer):
        error_message=None
        if (not cutomer.first_name):
            error_message="First Name required !!"
        elif len(cutomer.first_name)<4:
            error_message="First name should be 4 character long"
        elif not cutomer.last_name:
            error_message="Last Name required !!"
        elif not cutomer.email:
            error_message="Email required !!"
        elif not cutomer.password:
            error_message="Password required !!"
        elif len(cutomer.phone)<10:
            error_message="Phone Number must be 10 digit long !!"
        elif cutomer.isExist():
                error_message="Email Address Already Exist!!!"

        return error_message
