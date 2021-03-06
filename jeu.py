#! /usr/bin/env Python

import nxt.locator
from nxt.motor import *
import sys
from time import *
from nxt.sensor import *

def rechercher_brique(nom_brick) :
    """ cherche la brique"""
    try :
        brick=nxt.locator.find_one_brick(name=nom_brick)
        """ tourve la brique"""
    except nxt.locator.BrickNotFoundError, cause :
        raise nxt.locator.BrickNotFoundError, " votre robot n'a pas �t� trouv�"
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
   print "Adresse de l'h�te : %s" % host
   print "Force du signal Bluetooth : %s" % signalStrength
   print "-------------------------------------"
   print "M�moire flash libre : %s" % freeFlash  
   print "Niveau de la batterie : %s mV" % battery
   print "-------------------------------------"

def commande(i):
    """ execute les commande"""
    """ le 0 : avancer et tester si il y a un mur"""
    if i==0:
        lumiere.set_illuminated(True)
        lumens=lumiere.get_lightness()
        if lumens >600 :
            print lumens
            deux.turn(75,500,True)
            deux.idle()
        else :
            print "perdu"
            lumiere.set_illuminated()
    """ le 3 tourner � gauche 1/4 de tour"""
    if i==3 :
        deuxgauche.brake()
        deuxgauche.reset_position(True)
        deuxgauche.turn(75,170,True)
       
    """ le 2 tourner � droite 1/4 de tour"""
    if i==2 :
        deuxdroite.brake()
        deuxdroite.reset_position(True)
        deuxdroite.turn(75,170,True)
     
    """ le 3 reculer"""
    if i==3 :
        deux.turn(-75,500,True)
   
        

brick=rechercher_brique("NXT5")
gauche = nxt.Motor(brick, PORT_B)
droite = nxt.Motor(brick, PORT_C)
deux = nxt.SynchronizedMotors(gauche,droite,0)
deuxgauche = nxt.SynchronizedMotors(gauche, droite, 100)
infogauche = nxt.SynchronizedTacho(gauche,droite)
deuxdroite = nxt.SynchronizedMotors(droite, gauche, 100)
lumiere = nxt.Light(brick, PORT_1)

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


    
