from flask import Flask, jsonify
import router

app = Flask(__name__)


# get, post, put, delete


@app.get("/api/usuario")  # @app.get("/")
def index():
    # return "Hola mundo! 2"
    # users = [{"id": 1, "name": "Mari"}, {"id": 2, "name": "Jul"}]
    # return users
    data = router.obtenerUsuario()
    print("El tipo de dato es: ", type(data))
    return jsonify(data)


@app.delete("/api/eliminar/<id>")
def deleteUsuario(id):
    print("1", id)
    data = router.eliminarUsuario(id)
    print("2", id)
    return jsonify(data)


@app.post("/api/usuario")
def postUsuario(name, email):
    data = router.crearUsuario(name, email)
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=4000)


# DB

# CREATE TABLE IF NOT EXISTS usuario(
# 	id serial primary key,
#     nombre varchar(100) not null,
# 	correo varchar(100) not null
# );

# SELECT * FROM usuario;

# INSERT INTO usuario(nombre, correo)
# VALUES('Mari22', 'mari22@abc.com');
