import requests
from fuzzywuzzy import fuzz
import random

def fetch_dummy_products(api_url="https://api.escuelajs.co/api/v1/products?limit=100&offset=0", query=None):
    """
    Fetch products from EscuelaJS API, optionally filter by query using fuzzy matching.
    Adds synthetic 'platform' and normalizes fields to mimic multi-platform data.
    Returns list of products with title, price, stock, platform, rating.
    """
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        products = response.json()  # EscuelaJS returns a list directly
        
        # Normalize and add synthetic platform
        platforms = ['Amazon', 'Flipkart', 'eBay'] * (len(products) // 3 + 1)
        normalized_products = []
        for i, product in enumerate(products):
            # Simulate duplicates for cosmetics by reusing titles
            title = product.get('title', 'Unknown Product')
            if 'mascara' in title.lower() or 'lipstick' in title.lower() or random.random() < 0.3:  # Increase cosmetic matches
                for platform in platforms[:random.randint(1, 3)]:  # Create 1-3 duplicates
                    normalized_products.append({
                        'title': title,
                        'price': round(float(product.get('price', 0)) * random.uniform(0.9, 1.2), 2),  # Vary price
                        'stock': random.randint(10, 100),  # Synthetic stock
                        'platform': platform,
                        'rating': round(random.uniform(3.5, 5.0), 2),  # Synthetic rating
                        'category': product.get('category', {}).get('name', 'beauty'),  # Default to beauty
                        'description': product.get('description', 'No description'),
                        'images': product.get('images', []),
                    })
            else:
                normalized_products.append({
                    'title': title,
                    'price': float(product.get('price', 0)),
                    'stock': random.randint(10, 100),
                    'platform': platforms[i % len(platforms)],
                    'rating': round(random.uniform(3.5, 5.0), 2),
                    'category': product.get('category', {}).get('name', 'beauty'),
                    'description': product.get('description', 'No description'),
                    'images': product.get('images', []),
                })
        
        # Filter by query if provided
        if query:
            query = query.lower()
            filtered = [
                p for p in normalized_products
                if fuzz.partial_ratio(query, p.get('title', '').lower()) > 70
            ]
            return filtered
        return normalized_products
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []