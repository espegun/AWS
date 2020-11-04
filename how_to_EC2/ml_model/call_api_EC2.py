import requests



FEATURES = {'sepal length (cm)': 5.2,
            'sepal width (cm)': 4.9,
            'petal length (cm)': 1.9,
            'petal width (cm)': 2.1}

result = requests.post("http://54.216.85.67:5000/", params = FEATURES)
print(result.json())

