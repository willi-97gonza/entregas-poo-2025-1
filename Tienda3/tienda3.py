"""WILLIAM DARIO GONZALEZ ROJAS - jarviscole97s@gmail.com - 14/03/2025"""
# Definimos la clase Inventario para manejar los productos
class Inventario:
    def __init__(self):
        # Aquí guardamos los productos en un diccionario con su precio y cantidad
        self.productos = {
            "arroz": (2000, 20),
            "leche": (3100, 24),
            "pan": (5600, 17)
        }

    # Función para mostrar solo los nombres de los productos
    def mostrar_productos(self):
        print(", ".join(self.productos.keys()))

    # Función para mostrar la cantidad o el precio de cada producto
    def mostrar_info(self, tipo):
        if tipo not in ["cantidad", "precio"]:
            print("Comando no reconocido.")
            return

        # Recorremos los productos y mostramos la info según lo que pidan
        for producto, (precio, cantidad) in self.productos.items():
            valor = precio if tipo == "precio" else cantidad
            unidad = "pesos" if tipo == "precio" else "unidades"
            print(f"{producto}: {valor} {unidad}")

    # Función para mostrar el inventario en forma de tabla
    def mostrar_inventario(self):
        print("\nResumen del Inventario:")
        print("| Productos  | Cantidad   | Precio   |")
        print("|-----------|------------|----------|")
        for producto, (precio, cantidad) in self.productos.items():
            print(f"| {producto:<9} | {cantidad} unidades | {precio} pesos |")

    # Esta función hace que el usuario pueda interactuar con el inventario
    def iniciar(self):
        while True:
            # Preguntamos al usuario qué quiere consultar
            consulta = input("\n¿Qué productos, precios o cantidad de productos quieres consultar? (productos, cantidad, precio, salir): ").lower()
            if consulta == "productos":
                self.mostrar_productos()
            elif consulta in ["cantidad", "precio"]:
                self.mostrar_info(consulta)
            elif consulta == "salir":
                break
            else:
                print("Comando no reconocido.")

        # Al final mostramos el inventario completo
        self.mostrar_inventario()


# Si ejecutamos este archivo directamente, iniciamos el programa
if __name__ == "__main__":
    inventario = Inventario()
    inventario.iniciar()


# Definimos la clase Producto para guardar la información de cada producto
class Producto:
    def __init__(self, nombre, precio, cantidad, descripcion, clasificacion):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.clasificacion = clasificacion

    # Función para calcular el precio total del inventario de este producto
    def inventario_precio(self):
        return self.precio * self.cantidad

    # Función para calcular el precio de cierta cantidad del producto
    def calcula_precio(self, cantidad):
        return self.precio * cantidad


# Creamos una lista con productos predefinidos
productos = [
    Producto("arroz", 2000, 20, "arroz diana", "alimentos"),
    Producto("leche", 3100, 24, "leche alpina entera", "alimentos"),
    Producto("pan", 5600, 17, "pan tajado comapan premium", "alimentos")
]

# Mostramos cuántos productos hay en total en el inventario
print(f"Hay un total de {len(productos)} productos en el inventario.")

# Bucle para preguntar al usuario sobre los productos
while True:
    consulta = input("¿Sobre qué producto deseas información? (producto 1, producto 2, producto 3, salir): ").lower()

    if consulta == "producto 1":
        producto = productos[0]
    elif consulta == "producto 2":
        producto = productos[1]
    elif consulta == "producto 3":
        producto = productos[2]
    elif consulta == "salir":
        break
    else:
        print("Comando no reconocido.")
        continue

    # Mostramos la información detallada del producto que escogió el usuario
    print(f"El producto seleccionado es: {producto.nombre}")
    print(f"Su precio es: {producto.precio} pesos")
    print(f"Cantidad disponible: {producto.cantidad} unidades")
    print(f"Descripción: {producto.descripcion}")

# Función para mostrar un resumen de los productos en forma de tabla
def mostrar_inventario():
    print("\n> Resumen:")
    print("|Producto    |Cantidad      |Precio       |Descripción          |Clasificación |")
    print("|-----------|-------------|-------------|---------------------|--------------|")
    for producto in productos:
        print(f"|{producto.nombre:<12} |{producto.cantidad:<11} unidades |{producto.precio:<10} pesos |{producto.descripcion[:18]:<18}...|{producto.clasificacion:<14} |")

# Diccionario para almacenar el total de precios por clasificación
precios_por_clasificacion = {}
for producto in productos:
    if producto.clasificacion in precios_por_clasificacion:
        precios_por_clasificacion[producto.clasificacion] += producto.inventario_precio()
    else:
        precios_por_clasificacion[producto.clasificacion] = producto.inventario_precio()

# Mostramos el total de precios por clasificación en forma de tabla
print("\n> Precios por clasificación:")
print("|Clasificación  |Precio Total        |")
print("|---------------|--------------------|")
for clasificacion, precio_total in precios_por_clasificacion.items():
    print(f"|{clasificacion:<14} |{precio_total:<14} pesos|")
