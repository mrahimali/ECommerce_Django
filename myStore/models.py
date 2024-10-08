from django.db import models
import datetime

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    

    def __str__(self):
        return self.name
    


class Product(models.Model):
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    price=models.IntegerField()
    description=models.CharField(max_length=200)
    product_images=models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_id(category_id):
       if category_id:
            return Product.objects.filter(category=category_id)
       else:
            return Product.get_all_products()
       

    @staticmethod 
    def get_products_by_ids(ids):
        return Product.objects.filter(id__in=ids)

    def __str__(self):
        return self.name
    

class Cutomer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=255)

    def register(self):
        self.save()

    def isExist(self):
        if Cutomer.objects.filter(email=self.email):
            return True
        
    @staticmethod
    def getCustomerByEmail(email):
        try:
            return Cutomer.objects.get(email=email)
        except:
            return False 

    def __str__(self):
        return self.first_name

    

class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    customer =models.ForeignKey(Cutomer, on_delete=models.CASCADE)
    quantity= models.IntegerField(default=1)
    price=models.IntegerField()
    address=models.CharField(max_length=200, default='', blank=True)
    phone=models.CharField(max_length=13,default='', blank=True)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)


    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order\
            .objects\
            .filter(customer=customer_id)\
            .order_by('-date')