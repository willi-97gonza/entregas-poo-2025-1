"""WILLIAM DARIO GONZALEZ ROJAS - 12/04/2025 - mascotas.1 - JARVISCOLE97S@GMAIL.COM - El código simula el registro de tres mascotas (1 perro y 2 gatos), usando preguntas y respuestas predefinidas. Luego muestra un resumen en forma de tabla con su nombre, edad, raza y fecha de ingreso.

 """
from datetime import datetime

def obtener_pregunta(numero):
    preguntas = [
        "¿Cuántas mascotas va a ingresar?",
        "Mascota 1, ¿qué clase es (P)erro o (G)ato?",
        "¿Cuál es el nombre del Perro?",
        "¿Qué edad tiene 'Rocky'?",
        "¿De qué raza es 'Rocky'?",
        "Mascota 2, ¿qué clase es (P)erro o (G)ato?",
        "¿Cuál es el nombre del Gato (Michi)?",
        "¿Qué edad tiene 'Michi'?",
        "¿De qué raza es 'Michi'?",
        "Mascota 3, ¿qué clase es (P)erro o (G)ato?",
        "¿Cuál es el nombre del Gato (Nube)?",
        "¿Qué edad tiene 'Nube'?",
        "¿De qué raza es 'Nube'?"
    ]
    return preguntas[numero] if numero < len(preguntas) else "No hay más preguntas."

def obtener_respuesta(pregunta):
    respuestas = {
        "¿Cuántas mascotas va a ingresar?": "3",
        "Mascota 1, ¿qué clase es (P)erro o (G)ato?": "Perro",
        "¿Cuál es el nombre del Perro?": "Rocky",
        "¿Qué edad tiene 'Rocky'?": "4",
        "¿De qué raza es 'Rocky'?": "Labrador",
        "Mascota 2, ¿qué clase es (P)erro o (G)ato?": "Gato",
        "¿Cuál es el nombre del Gato (Michi)?": "Michi",
        "¿Qué edad tiene 'Michi'?": "6",
        "¿De qué raza es 'Michi'?": "Bengalí",
        "Mascota 3, ¿qué clase es (P)erro o (G)ato?": "Gato",
        "¿Cuál es el nombre del Gato (Nube)?": "Nube",
        "¿Qué edad tiene 'Nube'?": "1",
        "¿De qué raza es 'Nube'?": "Azul Ruso"
    }
    return respuestas.get(pregunta, "")

class Mascota:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = datetime.now().strftime("2025-03-30T22:53:45")

    def obtener_info(self):
        return [self.__class__.__name__, self.nombre, f"{self.edad} años", self.raza, self.fecha_ingreso]

class Perro(Mascota):
    pass

class Gato(Mascota):
    pass

def registrar_mascotas():
    mascotas = [
        Perro("Rocky", 4, "Labrador"),
        Gato("Michi", 6, "Bengalí"),
        Gato("Nube", 1, "Azul Ruso")
    ]
    return mascotas

def mostrar_mascotas(mascotas):
    print("Resumen:")
    print("|Clase |Nombre   |Edad   |Raza         |Fecha de ingreso          |")
    print("|------|---------|-------|-------------|--------------------------|")
    for mascota in mascotas:
        print(f"|{mascota.obtener_info()[0]:<6}|{mascota.obtener_info()[1]:<9}|{mascota.obtener_info()[2]:<7}|{mascota.obtener_info()[3]:<13}|{mascota.obtener_info()[4]:<26}|")

if __name__ == "__main__":
    numero_pregunta = 0
    while True:
        pregunta = obtener_pregunta(numero_pregunta)
        print(f"> {pregunta}")
        respuesta = obtener_respuesta(pregunta)
        if respuesta:
            print(f"< {respuesta}")
        numero_pregunta += 1
        if pregunta == "No hay más preguntas.":
            break
    print()
    mascotas = registrar_mascotas()
    mostrar_mascotas(mascotas)
