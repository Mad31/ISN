#! /usr/bin/env Python
# -*- coding: utf-8 -*-

import nxt.locator
from nxt.motor import *
import sys
from time import *
from nxt.sensor import *
import Tkinter

def rechercher_brique(nom_brick) :
    """ cherche la brique"""
    try :
      brick=nxt.locator.find_one_brick(name=nom_brick)
      """ tourve la brique"""
    except nxt.locator.BrickNotFoundError, cause :
      raise nxt.locator.BrickNotFoundError, " votre robot n a pas ete trouve"
    return brick

def printVersion(brick):
   """Affiche des informations sur la brique NXT"""
   protVersion, firmVersion = brick.get_firmware_version()
   name, host, signalStrength, freeFlash = brick.get_device_info()
   battery = brick.get_battery_level()
   print "-------------------------------------"
   print "  -- %s -- " % name
   print "-------------------------------------"
   print "Version du protocole: %s.%s" % protVersion
   print "Version du firmware : %s.%s" % firmVersion
   print "-------------------------------------"
   print "Adresse de l hote : %s" % host
   print "Force du signal Bluetooth : %s" % signalStrength
   print "-------------------------------------"
   print "Memoire flash libre : %s" % freeFlash
   print "Niveau de la batterie : %s mV" % battery
   print "-------------------------------------"


def Commande(i):
    # intialisation du capteur de lumière
    lumiere.set_illuminated(True)
    sleep(0.3) # il faut attendre que le capteur s'allume avant de faire la mesure
    lumens=lumiere.get_lightness()
    print lumens
    global mur
    mur=False
    
    """ execute les commande"""
    """ le 0 : avancer et tester si il y a un mur si il y a un mur c'est perdu"""
    if i==0:
        if lumens >500 :
            deux._disable()
            deux.reset_position(True)
            deux._enable()
            deux.turn(75,459,True)
            deux.idle()
        else :
            perdu = True
            mur = True
            print perdu
            lumiere.set_illuminated(False) 
            return perdu
    """ le 2 tourner à gauche 1/4 de tour"""
    if i==1 :
        if lumens <600 :
            mur = True
        deuxgauche._disable()
        deuxgauche._enable()
        deuxgauche.brake()
        deuxgauche.reset_position(True)
        deuxgauche.turn(75,195,True)

    """ le 1 tourner à droite 1/4 de tour"""
    if i==3 :
        if lumens <600 :
            mur = True
        deuxdroite._disable()
        deuxdroite._enable()
        deuxdroite.brake()
        deuxdroite.reset_position(False)
        tacho=deuxdroite.get_tacho()
        print tacho
        deuxdroite.turn(75,195,True)
        tacho=deuxdroite.get_tacho()
        print tacho

    """ le 1 reculer"""
    if i==2 :
        deux.turn(-75,500,True)
    lumiere.set_illuminated(False) # on eteint le capteur, pas la peine de consommer trop !
    print mur
    
def InitComm():
    """ nom_brique=CodeBrick()"""
    brick=rechercher_brique("NXT5")
    gauche = nxt.Motor(brick, PORT_B)
    droite = nxt.Motor(brick, PORT_C)
    global deux # actionneurs servo droite/gauche pour aller tout droit
    global deuxgauche # actionneur servos gauche/droite pour tourner à gauche
    global deuxdroite # actionneur servos droite/gauche pour tourner à droite
    deux = nxt.SynchronizedMotors(gauche,droite,0)
    deuxgauche = nxt.SynchronizedMotors(gauche, droite, 100)
    deuxdroite = nxt.SynchronizedMotors(droite, gauche, 100)
    global lumiere # objet capteur de lumière
    lumiere = nxt.Light(brick, PORT_1)
    
def CodeBrick():
    global gui
    gui = Tkinter.Tk()
    gui.title('BabyBot')
    gui.grid()
    label = Tkinter.Label(gui,text="Saisir l'identifiant du robot")
    label.grid(column=0,row=0,columnspan=2)
    global valeurSaisie
    valeurSaisie = Tkinter.StringVar()
    texte = Tkinter.Entry(gui,textvariable=valeurSaisie)
    texte.grid(column=0,row=1)
    bouton = Tkinter.Button(gui,text="OK",command=BoutonClic)
    bouton.grid(column=1,row=1)
    gui.mainloop()
    return valeurSaisie.get()

def BoutonClic():
    if valeurSaisie.get():
      gui.quit()

"""commande(1,brick)
sleep(0.1)
commande(2,brick)
sleep(0.1)
commande(3,brick)
sleep(0.1)
commande(4,brick)
printVersion(brick)"""



