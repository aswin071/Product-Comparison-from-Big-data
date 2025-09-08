import requests

def fetch_dummy_products(api_url="https://dummyjson.com/products"):
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        data = response.json()
        products = data.get("products", data)
        platforms = ['Amazon', 'Flipkart', 'eBay'] * (len(products) // 3 + 1)
        for i, product in enumerate(products):
            product['platform'] = platforms[i % len(platforms)]
        return products
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []