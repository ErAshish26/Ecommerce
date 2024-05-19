from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.

def index(request):
    products=Product.objects.all()
    print(products)
    n=len(products)
    nSlide=n//4+ceil((n/4)-(n//4))
    params={'no_of_slides':nSlide,'range': range(1,nSlide),'product':products}
    # allProds=[[products,range(1,len(products)),nSlide]],
    # [[products,range(1,len(products)),nSlide]]
    # params={'allProds':allProds}
    return render(request,'shop/index.html', params)

def about(request):
    return render(request,'shop/about.html')
def contact(request):
    return render(request,'shop/contact.html')
def track(request):
    return render(request,'shop/track.html')
def search(request):
    return render(request,'shop/search.html')
def products(request):
    return HttpResponse('products')
def checkout(request):
    return HttpResponse('checkout')