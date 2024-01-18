from planetas import ClasificacionPlaneta, PlanetaConcordia, PlanetaIlum, PlanetaKamino

class EstrellaDeLaMuerte:
    def __init__(self):
        self.puntos_vida = 1000
        self.naves_aliadas = []

    def destruir_planeta(self, planeta):
        if planeta.volumen <= self.puntos_vida:
            print(f"La Estrella de la Muerte ha destruido el planeta {planeta.nombre}.")
            self.puntos_vida -= planeta.clasificacion.value
        else:
            print(f"No se puede destruir el planeta {planeta.nombre}.")

    def agregar_nave_aliada(self, nave):
        self.naves_aliadas.append(nave)

    def atacar_nave_aliada(self, nave):
        if nave.puntos_vida <= self.puntos_vida:
            print(f"La Estrella de la Muerte ha destruido la nave aliada {nave.nombre}.")
            self.puntos_vida -= nave.puntos_vida
            self.naves_aliadas.remove(nave)
        else:
            print(f"No se puede destruir la nave aliada {nave.nombre}.")

if __name__ == "__main__":
    from Naves import NavePequena, NaveGrande

    estrella_muerte = EstrellaDeLaMuerte()
    nave_pequena = NavePequena("Nave Pequeña", 200)
    nave_grande = NaveGrande("Nave Grande", 500)

    estrella_muerte.agregar_nave_aliada(nave_pequena)
    estrella_muerte.agregar_nave_aliada(nave_grande)

    estrella_muerte.destruir_planeta(PlanetaConcordia())
    estrella_muerte.destruir_planeta(PlanetaIlum())
    estrella_muerte.destruir_planeta(PlanetaKamino())

    estrella_muerte.atacar_nave_aliada(nave_pequena)
    estrella_muerte.atacar_nave_aliada(nave_grande)
