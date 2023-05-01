from arkanoid import ALTO, ANCHO
from arkanoid.game import Arkanoid

if __name__ == "__main__":
    print(f"El tamaño de la pantalla es {ANCHO}x{ALTO}")
    juego = Arkanoid()
    juego.jugar()
