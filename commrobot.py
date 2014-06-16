#! /usr/bin/env Python

import nxt.locator
from nxt.motor import *
import sys
from time import *

def rechercher_brique(nom_brick) :
    """ cherche la brique"""
    try :
        brick=nxt.locator.find_one_brick(name=nom_brick)
        """ tourve la brique"""
    except nxt.locator.BrickNotFoundError, cause :
        raise nxt.locator.BrickNotFoundError, " votre robot n'a pas été trouvé"
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
   print "Adresse de l'hôte : %s" % host
   print "Force du signal Bluetooth : %s" % signalStrength
   print "-------------------------------------"
   print "Mémoire flash libre : %s" % freeFlash  
   print "Niveau de la batterie : %s mV" % battery
   print "-------------------------------------"

def commande(i):
    """ execute les commande"""
    """ le 8 : avancer """
    if i==8:
        deux.turn(100,720,True)
    """ le 2 tourner à gauche """
    if i==4 :
        gauche.turn(100,330,True)
    """ le 3 tourner à droite """
    if i==6 :
        droite.turn(100,330,True)
    """ le 4 reculer"""
    if i==2 :
        deux.turn(-100,360,True)
    if i==7 :
        gauche.turn(100,165,True)
    if i==9 :
        droite.turn(100,165,True)
    if i==1 :
        gauche.turn(100,465,True)
    if i==3 :
        droite.turn(100,465,True)
        

brick=rechercher_brique("NXT5")
gauche = nxt.Motor(brick, PORT_B)
droite = nxt.Motor(brick, PORT_C)
deux = nxt.SynchronizedMotors(gauche,droite,0)
deuxgauche = nxt.SynchronizedMotors(gauche, droite, 100)
deuxdroite = nxt.SynchronizedMotors(droite, gauche, 100)

a=1
score=0

while (a>0 and a<10) :
    a = input("entrez votre commande : ")
    if (a>0 and a<10)  :
        commande(a)
        sleep(0.1)
        score=score+1


print "Votre score est de: %s" %score
printVersion(brick)


    
