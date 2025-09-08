from fastapi import FastAPI
from comparison_algo.fetch_data import fetch_dummy_products
from comparison_algo.comparison_algo import basic_compare

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
    best = basic_compare(products)
    if not best:
        return {"error": "No available products to compare"}
    return {
        "best_product": {
            "platform": best.get("platform", "N/A"),
            "name": best.get("title", "N/A"),
            "price": best.get("price", "N/A"),
            "rating": best.get("rating", "N/A"),
            "stock": best.get("stock", "N/A")
        }
    }