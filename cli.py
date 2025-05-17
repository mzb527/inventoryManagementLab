import requests

BASE_URL = "http://127.0.0.1:5000"

def list_inventory():
    response = requests.get(f"{BASE_URL}/inventory")
    print(response.json())

def add_item():
    name = input("Enter product name: ")
    barcode = input("Enter barcode (optional): ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    payload = {"name": name, "barcode": barcode, "quantity": quantity, "price": price}
    response = requests.post(f"{BASE_URL}/inventory", json=payload)
    print(response.json())

def update_item():
    item_id = int(input("Enter item ID to update: "))
    key = input("Enter field to update (name, quantity, price): ")
    value = input("Enter new value: ")

    payload = {key: value}
    response = requests.patch(f"{BASE_URL}/inventory/{item_id}", json=payload)
    print(response.json())

def delete_item():
    item_id = int(input("Enter item ID to delete: "))
    response = requests.delete(f"{BASE_URL}/inventory/{item_id}")
    print(response.text)

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