from flask import Flask, jsonify, request

app = Flask(__name__)

def sumar(a, b):
    return a + b

@app.route("/api/suma", methods=["GET"])
def api_suma():
    try:
        a = int(request.args.get("a"))
        b = int(request.args.get("b"))
        resultado = sumar(a, b)
        return jsonify({"resultado": resultado})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)