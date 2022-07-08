from django.shortcuts import render, get_object_or_404

from cart.form import CartAddProductForm
from shop.models import Product, Category


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(klass=Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/list.html', {'categories': categories, 'category': category, 'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(klass=Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/detail.html', {'product': product,'cart_product_form':cart_product_form})
