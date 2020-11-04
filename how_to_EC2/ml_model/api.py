import flask
app = flask.Flask(__name__)
from train_predict_iris import make_prediction

@app.route("/", methods=["GET", "POST"])
def predict():
    data = {"success": False}
    
    params = flask.request.json
    if params is None:
        params = flask.request.args
    
    print("params")
    print(params)
        
    if len(params) == 4:

        pred = make_prediction(params)
        data["response"] = pred
        data["success"] = True
    else:
        raise ValueError("Number of arguments is not 4.")

    print(data)

    return flask.jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
