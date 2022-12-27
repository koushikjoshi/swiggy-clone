from flask import Flask, jsonify, request
from data import restaurants, locations

app = Flask(__name__)

# List to store orders
orders = []

# Endpoints

@app.route("/api/restaurants", methods=["GET"])
def get_restaurants():
    """Returns a list of restaurants"""
    return jsonify(restaurants)

@app.route("/api/restaurants/<int:restaurant_id>", methods=["GET"])
def get_restaurant(restaurant_id):
    """Returns a specific restaurant"""
    for restaurant in restaurants:
        if restaurant["id"] == restaurant_id:
            return jsonify(restaurant)
    return jsonify({"error": "Restaurant not found"}), 404

@app.route("/api/restaurants/<int:restaurant_id>/menu", methods=["GET"])
def get_menu(restaurant_id):
    """Returns the menu for a specific restaurant"""
    for restaurant in restaurants:
        if restaurant["id"] == restaurant_id:
            return jsonify(restaurant["menu"])
    return jsonify({"error": "Restaurant not found"}), 404

@app.route("/api/locations", methods=["GET"])
def get_locations():
    """Returns a list of locations"""
    return jsonify(locations)

@app.route("/api/orders", methods=["POST"])
def place_order():
    """Places a new order"""
    data = request.get_json()
    restaurant_id = data["restaurant_id"]
    menu_items = data["menu_items"]
    location_id = data["location_id"]

    # Validate input
    if not all(field in data for field in ["restaurant_id", "menu_items", "location_id"]):
        return jsonify({"error": "Invalid input"}), 422

    for restaurant in restaurants:
        if restaurant["id"] == restaurant_id:
            for menu_item in menu_items:
                if not any(item["id"] == menu_item["id"] for item in restaurant["menu"]):
                    return jsonify({"error": "Invalid menu item"}), 422
            break
    else:
        return jsonify({"error": "Invalid restaurant"}), 422

    for location in locations:
        if location["id"] == location_id:
            break
    else:
        return jsonify({"error": "Invalid location"}), 422

    # Place order
    order = {
        "id": len(orders) + 1,
        "restaurant_id": restaurant_id,
        "menu_items": menu_items,
        "location_id": location_id,
        "status": "pending"
    }
    orders.append(order)
    return jsonify(order)

@app.route("/api/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):
    """Returns a specific order"""
    for order in orders:
        if order["id"] == order_id:
            return jsonify(order)
    return jsonify({"error": "Order not found"}), 404