def validate_inventory_item(data):
    """Validates required fields before adding/updating inventory."""
    required_fields = ["name", "quantity", "price"]
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        return False, f"Missing fields: {', '.join(missing_fields)}"
    
    if not isinstance(data.get("quantity"), int) or data["quantity"] < 0:
        return False, "Quantity must be a positive integer."
    
    if not isinstance(data.get("price"), (int, float)) or data["price"] < 0:
        return False, "Price must be a positive number."
    
    return True, "Valid data."

def format_currency(amount):
    """Formats a numeric value into currency format."""
    return f"${amount:.2f}"

def find_item_by_id(inventory, item_id):
    """Finds an item by ID from inventory."""
    return next((item for item in inventory if item["id"] == item_id), None)