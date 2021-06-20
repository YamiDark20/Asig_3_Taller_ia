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
        #print(seleccionado, p)
        #print(seleccionado[0][0])
        self.nfila = int(seleccionado[0][0])

    def modificarColum(self, seleccionado, p):
        self.ncolum = int(seleccionado[0][0])

    def modificarIniciador(self, seleccionado, p):
        self.iniciador = seleccionado[0][0]

    def iniciar_juego(self):
        self.menu.disable()
        self.menu.full_reset()
        #print(self.iniciador)
        t = TableroVisual(self.nfila, self.ncolum, self.surface, self.iniciador)
        t.pintarTablero()

        #while True:
            #events = pygame.event.get()
            #for e in events:
                #if e.type == pygame.QUIT:
                    #exit()
                #elif e.type == pygame.KEYDOWN:
                    #if e.key == pygame.K_ESCAPE:
                        #self.menu.enable()
            #if self.menu.is_enabled():
                #self.menu.update(events)
                #break
            #self.surface.fill(BLANCO)
            #pygame.draw.rect(self.surface, (255, 0, 0), (120, 60, 120, 60))
            #pygame.display.flip()

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


#menu = pygame_menu.Menu(
    #height=400,
    #theme=pygame_menu.themes.THEME_BLUE,
    #title='Menu de inicio del juego',
    #width=700
#)

#posiciones = [
    #('4', 1), ('5', 2), ('6', 3), ('7', 4), ('8', 5), ('9', 6), ('10', 7)]
#menu.add.button('Jugar', start_the_game)
#menu.add.selector('N° Filas: ', posiciones)
#menu.add.selector('N° Columnas: ', posiciones)
#menu.add.selector('¿Quien inicia?: ', [('Jugador', 1), ('Agente', 2)])
#menu.add.button('Salir del Juego', pygame_menu.events.EXIT)
#t = TableroVisual()

#if __name__ == '__main__':
    #while True:
        #events = pygame.event.get()
        #for event in events:
            #if event.type == pygame.QUIT:
                #sys.exit()
        #surface.fill(BLANCO)
        #if menu.is_enabled():
            #menu.mainloop(surface)
        #pygame.display.flip()
m = MenuPrincipal()
m.iniciarVista()