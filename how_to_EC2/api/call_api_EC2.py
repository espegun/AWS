import requests

result = requests.post("http://54.216.85.67:5000/", params = {"x1": 3, "x2": 5})
print(result.json())
