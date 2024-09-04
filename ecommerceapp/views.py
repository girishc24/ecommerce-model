from django.shortcuts import render
from django.http import HttpResponse
from . models import *

# Create your views here.
def index(request):
        # Create attributes
    color = Attribute.objects.create(name='Color')
    size = Attribute.objects.create(name='Size')

    # Create attribute values
    red = AttributeValue.objects.create(attribute=color, value='Red')
    blue = AttributeValue.objects.create(attribute=color, value='Blue')
    small = AttributeValue.objects.create(attribute=size, value='Small')
    large = AttributeValue.objects.create(attribute=size, value='Large')

    # Create a product
    tshirt = Product.objects.create(name='T-Shirt')

    # Assign categories to the product
    category1 = Category.objects.create(name='Clothing')
    tshirt.categories.add(category1)

    # Create product variants with different attribute combinations and prices
    variant1 = ProductVariant.objects.create(product=tshirt, price=10.99, stock=100)
    variant1.attributes.add(red, small)

    variant2 = ProductVariant.objects.create(product=tshirt, price=12.99, stock=50)
    variant2.attributes.add(red, large)

    variant3 = ProductVariant.objects.create(product=tshirt, price=11.99, stock=80)
    variant3.attributes.add(blue, small)

    variant4 = ProductVariant.objects.create(product=tshirt, price=13.99, stock=40)
    variant4.attributes.add(blue, large)
    return HttpResponse("Inserted")
