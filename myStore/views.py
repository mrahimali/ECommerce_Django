from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Category, Cutomer
from django.contrib.auth.hashers import make_password, check_password



# Create your views here.
def home(request):
    products=None
    categories=Category.get_all_categories()
    print(request.GET.get('category'))
    category_id=request.GET.get('category')
    if category_id:
        products=Product.get_all_products_by_id(category_id)
    else:
         products=Product.get_all_products()

    
    data={
        'products':products,
        'categories':categories
    }
    print(products)
    return render(request, 'home/index.html', context=data)

def validateCustomer(cutomer):
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

def registerUser(request):
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
    error_message=validateCustomer(cutomer)
    

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

def SignUp(request):
    if request.method=='GET':
        return render(request, 'signup.html')
    else:
        return registerUser(request)
    
def Login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
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
                return redirect('/')
            else:
                error_message="Password Invalid!!!"
        else:
            error_message="Email Invalid!!!"
        print(customer)
        print(email, password)
        return render(request, 'login.html', {'error':error_message, 'values':filled_value})
        
    