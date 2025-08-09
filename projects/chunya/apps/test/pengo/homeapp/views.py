from django.shortcuts import render
from .models import ProductsTable, PricesTable

def home(request):
  return render(request, 'index.html')

def prods(request):
  myproducts = ProductsTable.objects.all()
  print(myproducts)
  return render(request, 'results.html', {'myproducts' : myproducts})
