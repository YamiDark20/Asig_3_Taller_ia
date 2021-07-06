import pygame_menu
from pygame_menu.examples import create_example_window
import pygame
from TableroVisual import *
import sys


class MenuPrincipal():

    def __init__(self):
        super(MenuPrincipal, self).__init__()
        self.surface = create_example_window('Asignacion N° 3', (1300, 680))
        self.nfila = self.ncolum = 4
        self.iniciador = 'Jugador'
        self.menu = pygame_menu.Menu(
            height=400,
            theme=pygame_menu.themes.THEME_BLUE,
            title='Menu de inicio del juego',
            width=700
        )

        posiciones = [
            ('4', 1), ('5', 2), ('6', 3), ('7', 4),
            ('8', 5), ('9', 6), ('10', 7)]
        self.menu.add.button('Jugar', self.iniciar_juego)
        self.menu.add.selector('N° Filas: ', posiciones,
        onchange=self.modificarFila)
        self.menu.add.selector('N° Columnas: ', posiciones,
        onchange=self.modificarColum)
        self.menu.add.selector('¿Quien inicia?: ', [
        ('Jugador', 1), ('Agente', 2)], onchange=self.modificarIniciador)
        self.menu.add.button('Salir del Juego', pygame_menu.events.EXIT)

    def modificarFila(self, seleccionado, p):
        #print(p)
        self.nfila = int(seleccionado[0][0])

    def modificarColum(self, seleccionado, p):
        self.ncolum = int(seleccionado[0][0])

    def modificarIniciador(self, seleccionado, p):
        self.iniciador = seleccionado[0][0]

    def iniciar_juego(self):
        self.menu.disable()
        self.menu.full_reset()
        t = TableroVisual(self.nfila, self.ncolum, self.surface, self.iniciador)
        t.pintarTablero()
        #p1 = None
        #p2 = None
        #for punt in t.puntos:
            #if punt.valor == 78:
                #p1 = punt
            #elif punt.valor == 96:
                #p2 = punt
        #print(t.tablero.tablero)
        #print(p1, p2)

    def iniciarVista(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()
            self.surface.fill(BLANCO)
            if self.menu.is_enabled():
                self.menu.mainloop(self.surface)
            pygame.display.flip()


m = MenuPrincipal()
m.iniciarVista()