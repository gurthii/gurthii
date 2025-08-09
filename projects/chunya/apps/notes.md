# Pengo (Django app)
Start the project: `django-admin startproject pengo`

Run the project: `py manage.py runserver`

Creating first app to cater for the home page: `py manage.py startapp homeapp`

## Django views
- replace default views in app with: 
```py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello world!")
```

# URLs
- in the same folder as views of app, create urls.py with below content:
```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```
- route app to root by editting urls.py in project folder:
```py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('homeapp.urls')),
    path('admin/', admin.site.urls),
]
```
# Templates
- create templates folder in app folder and add html doc `index.html`
- modify views to now render the html file:
```py
from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
```
- let's tell django of the new app in the `settings.py` in the projects root folder, and add under INSTALLED_APPS[]:
```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'homeapp'
```
- run some migrations before running the site again:
`py manage.py migrate`

# Switch from SQLite to PostgreSQL
- add the below in the `DATABASES` section in the `settings.py`:
```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tengoapp',
        'USER': 'tengoboos',
        'PASSWORD': 'GArtyPOpGreN',
        'HOST': '127.0.0.1',  # or your DB server IP
        'PORT': '5432',       # default Postgres port
    }
}
```
- apply migrations `py manage.py migrate` and you'll be set

# Django models
- in `models.py` in `/homeapp/` folder, open add a `ProductTracer` class and describe the table fields in it:
```py
from django.db import models

class ProductTracer(models.Model):
  prod_name = models.CharField(max_length=255)
  prod_sku = models.CharField(max_length=255)
  prod_price = models.CharField(max_length=255)
  prod_url = models.CharField(max_length=255)
```
- all models are created as tables in the database, this is actioned by running a migration: `py manage.py makemigrations homeapp`
- this changes are recorded in the migrations folder
- run this one more time `python manage.py migrate` to actually create the table based on what's in the `/migrations/`folder
-- (optional) you can view the related sql by running `py manage.py sqlmigrate homeapp 0001`
-- adding items manually
```py
# opens shell in cmd
python manage.py shell

# grabbing the specific model
from homeapp.models import ProductTracer 

# returns a queryset, initially empty
ProductTracer.objects.all() 

# adding data manually
home = ProductTracer(prod_name='Aesthetic Shades Sunglasses UV400 For Women Men Eyeglasses', prod_sku='FA113FC3XCX9CNAFAMZ', prod_price='189', prod_url='http://jumia.co.ke/fashion-aesthetic-shades-sunglasses-uv400-for-women-men-eyeglasses-223882473.html')
home.save()

# checking if the data has been added to ProductTracer 
ProductTracer.objects.all().values()

# adding multiple data items
n = ProductTracer(prod_name='', prod_sku='', prod_price='', prod_url='')
m = ProductTracer(prod_name='', prod_sku='', prod_price='', prod_url='')
items_list = [n, m]
for i in items_list:
    i.save()

# update existing records, first get records (model)
from homeapp.models import ProductTracer

# get all specific object
y = ProductTracer.objects.all()[0]
y.prod_name # confirming value
y.prod_price = 190 # change into new value
y.save() # save change

# deleting records
y.delete()
```

# Improving models for context relevance
```py
from django.db import models
from decimal import Decimal  # used later when creating prices

class ProductsTable(models.Model):
    sku = models.CharField(max_length=255, primary_key=True)  # product code, must be unique but Django will still add an id unless you specify primary_key=True
    name = models.CharField(max_length=255)                   # short text, required
    url = models.URLField()                                   # must be provided, else add (blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.sku})"                    # nice readable string for admin/shell


class PricesTable(models.Model):
    sku = models.ForeignKey(
        ProductsTable,         # relation points to the ProductsTable model
        to_field='sku',        # store the ProductsTable.sku value (not its numeric id)
        on_delete=models.CASCADE,
        related_name='prices'  # lets you do product.prices.all()
    )
    current_price = models.DecimalField(max_digits=12, decimal_places=2)  # money value 10 digits before 2 decimal places
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sku.sku} - {self.current_price}"
```
- save models.py and run migrations
`py manage.py makemigrations homeapp`
`py manage.py migrate`
