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