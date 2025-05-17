import requests

def fetch_product_details(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        if data.get("status") == 1:
            product = data.get("product", {})
            return {
                "name": product.get("product_name", "Unknown"),
                "brand": product.get("brands", "Unknown"),
                "ingredients": product.get("ingredients_text", "Unknown")
            }
    except Exception as e:
        print(f"Error fetching product details: {e}")
    return None