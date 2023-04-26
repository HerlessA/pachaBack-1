from flask import Flask, jsonify
import router

app = Flask(__name__)

@app.get("/")
def index():
    # users = [
    #     {
    #         "id": 1, 
    #         "name": "Juan"
    #     }, 
    #     {
    #         "id": 2, 
    #         "name": "Pedro"
    #     }
    # ]
    data = router.obtenerUsuario()
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=4000)
