import requests

result = requests.post("http://localhost:5000/", params = {"x1": 3, "x2": 5})
print(result.json())
