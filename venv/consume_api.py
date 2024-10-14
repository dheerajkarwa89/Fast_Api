import requests

# The API URL (FastAPI default is http://127.0.0.1:8000)
url = "http://127.0.0.1:8000/sample/5"

# Optional query parameters
params = {"q": "search"}

# Make a GET request to the API
response = requests.get(url, params=params)

# Print the JSON response
print(response.json())