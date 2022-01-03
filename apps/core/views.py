from django.shortcuts import render
from django.core.paginator import Paginator ,EmptyPage
from apps.store.models import Product, Category

def frontpage(request):
    products = Product.objects.filter(is_featured=True)
    featured_categories = Category.objects.filter(is_featured=True)
    popular_products = Product.objects.all().order_by('-num_visits')[0:4]
    recently_viewed_products = Product.objects.all().order_by('-last_visit')[0:4]
    

    context = {
        'products': products,
        'featured_categories': featured_categories,
        'popular_products': popular_products,
        'recently_viewed_products': recently_viewed_products
    
    }

    return render(request, 'frontpage.html', context)


def all_products(request):
    all_products = Product.objects.all()
    p=Paginator(all_products, 12)
    
    page_num = request.GET.get('page',1)

    try:
        page =p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    
    context = {
        'all_products': page,
    }

    return render(request, 'all_products.html', context)




def contact(request):
    return render(request, 'contact.html')

def allcategories(request):
    return render(request, 'allcategories.html')


def about(request):
    return render(request, 'about.html')