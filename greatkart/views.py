from django.http import HttpResponse
from django.shortcuts import render

from store.models import Product

def home(request):
    # return HttpResponse("hiii")
    products=Product.objects.filter(is_available=True)
    context={
        'products':products,
    }
    return render(request,'app/home.html',context)
