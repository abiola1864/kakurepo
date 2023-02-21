from django.shortcuts import render, redirect
from .models import Product, Sale
from .forms import ProductForm, SaleForm

def home(request):
    return render(request, 'kakuapp/home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'kakuapp/product_list.html', {'products': products})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'kakuapp/product_create.html', {'form': form})

def product_edit(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'kakuapp/product_edit.html', {'form': form})

def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('product_list')

def sale_list(request):
    sales = Sale.objects.all()
    return render(request, 'kakuapp/sale_list.html', {'sales': sales})

def sale_create(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sale_list')
    else:
        form = SaleForm()
    return render(request, 'kakuapp/sale_create.html', {'form': form})

def sale_edit(request, pk):
    sale = Sale.objects.get(pk=pk)
    if request.method == 'POST':
        form = SaleForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            return redirect('sale_list')
    else:
        form = SaleForm(instance=sale)
    return render(request, 'kakuapp/sale_edit.html', {'form': form, 'sale': sale})


    else:
        form = SaleForm(instance=sale)
    return render(request, 'kakuapp/sale_edit.html', {'form': form})

def sale_delete(request, pk):
    sale = Sale.objects.get(pk=pk)
    sale.delete()
    return redirect('sale_list')
