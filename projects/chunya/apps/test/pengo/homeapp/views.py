from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from .models import ProductsTable, PricesTable, ProductRequest
import re
import json
from decimal import Decimal

def home(request):
    if request.method == 'POST':
        product_input = request.POST.get('product_input', '').strip()
        
        if product_input:
            # Determine if input is URL or SKU
            is_url = bool(re.match(r'^https?://', product_input))
            request_type = 'url' if is_url else 'sku'
            
            # Create product request
            product_request = ProductRequest.objects.create(
                input_data=product_input,
                request_type=request_type,
                status='pending'
            )
            
            try:
                if is_url:
                    # Search by URL
                    product = ProductsTable.objects.filter(url__icontains=product_input).first()
                else:
                    # Search by SKU
                    product = ProductsTable.objects.filter(sku__icontains=product_input).first()
                
                if product:
                    # Product found - redirect to results with product data
                    product_request.status = 'completed'
                    product_request.processed_at = timezone.now()
                    product_request.save()
                    return redirect('results')
                else:
                    # Product not found - create it with sample data
                    try:
                        # Generate a unique SKU if input is URL
                        if is_url:
                            sku = f"NEW_{int(timezone.now().timestamp())}"
                            name = f"Product from {product_input[:50]}"
                        else:
                            sku = product_input
                            name = f"Product {product_input}"
                        
                        # Create new product
                        new_product = ProductsTable.objects.create(
                            sku=sku,
                            name=name,
                            url=product_input if is_url else ""
                        )
                        
                        # Add sample price history for the chart
                        sample_prices = [
                            (Decimal('180.00'), timezone.now() - timezone.timedelta(days=180)),
                            (Decimal('600.00'), timezone.now() - timezone.timedelta(days=120)),
                            (Decimal('500.00'), timezone.now() - timezone.timedelta(days=60)),
                            (Decimal('880.00'), timezone.now() - timezone.timedelta(days=30)),
                            (Decimal('200.00'), timezone.now() - timezone.timedelta(days=15)),
                            (Decimal('360.00'), timezone.now() - timezone.timedelta(days=0))
                        ]
                        
                        for price, timestamp in sample_prices:
                            PricesTable.objects.create(
                                sku=new_product,
                                current_price=price,
                                timestamp=timestamp
                            )
                        
                        # Mark request as completed
                        product_request.status = 'completed'
                        product_request.notes = f'New product created: {name}'
                        product_request.processed_at = timezone.now()
                        product_request.save()
                        
                        messages.success(request, f'New product "{name}" has been added to our tracking system!')
                        return redirect('results')
                        
                    except Exception as e:
                        # Handle creation errors
                        product_request.status = 'failed'
                        product_request.notes = f'Error creating product: {str(e)}'
                        product_request.processed_at = timezone.now()
                        product_request.save()
                        
                        messages.error(request, 'An error occurred while creating the product.')
                        return redirect('results')
                    
            except Exception as e:
                # Handle any other errors
                product_request.status = 'failed'
                product_request.notes = f'Error processing request: {str(e)}'
                product_request.processed_at = timezone.now()
                product_request.save()
                
                messages.error(request, 'An error occurred while processing your request.')
                return redirect('results')
        else:
            messages.error(request, 'Please enter a product URL or SKU.')
    
    return render(request, 'index.html')

def prods(request):
    # Get all products with their latest prices
    products_with_prices = []
    
    for product in ProductsTable.objects.all():
        latest_price = product.prices.order_by('-timestamp').first()
        if latest_price:
            products_with_prices.append({
                'product': product,
                'latest_price': latest_price,
                'price_history': list(product.prices.order_by('timestamp').values('current_price', 'timestamp'))
            })
    
    # Prepare chart data for the first product (or create sample data if none exist)
    chart_data = None
    if products_with_prices:
        first_product = products_with_prices[0]
        chart_data = {
            'labels': [price['timestamp'].strftime('%b %d, %Y') for price in first_product['price_history']],
            'prices': [float(price['current_price']) for price in first_product['price_history']],
            'product_name': first_product['product'].name,
            'current_price': float(first_product['latest_price'].current_price),
            'last_updated': first_product['latest_price'].timestamp.strftime('%B %d, %Y at %I:%M %p')
        }
    else:
        # Sample data for demonstration
        chart_data = {
            'labels': ['Jan 01, 2025', 'Mar 01, 2025', 'May 01, 2025', 'Jul 01, 2025'],
            'prices': [180, 600, 500, 880, 200, 360],
            'product_name': 'Sample Product',
            'current_price': 360,
            'last_updated': 'July 12, 2025 at 11:00 AM'
        }
    
    context = {
        'myproducts': products_with_prices,
        'chart_data': json.dumps(chart_data),
        'chart_product': chart_data
    }
    
    return render(request, 'results.html', context)
