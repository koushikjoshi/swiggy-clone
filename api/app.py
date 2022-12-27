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