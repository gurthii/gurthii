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