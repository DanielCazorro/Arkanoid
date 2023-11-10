import os
import pygame as pg
from . import ALTO, ANCHO
from .escenas import Portada, Partida, MejoresJugadores

# Clase Arkanoid
class Arkanoid:
    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))
        pg.display.set_caption("Arkanoid BZ Version")

        # Cargar icono
        ruta_icono = os.path.join("resources", "images", "icon.png")
        icono = pg.image.load(ruta_icono)
        pg.display.set_icon(icono)

        # Crear instancias de las escenas
        objeto_portada = Portada(self.pantalla)
        objeto_partida = Partida(self.pantalla)
        objeto_mejores = MejoresJugadores(self.pantalla)

        # Lista de escenas
        self.escenas = [objeto_portada, objeto_partida, objeto_mejores]

    def jugar(self):
        """Este es el bucle principal"""
        for escena in self.escenas:
            he_acabado = escena.bucle_principal()
            if he_acabado:
                # return
                break
        pg.quit()

# Ejecutar el juego si este archivo es el punto de entrada
if __name__ == "__main__":
    arkanoid = Arkanoid()
    arkanoid.jugar()
