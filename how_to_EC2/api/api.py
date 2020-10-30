import flask
app = flask.Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def predict():
    data = {"success": False}
    
    params = flask.request.json
    if params is None:
        params = flask.request.args
    
    print("params")
    print(params)
        
    if "x1" in params.keys() and "x2" in params.keys():
        
                       
        data["response"] = float(params.get("x1")) + float(params.get("x2"))
        data["success"] = True
       
    return flask.jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    
