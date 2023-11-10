import os
import pygame as pg
from . import ALTO, ANCHO, FPS
from .entidades import Ladrillo, Pelota, Raqueta

# Clase Escena
class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        """
        Este método debe ser implementado por cada una de las escenas,
        en función de lo que estén esperando hasta la condición de salida.
        """
        pass

# Clase Portada
class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        ruta = os.path.join("resources", "images", "arkanoid_name.png")
        self.logo = pg.image.load(ruta)
        ruta_tipo = os.path.join("resources", "fonts", "CabinSketch-Bold.ttf")
        self.tipografia = pg.font.Font(ruta_tipo, 28)

    def bucle_principal(self):
        """
        Devuelve True si hay que finalizar el programa
        Devuelve False si hay que pasar a la siguiente escena
        """
        super().bucle_principal()
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    salir = True
            self.pantalla.fill((99, 0, 0))
            self.pintar_logo()
            self.pintar_texto()
            pg.display.flip()
        return False

    def pintar_logo(self):
        ancho_logo = self.logo.get_width()
        pos_x = (ANCHO - ancho_logo) / 2
        pos_y = ALTO/3
        self.pantalla.blit(self.logo, (pos_x, pos_y))

    def pintar_texto(self):
        mensaje = "Pulsa <espacio> para comenzar la partida"
        texto = self.tipografia.render(mensaje, True, (255, 255, 255))
        pos_x = ANCHO/2 - texto.get_width()/2
        pos_y = ALTO * 3 / 4
        self.pantalla.blit(texto, (pos_x, pos_y))

class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        ruta = os.path.join("resources", "images", "background.jpg")
        self.fondo = pg.image.load(ruta)
        self.jugador = Raqueta()
        self.pelota = Pelota(self.jugador.rect.midtop)
        # Guardar la posición inicial
        self.pelota.posicion_inicial = self.jugador.rect.midtop
        self.crear_muro()
        self.puntuacion = 0

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        partida_iniciada = False
        while not salir:
            self.reloj.tick(FPS)
            for event in pg.event.get():


                if event.type == pg.QUIT:
                    return True
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    partida_iniciada = not partida_iniciada  # Invertir el estado del juego
                    if partida_iniciada:
                        self.pelota.en_movimiento = True  # Permitir que la pelota se mueva nuevamente

            self.pintar_fondo()
            self.jugador.update()
            self.pantalla.blit(self.jugador.image, self.jugador.rect)

            self.pelota.update(self.jugador, partida_iniciada)
            self.pantalla.blit(self.pelota.image, self.pelota.rect)

            self.pelota.hay_colision(self.jugador)
            golpeados = pg.sprite.spritecollide(
                self.pelota,
                self.ladrillos,
                True
            )
            if len(golpeados) > 0:
                self.pelota.velocidad_y = -self.pelota.velocidad_y
                # Incrementar la puntuación por cada bloque roto
                self.puntuacion += len(golpeados)

            self.ladrillos.draw(self.pantalla)
            self.mostrar_puntuacion()

            pg.display.flip()
        return False
    
    def mostrar_puntuacion(self):
        font = pg.font.Font(None, 36)
        texto = font.render(f"Puntuación: {self.puntuacion}", True, (255, 255, 255))
        self.pantalla.blit(texto, (10, ALTO - 40))

    def pintar_fondo(self):
        self.pantalla.fill((0, 0, 99))
        self.pantalla.blit(self.fondo, (0, 0))

    def crear_muro(self):
        filas = 5
        columnas = 6
        margen_superior = 40
        self.ladrillos = pg.sprite.Group()

        for fila in range(filas):
            for col in range(columnas):
                ladrillo = Ladrillo(fila, col)
                ancho_muro = ladrillo.rect.width * columnas
                margen_izda = (ANCHO - ancho_muro) // 2
                ladrillo.rect.x = margen_izda + col * ladrillo.rect.width
                ladrillo.rect.y = margen_superior + fila * ladrillo.rect.height
                self.ladrillos.add(ladrillo)
                print(ladrillo.rect)

# Clase MejoresJugadores
class MejoresJugadores(Escena):
    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True
            self.pantalla.fill((0, 0, 99))
            pg.display.flip()
        return False
