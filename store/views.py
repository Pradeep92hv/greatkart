from django.shortcuts import render,get_object_or_404

# Create your views here.

from .models import Product
from category.models import Category
from carts.models import CartItem,Cart

from carts.views import _cart_id


# def store(request,category_slug=None):
#     categories=None
#     products=None
    
#     if category_slug!=None:
#        print(category_slug)
#        categories= get_object_or_404(Category, slug=category_slug)
#        products=Product.objects.filter(category=categories,is_available=True)
#        products_count=products.count()
       
#     else:
#         products=Product.objects.filter(is_available=True)
#         products_count=products.count()
        
#     context={
#         'products':products,
#         'products_count':products_count,
#     }
#     return render(request,'store/store.html',context)


#  for pagination


from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator


def store(request,category_slug=None):
    categories=None
    products=None
    
    if category_slug!=None:
       print(category_slug)
       categories= get_object_or_404(Category, slug=category_slug)
       products=Product.objects.filter(category=categories,is_available=True).order_by('id')
       products_count=products.count()
       paginator=Paginator(products,4)
       page=request.GET.get('page')
       paged_products=paginator.get_page(page)
       
    else:
        products=Product.objects.filter(is_available=True).order_by('id')
        paginator=Paginator(products,3)
        page=request.GET.get('page')
        paged_products=paginator.get_page(page)
        products_count=products.count()
        
    context={
        'products':paged_products,
        'products_count':products_count,
    }
    return render(request,'store/store.html',context)


def product_details(request,category_slug,product_slug):
    
    try:
        # single_product=Product.objects.get(category__slug=category_slug,slug=product_slug)
        selected_category = get_object_or_404(Category, slug=category_slug)
        single_product = get_object_or_404(Product, category=selected_category, slug=product_slug)
        
        in_cart=CartItem.objects.filter(cart__cart_id=_cart_id(request),product=single_product).exists()     # to check is product already in cart or not
        
    except Exception as e:
        raise e
    
    # selected_category = get_object_or_404(Category, slug=category_slug)
    # single_product = get_object_or_404(Product, category=selected_category, slug=product_slug)
    #  only  above 2 line are working
    context={
        'single_product': single_product,
        'in_cart':in_cart,
        
    }    
    return render(request,'store/product_details.html',context)



from django.db.models import Q

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword')

        if keyword:
            products = Product.objects.filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            products_count=products.count()
    context = {
        'products': products,
        'products_count':products_count,
        
    }        
    print(products.count(), "jvhmh")
    return render(request, 'store/store.html', context)

