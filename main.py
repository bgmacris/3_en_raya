import pygame
import copy
import sys
import time
from pygame.locals import *

pygame.init()
dimensiones = [200, 200]
ventana = pygame.display.set_mode(dimensiones)
pygame.display.set_caption(":)")

reloj = pygame.time.Clock()
ancho = 60
alto = 60
margen = 5

MAX = 1
MIN = -1
global jugada_maquina

tablero = [[0 for i in range(3)] for i in range(3)]


def minimax(tablero, jugador):
    global jugada_maquina

    if game_over(tablero):
        return [ganador(tablero), 0]

    movimientos = []
    for jugada in range(0, len(tablero)):
        if tablero[jugada] == 0:
            trableroaux = tablero[:]
            trableroaux[jugada] = jugador

            puntuacion = minimax(trableroaux, jugador*(-1))
            movimientos.append([puntuacion, jugada])

    if jugador == MAX:
        movimiento = max(movimientos)
        jugada_maquina = movimiento[1]
        return movimiento[0]
    else:
        movimiento = min(movimientos)
        return movimiento[0]


def game_over(tablero):
    no_tablas = False
    for i in range(0, len(tablero)):
        if tablero[i] == 0:
            no_tablas = True

    if ganador(tablero) == 0 and no_tablas:
        return False
    else:
        return True


def ganador(tablero):
    lineas = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
              [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    ganador = 0
    for linea in lineas:
        if tablero[linea[0]] == tablero[linea[1]] and tablero[linea[0]] == tablero[linea[2]] and tablero[linea[0]] != 0:
            ganador = tablero[linea[0]]
    return ganador


def jugada_ordenador(tablero):
    global jugada_maquina
    punt = minimax(tablero[:], MAX)
    print(MAX, jugada_maquina)
    tablero[jugada_maquina] = MAX

    tableroaux = []
    for i in range(0, len(tablero), 3):
        tableroaux.append(tablero[i:i+3])
    print(tableroaux)
    print("\n")
    return tableroaux


jugada_player = True
while True:
    for evento in pygame.event.get():
        # Eventos en pantalla
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        
        elif evento.type == pygame.MOUSEBUTTONDOWN and jugada_player:
            pos = pygame.mouse.get_pos()
            columna = pos[0] // (ancho + margen)
            fila = pos[1] // (alto + margen)
            tablero[fila][columna] = -1
            jugada_player = False
        

        # Código de dibujo
        ventana.fill((0, 0, 0))
        # Todos los dibujos van despues de esta linea

        for i in range(0, 3):
            for j in range(0, 3):
                color = [161, 158, 157]
                if tablero[i][j] == MAX:
                    color = [44, 108, 182]
                if tablero[i][j] == MIN:
                    color = [56, 182, 44]
                pygame.draw.rect(ventana, color, [
                                 (margen + ancho) * j + margen, (margen + alto) * i + margen, ancho, alto], 0)

        # Todos los dibujos van antes de esta linea
        pygame.display.flip()

        # Logica del juego
    
        if not jugada_player:
            time.sleep(0.3)
            controlTablero = []
            for i in tablero:
                controlTablero += i
            tablero = jugada_ordenador(controlTablero)
            jugada_player = True


        

    pygame.display.update()
