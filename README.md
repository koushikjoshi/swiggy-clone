# Food Delivery App

Welcome to the Food Delivery App! This app allows users to browse restaurants, view their menus, and place orders for pickup or delivery.

## Android app

Coming Soon!

## Flask App

The Flask app is the backend for the food delivery app, providing a RESTful API for the Android app to interact with. It is written in Python and uses the Flask framework.

### Endpoints

The Flask app has the following endpoints:

#### 1. GET /restaurants

Returns a list of all the restaurants available on the app.

##### Request:

```
curl -X GET http://localhost:5000/restaurants
```

##### Response:

```
HTTP 200 OK
Content-Type: application/json

[
    {
        "id": 1,
        "name": "Pizza Palace",
        "location": "123 Main Street",
        "image_url": "https://www.example.com/pizza-palace.jpg",
        "menu": [
            {
                "id": 1,
                "name": "Pepperoni Pizza",
                "price": 12.99,
                "image_url": "https://www.example.com/pepperoni-pizza.jpg"
            },
            # ...
        ]
    },
    # ...
]

```

#### 2. GET /restaurants/<restaurant_id>

Returns the details for a single restaurant.

##### Request:

```
curl -X GET http://localhost:5000/restaurants/1

```

##### Response:

```
HTTP 200 OK
Content-Type: application/json

{
    "id": 1,
    "image_url": "https://www.example.com/pizza-palace.jpg",
    "location": "123 Main Street",
    "menu": [
        {
            "id": 1,
            "image_url": "https://www.example.com/pepperoni-pizza.jpg",
            "name": "Pepperoni Pizza",
            "price": 12.99
        },
        {
            "id": 2,
            "image_url": "https://www.example.com/margherita-pizza.jpg",
            "name": "Margherita Pizza",
            "price": 11.99
        },
        {
            "id": 3,
            "image_url": "https://www.example.com/bbq-chicken-pizza.jpg",
            "name": "BBQ Chicken Pizza",
            "price": 13.99
        }
    ],
    "name": "Pizza Palace"
}

```

#### 3. POST /orders

Places a new order.

##### Request

```
{
    "restaurant_id": 1,
    "menu_items": [
        {
            "id": 1,
            "quantity": 2
        },
        {
            "id": 2,
            "quantity": 1
        }
    ],
    "pickup": true,
    "location_id": 1,
    "status": "pending"
}

```

##### Response

```
{
    "restaurant_id": 1,
    "menu_items": [
        {
            "id": 1,
            "quantity": 2
        },
        {
            "id": 2,
            "quantity": 1
        }
    ],
    "pickup": true,
    "location_id": 1,
    "status": "pending"
}

```

#### 5. GET /orders/<order_id>

Returns the details for a single order.

##### Request

```
curl -X GET http://localhost:5000/orders/1
```

##### Response

```
HTTP 200 OK
Content-Type: application/json

{
    "id": 1,
    "restaurant_id": 1,
    "items": [
        {
            "id": 1,
            "name": "Pepperoni Pizza",
            "price": 12.99,
            "quantity": 2,
            "subtotal": 25.98
        },
        {
            "id": 2,
            "name": "Margherita Pizza",
            "price": 11.99,
            "quantity": 1,
            "subtotal": 11.99
        }
    ],
    "total": 37.97,
    "pickup": true
}
```
