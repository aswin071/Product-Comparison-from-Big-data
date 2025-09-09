from fastapi import FastAPI
from comparison_algo.fetch_data import fetch_dummy_products
from comparison_algo.comparison_algo import sort_by_price

app = FastAPI(title="Price Comparison API")

@app.get("/products")
async def get_products():
    products = fetch_dummy_products()
    if not products:
        return {"error": "Failed to fetch products"}
    return {"products": products}

@app.get("/compare")
async def compare_products():
    products = fetch_dummy_products()
    if not products:
        return {"error": "No products available"}
    sorted_products = sort_by_price(products)
    if not sorted_products:
        return {"error": "No available products to compare"}
    best = sorted_products[0]  # Take cheapest product
    return {
        "best_product": {
            "platform": best.get("platform", "N/A"),
            "name": best.get("title", "N/A"),
            "price": best.get("price", "N/A"),
            "rating": best.get("rating", "N/A"),
            "stock": best.get("stock", "N/A")
        }
    }

@app.get("/search")
async def search_products(query: str):
    products = fetch_dummy_products(query=query)
    if not products:
        return {"error": f"No products found for query: {query}"}
    sorted_products = sort_by_price(products)
    if not sorted_products:
        return {"error": f"No available products found for query: {query}"}
    return {
        "query": query,
        "results": [
            {
                "platform": p.get("platform", "N/A"),
                "name": p.get("title", "N/A"),
                "price": p.get("price", "N/A"),
                "rating": p.get("rating", "N/A"),
                "stock": p.get("stock", "N/A"),
                "category" :p.get("category", "N/A"),
                "description" : p.get("description", "N/A"),
                "images":p.get("images", "N/A"),

            }
            for p in sorted_products
        ]
    }