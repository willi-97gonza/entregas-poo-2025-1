class Inventario:
    def __init__(self):
        """Inicializa el inventario con algunos productos predefinidos."""
        self.productos = {
            "arroz": (2000, 20),
            "leche": (3100, 24),
            "pan": (5600, 17)
        }

    def mostrar_productos(self):
        """Muestra la lista de productos disponibles."""
        print(", ".join(self.productos.keys()))

    def mostrar_info(self, tipo):
        """Muestra la cantidad o el precio de cada producto."""
        if tipo not in ["cantidad", "precio"]:
            print("Comando no reconocido.")
            return

        for producto, (precio, cantidad) in self.productos.items():
            valor = precio if tipo == "precio" else cantidad
            unidad = "pesos" if tipo == "precio" else "unidades"
            print(f"{producto}: {valor} {unidad}")

    def mostrar_inventario(self):
        """Muestra el inventario en formato de tabla."""
        print("\nResumen del Inventario:")
        print("| Productos | Cantidad | Precio  |")
        print("|-----------|---------|--------|")
        for producto, (precio, cantidad) in self.productos.items():
            print(f"| {producto:<9} | {cantidad} unidades | {precio} pesos |")

    def iniciar(self):
        """Inicia el bucle de consulta del usuario."""
        while True:
            consulta = input("\n¿Qué productos, precios o catidad de productos quieres cunsultar? (productos, cantidad, precio, salir): ").lower()
            if consulta == "productos":
                self.mostrar_productos()
            elif consulta in ["cantidad", "precio"]:
                self.mostrar_info(consulta)
            elif consulta == "salir":
                break
            else:
                print("Comando no reconocido.")

        self.mostrar_inventario()


# Punto de entrada del programa
if __name__ == "__main__":
    inventario = Inventario()
    inventario.iniciar()
