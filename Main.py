import pygame, sys,random
from pygame.locals import *
from vivant import *
from Entite.animauxC import *
from Entite.animauxH import *
from Entite.animauxP import *
listeDesVivants= listeDesHerbivores + listeDesCarnivores + listeDesPlantes

pygame.init()

#Liste des couleurs pour plus tard potentiellement remplacé par des images/sprites ou dans classe abstraite faux que je relise le cours
GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE)

#définir taille écran:
SCREENWIDTH=800
SCREENHEIGHT=600
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Environnement")

#vitesse du jeu en fps
FPS = 0
FPS = 20

#Regroupement de tous les sprites => potentiellement peut etre bougé
#all_sprites_list = pygame.sprite.Group()

#PNJANIMAL = Animal(color, taille_du_sprite, speed, point_de_vies)
#PNJANIMAL = animal(WHITE, 10, 2, 100)
frames=0
while 1:
    for event in pygame.event.get():
        if event.type== QUIT: #if pressing the X, quit the progra
            pygame.quit() #stop pygame
            sys.exit() #stop the program
    screen.fill((0,0,0)) #clear the screen;
    #print(str(len(listeDesVivants))) 
    i=0
    toKill = []
    frames+=1
    if frames>3:
        frames=0
    while i<len(listeDesVivants): #update all animals
        newPosition=listeDesVivants[i].deplacer(random.randrange(0,8))
        #print(gif)
        listeDesVivants[i].draw(newPosition, frames)
        if listeDesVivants[i].energie>=1:
            listeDesVivants[i].energie -=1
            print(listeDesVivants[i].energie)
        else:
            if listeDesVivants[i].vie>=1:
                listeDesVivants[i].energie+=listeDesVivants[i].vie
                listeDesVivants[i].vie=0
                #print(listeDesVivants[i].energie)
                
        if listeDesVivants[i].vie <=0 and listeDesVivants[i].energie<=0: #demander Lurkin prblm point de vie/energie
            #print(i)
            toKill.append(i)
        i+=1
    #listeDesVivants+=listeDesNaissances
    for dead in reversed(toKill):
        #print("1",dead)
        listeDesVivants.remove(listeDesVivants[dead])
        #print("donne")
        
        
    pygame.display.update() #update display
    pygame.time.Clock().tick(FPS) #limit FPS



