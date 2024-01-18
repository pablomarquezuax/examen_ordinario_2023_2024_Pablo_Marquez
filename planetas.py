# Enumerado para la clasificación de planetas
from enum import Enum

class ClasificacionPlaneta(Enum):
    CONCORDIA = 1
    ILUM = 2
    KAMINO = 3

class Planeta:
    def __init__(self, nombre, volumen, clasificacion):
        self.nombre = nombre
        self.volumen = volumen
        self.clasificacion = clasificacion

class PlanetaConcordia(Planeta):
    def __init__(self):
        super().__init__("Concordia", 500, ClasificacionPlaneta.CONCORDIA)

class PlanetaIlum(Planeta):
    def __init__(self):
        super().__init__("Ilum", 1200, ClasificacionPlaneta.ILUM)

class PlanetaKamino(Planeta):
    def __init__(self):
        super().__init__("Kamino", 800, ClasificacionPlaneta.KAMINO)
