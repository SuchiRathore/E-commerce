from django.shortcuts import render,redirect
from django.views import View
from . models import *
from django.db.models import Q
from django.http import JsonResponse


class ProductView(View):
 def get(self,request):
  mobile =Product.objects.filter(category="M")
  laptop =Product.objects.filter(category="L")
  topweres =Product.objects.filter(category="TW")
  bottomweres =Product.objects.filter(category="BW")
  print(bottomweres)
  return render (request,"app/home.html",
                 {"mobile":mobile,
                  "laptop":laptop,
                  "topweres":topweres,
                  "bottomweres":bottomweres   
                 },
                 )

class ProductDetailView(View):
 def get(self,request,pk):
  product= Product.objects.get(pk=pk)
  item_alredy_in_cart = False
  if request.user.is_authenticated:
   item_alredy_in_cart=Cart.objects.filter(
    Q(product=product.id)& Q(user = request.user)
   
   ).exists()
   return render(request,"app/productdetail.html",{"product":product,"item_alredy_in_cart":item_alredy_in_cart})
  else:
   return render(request,"app/productdetail.html",{"product":product,"item_alredy_in_cart":item_alredy_in_cart})
   

def add_to_cart(request):
 user = request.user
 product_id = request.GET.get("prod_id")
 product = Product.objects.get(id=product_id)
 Cart(user=user,product=product).save()
 return redirect("/cart")



def showcart(request):
 if request.user.is_authenticated:
  user = request.user
  cart = Cart.objects.filter(user=user)
  amount = 0.0
  shipping_amount = 70.0
  total_amount = 0.0
  cart_product = [p for p in Cart.objects.all()
                  if p.user == user]
  if cart_product:
      for p in cart_product:
         tempamount = p.quantity * p.product.discounted_price
         amount +=  tempamount
         total_amount = amount + shipping_amount
      return render(
         request,
         "app/addtocart.html",
         {"carts": cart, "total_amount":  total_amount,  "amount": amount },
      )
  else:
    return render(request , "app/emptycart.html")
     

def plus_cart(request):
  if request.method == "GET":
   prod_id = request.GET["prod_id"]
   c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
   c.quantity += 1
   c.save()
   amount = 0.0
   shipping_amount = 70.0
   cart_product =[p for p in Cart.objects.all() if p.user == request.user]
   for p in cart_product:
    tempamount = p.quantity * p.product.discounted_price
    amount += tempamount

    data = {
     "quantity":c.quantity,
     "amount" :amount,
     "totalamount": amount + shipping_amount,
    }
    return JsonResponse(data)
   
def minus_cart(request):
  if request.method == "GET":
   prod_id = request.GET["prod_id"]
   c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
   c.quantity -= 1
   c.save()
   amount = 0.0
   shipping_amount = 70.0
   cart_product =[p for p in Cart.objects.all() if p.user == request.user]
   for p in cart_product:
    tempamount = p.quantity * p.product.discounted_price
    amount += tempamount

    data = {
     "quantity":c.quantity,
     "amount" :amount,
     "totalamount": amount + shipping_amount,
    }
    return JsonResponse(data)

def remove_cart(request):
  if request.method == "GET":
   prod_id = request.GET["prod_id"]
   c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
   c.delete()
   amount = 0.0
   shipping_amount = 70.0
   cart_product =[p for p in Cart.objects.all() if p.user == request.user]
   for p in cart_product:
    tempamount = p.quantity * p.product.discounted_price
    amount += tempamount

    data = {
     "amount" :amount,
     "totalamount": amount + shipping_amount,
    }
    return JsonResponse(data)       


def mobile(request,data=None):
 if data == None:
  mobiles = Product.objects.filter(category="M")
 elif data == "Redmi" or data == "Samsung":
  mobiles = Product.objects.filter(category="M").filter(brand=data)
 elif data == "below":
  mobiles = Product.objects.filter(category ="M").filter(discounted_price__gt=10000)
 return render(request,"app/mobile.html",{"mobiles":mobiles})
    

def laptop(request,data=None):
 if data == None:
  laptops = Product.objects.filter(category="L")
 elif data == "HP" or data == "Lenovo":
  laptops = Product.objects.filter(category="l").filter(brand=data)
 elif data == "below":
  laptops = Product.objects.filter(category ="l").filter(discounted_price__gt=10000)
 return render(request,"app/laptop.html",{"laptops":laptops})        

 

#def home(request):
 #return render(request, 'app/home.html')


def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

# def mobile(request):
#  return render(request, 'app/mobile.html')



def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
