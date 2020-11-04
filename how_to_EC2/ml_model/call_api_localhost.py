import requests

#result = requests.post("http://localhost:5000/", params = {"x1": 3, "x2": 5})
FEATURES = {'sepal length (cm)': 5.2,
            'sepal width (cm)': 4.9,
            'petal length (cm)': 1.9,
            'petal width (cm)': 2.1}

result = requests.post("http://localhost:5000/", params = FEATURES)
print(result.json())
