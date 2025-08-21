# from django.db import models

# class ProductTracer(models.Model):
#   prod_name = models.CharField(max_length=255)
#   prod_sku = models.CharField(max_length=255)
#   prod_price = models.CharField(max_length=255)
#   prod_url = models.CharField(max_length=255)
  
## redefined prices/product models (db tables)
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

class ProductRequest(models.Model):
    """Model to handle user requests for product tracking from the home page form"""
    REQUEST_STATUS = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]
    
    input_data = models.CharField(max_length=500, help_text="Product URL or SKU entered by user")
    request_type = models.CharField(
        max_length=10, 
        choices=[('url', 'URL'), ('sku', 'SKU')],
        default='url'
    )
    status = models.CharField(max_length=20, choices=REQUEST_STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True, help_text="Any additional notes or error messages")
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.input_data[:50]} - {self.status} ({self.created_at.strftime('%Y-%m-%d')})"

