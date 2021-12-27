import pygame, sys,random
from pygame.locals import *
from UI import *

from living import *
from Entite.animalsC import *
from Entite.animalsH import *
from Entite.animalsP import *

from object import *
from Inerte.meat import *
from Inerte.waste import *

from plant import *

class Main:
    pygame.init()

    #vitesse du jeu en fps
    FPS = 0

    #Frame Gif
    frames = 0

    #Terrain
    image = pygame.image.load("background/grass.png")
            
    #Initialisation
    while 1:
        for event in pygame.event.get():
            if event.type== QUIT: #if pressing the X, quit the program
                pygame.quit() #stop pygame
                sys.exit() #stop the program
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit() #stop the program
        screen.blit(image, (0,0))
        
        frames+=1
        if frames > 6:
            frames = 0
            
        # 1er = plantes
        toKill = []
        toAdd = []
        plante = 0
        while plante<len(listeDesPlantes):
            listeDesPlantes[plante].draw(listeDesPlantes[plante].position, frames)
            listeDesPlantes[plante].energyUpdate(plante)
            if listeDesPlantes[plante].health <= 0:
                toKill.append(plante)
                toAdd.append([plante, listeDesPlantes[plante].position])
            listeDesPlantes[plante].inZoneRacine(listeDesDechets)
            listeDesPlantes[plante].inZoneSemis()
            plante+=1
        for dead in reversed(toKill):
            listeDesPlantes.remove(listeDesPlantes[dead]) 
        for i, position in toAdd:
            listeDesDechets.append(Waste(300, position))
            listeDesObjets = listeDesDechets + listeDesViandes

        
        #2eme animaux
        toKill = []
        toAdd = []
        i=0
        while i<len(listeDesAnimaux): #update all animals
            newPosition=listeDesAnimaux[i].move(random.randrange(0,8))
            listeDesAnimaux[i].draw(newPosition, frames)
            listeDesAnimaux[i].energyUpdate(plante)
            if listeDesAnimaux[i].health <= 0:
                toKill.append(i)
                toAdd.append([i, listeDesAnimaux[i].position])
            i+=1

        for dead in reversed(toKill):
            try:
                listeDesCarnivores.remove(listeDesAnimaux[dead])
            except:
                listeDesHerbivores.remove(listeDesAnimaux[dead])
            listeDesAnimaux.remove(listeDesAnimaux[dead])

        for i, position in toAdd:
            viande = Beef(300, position)
            listeDesViandes.append(viande)
            listeDesObjets.append(viande)


        #3eme objets
        toKill = []
        toAdd = []
        objet = 0
        while objet<len(listeDesObjets): #update all objects
            listeDesObjets[objet].draw(listeDesObjets[objet].position, frames)
            if listeDesObjets[objet].energy >= 1:
                listeDesObjets[objet].energy-=1  
                
            else:
                toKill.append(objet)
                if (isinstance(listeDesObjets[objet], Waste)) == False:
                    toAdd.append([objet, listeDesObjets[objet].position])
            objet+=1
            
        for dead in reversed(toKill):
            try:
                listeDesViandes.remove(listeDesObjets[dead])
            except:
                listeDesDechets.remove(listeDesObjets[dead])
            listeDesObjets.remove(listeDesObjets[dead])
            

        for i, position in toAdd:
            listeDesDechets.append(Waste(300, position))
            listeDesObjets = listeDesDechets + listeDesViandes
        
        #childBirth
        for bebeHerbivore in listeDesBebeHerbivores:
            bebeHerbivore.childBirth(listeDesHerbivores,listeDesBebeHerbivores,bebeHerbivore)
        for bebeCarnivore in listeDesBebeCarnivores:
            bebeCarnivore.childBirth(listeDesCarnivores,listeDesBebeCarnivores,bebeCarnivore)


        listeDesAnimaux = listeDesCarnivores + listeDesHerbivores
        listeDesPlantes+=listeDesGraines
        listeDesGraines.clear()

        pygame.display.update() #update display
        pygame.time.Clock().tick(FPS) #limit FPS