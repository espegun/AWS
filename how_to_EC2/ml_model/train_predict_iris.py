import numpy as np
from sklearn import datasets, svm
import pickle

PICKLE_FILE = "model.pkl"

#target_names = datasets.load_iris().target_names
#print(target_names)

def train_model():

    X, y = datasets.load_iris(return_X_y=True)
    model = svm.SVC().fit(X, y)

    return model


def save_model(model, filename):

    with open(filename, "wb") as f:
        pickle.dump(model, f)

    print(f"Model saved to {filename}.")


def load_model(filename):

    with open(filename, "rb") as f:
        model = pickle.load(f)

    print(f"Model loaded from {filename}.")

    return model


def make_prediction(features):

    model = load_model(PICKLE_FILE)
    return actual_prediction(model, features)


def actual_prediction(model, features):

    REQUIRED_FEATURES = ['sepal length (cm)',
                         'sepal width (cm)',
                         'petal length (cm)',
                         'petal width (cm)']
    TARGET_NAMES = ['setosa', 'versicolor', 'virginica']

    if len(REQUIRED_FEATURES) != len(features):
        raise ValueError(f"Number of features is not {len(REQUIRED_FEATURES)}.")

    for req_feat in REQUIRED_FEATURES:
        if not req_feat in features:
            raise ValueError(f"Missing feature {req_feature} in arguments.")

    X = np.array([[float(features[REQUIRED_FEATURES[0]]),
                   float(features[REQUIRED_FEATURES[1]]),
                   float(features[REQUIRED_FEATURES[2]]),
                   float(features[REQUIRED_FEATURES[3]])]])

    pred_raw = model.predict(X)[0]
    pred_name = TARGET_NAMES[pred_raw]

    return pred_name


if __name__ == "__main__":

    model = train_model()
    save_model(model, PICKLE_FILE)

    PREDICT = False
    if PREDICT:
        FEATURES = {'sepal length (cm)': 5.2,
                    'sepal width (cm)': 4.9,
                    'petal length (cm)': 1.9,
                    'petal width (cm)': 2.1}
        model = load_model(PICKLE_FILE)
        pred = actual_prediction(model, FEATURES)
        print(pred)

    print("That was fun.")
