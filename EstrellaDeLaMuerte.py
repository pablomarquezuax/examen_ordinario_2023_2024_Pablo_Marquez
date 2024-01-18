from planetas import ClasificacionPlaneta

class EstrellaDeLaMuerte:
    def __init__(self):
        self.puntos_vida = 1000

    def destruir_planeta(self, planeta):
        if planeta.volumen <= self.puntos_vida:
            print(f"La Estrella de la Muerte ha destruido el planeta {planeta.nombre}.")
            self.puntos_vida -= planeta.clasificacion.value
        else:
            print(f"No se puede destruir el planeta {planeta.nombre}.")

if __name__ == "__main__":
    from planetas import PlanetaConcordia, PlanetaIlum, PlanetaKamino

    estrella_muerte = EstrellaDeLaMuerte()
    concordia = PlanetaConcordia()
    ilum = PlanetaIlum()
    kamino = PlanetaKamino()

    estrella_muerte.destruir_planeta(concordia)
    estrella_muerte.destruir_planeta(ilum)
    estrella_muerte.destruir_planeta(kamino)
