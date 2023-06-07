from flask import Flask, jsonify
import router

app = Flask(__name__)

@app.get("/api/usuario")
def index():
    data = router.obtenerUsuario()

    print("el tipo de datos es: ", type(data))
    return jsonify(data)

@app.delete("/api/eliminar/<id>")
def deleteUsuario(id):
    print('1',id)
    data = router.eliminaUsuario(id)
    print('2',id)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=4000)


## get: para obtener datos
## post: insert datos
## put: actualizar datos
## delete: eliminar datos