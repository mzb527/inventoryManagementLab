# Inventory Management System

## Overview
This is a **Flask-based REST API** for inventory management. It allows users to **add, edit, view, and delete** inventory items, while fetching real-time product details from the OpenFoodFacts API.

## Prerequisites
Before running the project, ensure you have:
- Python 3 installed
- Flask and requests libraries
- Git (optional, for version control)

## Installation
Follow these steps to set up the project:

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd inventory-management
2.   - Install Dependencies Run the following command to install required libraries:
pip install -r requirements.txt
Running the API
To start the Flask server, run:
python app.py

The API will start at http://127.0.0.1:5000/.
API Endpoints
Use the following endpoints to interact with the inventory:
- GET /inventory → Fetch all items
- GET /inventory/<id> → Fetch a single item
- POST /inventory → Add a new item
- PATCH /inventory/<id> → Update an item
- DELETE /inventory/<id> → Remove an item
Using the CLI
A command-line interface (cli.py) is available for inventory management.

Start CLI Interaction:
python cli.py


You can then:
- View inventory
- Add new items
- Update existing items
- Delete items
Follow the prompts within the CLI to manage inventory.
Fetching Product Data
The system integrates with OpenFoodFacts API to fetch product details by barcode. If a barcode is provided when adding an item, the system automatically retrieves additional information.
