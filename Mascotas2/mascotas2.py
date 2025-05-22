"""
Título de práctica:  Mascotas2

Extensión del sistema de registro de mascotas con visualización de resumen usando herencia múltiple.

Autor: William Dario Gonzalez Rojas <jarviscole97s@gmail.com>
Fecha: 2025-05-21
"""

import datetime
from typing import List, Union

class Visualizador:
    """
    Clase base encargada de la visualización de objetos.
    Contiene el método resumen, que devuelve una representación formateada del objeto.
    """

    def resumen(self) -> str:
        """
        Genera un resumen en formato de tabla de la mascota.
        """
        return f"|{self.__class__.__bases__[0].__name__:5} |{self.nombre:8} |{self.edad} años |{self.raza.title():13} |{self.fecha_ingreso.isoformat():25} |"


class Mascota:
    """
    Clase base que representa una mascota dentro del sistema de la veterinaria.
    """

    def __init__(self, nombre: str, edad: int, raza: str):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = datetime.datetime.now()
    
    def obtener_tipo(self) -> str:
        """Devuelve el tipo de mascota, basado en el nombre de la clase."""
        return self.__class__.__name__


class Perro(Mascota, Visualizador):
    """Clase que representa un perro, con funcionalidad para visualización.""" 
    pass


class Gato(Mascota, Visualizador):
    """Clase que representa un gato, con funcionalidad para visualización.""" 
    pass


def ingresar_mascota(numero: int) -> Union[Perro, Gato]:
    while True:
        tipo = input(f"> Mascota {numero}, ¿qué clase es (P)erro o (G)ato?\n< ").strip().lower()
        if tipo in ['perro', 'p']:
            clase = Perro
            tipo_str = "Perro"
            break
        elif tipo in
