from harp.http import HttpResponse
import json

PRODUCTS = [
    {
        "id": 1,
        "name": "Ergonomic Chair",
        "price": 199.99,
        "category": "Furniture",
        "image": "/placeholder.svg?height=200&width=200",
    },
    {
        "id": 2,
        "name": "Mechanical Keyboard",
        "price": 129.99,
        "category": "Electronics",
        "image": "/placeholder.svg?height=200&width=200",
    },
    {
        "id": 3,
        "name": "Wireless Mouse",
        "price": 49.99,
        "category": "Electronics",
        "image": "/placeholder.svg?height=200&width=200",
    },
    {
        "id": 4,
        "name": "LED Desk Lamp",
        "price": 39.99,
        "category": "Lighting",
        "image": "/placeholder.svg?height=200&width=200",
    },
    {
        "id": 5,
        "name": "Noise-Cancelling Headphones",
        "price": 299.99,
        "category": "Audio",
        "image": "/placeholder.svg?height=200&width=200",
    },
    {
        "id": 6,
        "name": "Standing Desk",
        "price": 399.99,
        "category": "Furniture",
        "image": "/placeholder.svg?height=200&width=200",
    },
]

response = HttpResponse(json.dumps(PRODUCTS))
