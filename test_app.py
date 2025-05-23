import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"

class TestInventoryAPI(unittest.TestCase):
    def test_add_item(self):
        payload = {"name": "Test Product", "quantity": 5, "price": 2.99}
        response = requests.post(f"{BASE_URL}/inventory", json=payload)
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data["name"], "Test Product")
        self.assertEqual(data["quantity"], 5)
        self.assertEqual(data["price"], 2.99)

    def test_fetch_inventory(self):
        response = requests.get(f"{BASE_URL}/inventory")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

if __name__ == "__main__":
    unittest.main()