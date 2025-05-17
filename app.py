from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

inventory = []  # Mock database

# Fetch product details from OpenFoodFacts API
def fetch_product_details(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    response = requests.get(url)
    data = response.json()
    if data.get("status") == 1:
        product = data.get("product", {})
        return {
            "name": product.get("product_name", "Unknown"),
            "brand": product.get("brands", "Unknown"),
            "ingredients": product.get("ingredients_text", "Unknown")
        }
    return None

# CRUD Routes
@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory)

@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((i for i in inventory if i["id"] == item_id), None)
    return jsonify(item) if item else ("Item not found", 404)

@app.route('/inventory', methods=['POST'])
def add_item():
    data = request.json
    barcode = data.get("barcode")
    product_details = fetch_product_details(barcode) if barcode else {}

    new_item = {
        "id": len(inventory) + 1,
        "name": data.get("name", product_details.get("name", "Unknown")),
        "brand": data.get("brand", product_details.get("brand", "Unknown")),
        "ingredients": data.get("ingredients", product_details.get("ingredients", "Unknown")),
        "quantity": data.get("quantity", 0),
        "price": data.get("price", 0.0)
    }
    inventory.append(new_item)
    return jsonify(new_item), 201

@app.route('/inventory/<int:item_id>', methods=['PATCH'])
def update_item(item_id):
    item = next((i for i in inventory if i["id"] == item_id), None)
    if not item:
        return "Item not found", 404
    
    data = request.json
    item.update({key: data[key] for key in data if key in item})
    return jsonify(item)

@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global inventory
    inventory = [i for i in inventory if i["id"] != item_id]
    return "Item deleted", 200

if __name__ == '__main__':
    app.run(debug=True)