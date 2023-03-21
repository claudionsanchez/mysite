from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configurar la conexión a la base de datos
conexion = mysql.connector.connect(
  host="localhost",
  user="usuario",
  password="contraseña",
  database="basedatos"
)

# Definir la ruta para el formulario de pedidos
@app.route("/", methods=["GET", "POST"])
def formulario_pedido():
  if request.method == "POST":
    # Obtener los datos del formulario
    nombre_producto = request.form["nombre_producto"]
    cantidad = request.form["cantidad"]
    precio = request.form["precio"]
    nombre_cliente = request.form["nombre_cliente"]

    # Insertar los datos en la base de datos
    cursor = conexion.cursor()
    query = "INSERT INTO pedidos (nombre_producto, cantidad, precio, nombre_cliente) VALUES (%s, %s, %s, %s)"
    valores = (nombre_producto, cantidad, precio, nombre_cliente)
    cursor.execute(query, valores)
    conexion.commit()

    return "Pedido registrado correctamente"
  else:
    # Mostrar el formulario
    return render_template("formulario_pedido.html")

# Definir la ruta para la lista de pedidos
@app.route("/pedidos")
def lista_pedidos():
  # Obtener los pedidos de la base de datos
  cursor = conexion.cursor()
  query = "SELECT * FROM pedidos"
  cursor.execute(query)
  pedidos = cursor.fetchall()

  # Mostrar los pedidos en una tabla
  return render_template("lista_pedidos.html", pedidos=pedidos)

if __name__ == "__main__":
  app.run()