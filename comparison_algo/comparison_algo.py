# import requests
# import json

# def fetch_dummy_products(api_url="https://dummyjson.com/products"):
#     try:
#         response = requests.get(api_url, timeout=5)
#         response.raise_for_status()  # Check for HTTP errors
#         data = response.json()
        
#         # Handle DummyJSON structure
#         products = data.get("products", data)
#         platforms = ['Amazon', 'Flipkart', 'eBay'] * (len(products) // 3 + 1)
#         for i, product in enumerate(products):
#             product['platform'] = platforms[i % len(platforms)]
#         return products
#     except requests.RequestException as e:
#         print(f"Error fetching data: {e}")
#         return []

# def basic_compare(products):
#     available = [p for p in products if p.get('stock', 0) > 0]
#     if not available:
#         return None
#     sorted_products = sorted(available, key=lambda p: p['price'])
#     return sorted_products[0]

# def display_product(product):
#     if product:
#         print(f"Best Product:")
#         print(f"Platform: {product.get('platform', 'N/A')}")
#         print(f"Name: {product.get('title', 'N/A')}")
#         print(f"Price: ${product.get('price', 'N/A')}")
#         print(f"Rating: {product.get('rating', 'N/A')}/5")
#         print(f"Stock: {product.get('stock', 'N/A')}")
#     else:
#         print("No available products found.")

# if __name__ == "__main__":
#     products = fetch_dummy_products()
#     if products:
#         best = basic_compare(products)
#         display_product(best)
#     else:
#         print("Failed to fetch products.")



import math

def sort_by_price(products):
    """
    Efficiently sorts products by price (min to max) for MVP.
    - Filters available products (stock > 0).
    - Handles missing prices by treating as worst-case (inf).
    - Uses stable Timsort for accuracy on ties.
    """
    # Filter available
    available = [p for p in products if p.get('stock', 0) > 0]
    if not available:
        return []
    
    # Sort by price ascending, handling missing as inf
    sorted_products = sorted(
        available,
        key=lambda p: p.get('price', math.inf)
    )
    return sorted_products