import requests

BASE_URL = "http://127.0.0.1:5000"

def list_inventory():
    try:
        response = requests.get(f"{BASE_URL}/inventory")
        response.raise_for_status()
        items = response.json()
        if not items:
            print("Inventory is empty.")
        else:
            for item in items:
                print(f"ID: {item['id']}, Name: {item['name']}, Brand: {item.get('brand', '')}, "
                      f"Qty: {item['quantity']}, Price: {item['price']}")
    except Exception as e:
        print(f"Error: {e}")

def add_item():
    name = input("Enter product name: ")
    barcode = input("Enter barcode (optional): ")
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
    except ValueError:
        print("Invalid quantity or price.")
        return

    payload = {"name": name, "barcode": barcode, "quantity": quantity, "price": price}
    try:
        response = requests.post(f"{BASE_URL}/inventory", json=payload)
        response.raise_for_status()
        print("Added:", response.json())
    except Exception as e:
        print(f"Error: {e}")

def update_item():
    try:
        item_id = int(input("Enter item ID to update: "))
        key = input("Enter field to update (name, brand, ingredients, quantity, price): ")
        value = input("Enter new value: ")
        if key in ["quantity"]:
            value = int(value)
        elif key in ["price"]:
            value = float(value)
        payload = {key: value}
        response = requests.patch(f"{BASE_URL}/inventory/{item_id}", json=payload)
        response.raise_for_status()
        print("Updated:", response.json())
    except Exception as e:
        print(f"Error: {e}")

def delete_item():
    try:
        item_id = int(input("Enter item ID to delete: "))
        response = requests.delete(f"{BASE_URL}/inventory/{item_id}")
        response.raise_for_status()
        print(response.text)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        print("\n1. View Inventory\n2. Add Item\n3. Update Item\n4. Delete Item\n5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            list_inventory()
        elif choice == "2":
            add_item()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            break