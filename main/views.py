from django.shortcuts import render, redirect
from main.forms import ProductForms
from main.models import Product, ProductForm
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def show_main(request):
    products = Product.objects.all()
    ordered = ProductForm.objects.all()

    context = {
        'name': 'Candy Baby Parfum',
        'price': 'Rp 150.000',
        'description': 'Candy Baby adalah body mist yang manis dan menyegarkan, dengan aroma permen kapas yang menggoda dan vanilla yang lembut. Parfum ini memberikan sensasi seperti berada di dunia permen yang ceria, sempurna untuk mereka yang ingin menonjolkan sisi playful dan feminin. Dengan aroma ringan namun tahan lama, Candy Baby adalah pilihan ideal untuk digunakan sehari-hari.',
        'quantity': '10',
        'products': products,
        'ordered':ordered,
    }

    return render(request, "main.html", context)

def add_product(request):
    form = ProductForms(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')
    # else:
    #     form = ProductForms()  # Form diubah ke ProductForm
    return render(request, 'add_product.html', {'form': form})

# def product_list(request):
#     products = ProductForm.objects.all()  
#     return render(request, 'product_list.html', {'products': products})

def show_xml(request):
    data = ProductForm.objects.all()  
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ProductForm.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ProductForm.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ProductForm.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
