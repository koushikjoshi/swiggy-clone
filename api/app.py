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