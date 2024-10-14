import requests

# The API URL (FastAPI default is http://127.0.0.1:8000)
url = "http://127.0.0.1:8000/items/1"

# Optional query parameters
params = {"q": "search"}

# Make a GET request to the API
#response = requests.get(url, params=params)

# Data to update the item
updated_item = {
    "name": "Updated Item",
    "price": 99.99,
    "description": "Updated description"   
}

# Make a PUT request to the API
response = requests.put(url, json=updated_item)

# Print the JSON response
print(response.json())