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
    """ execute les commande"""
    """ le 1 : avancer """
    if i==0:
        deux.turn(100,360,True)
    """ le 2 tourner a gauche """
    if i==3 :
        deuxgauche.turn(100,360,True)
    """ le 3 tourner a droite """
    if i==1 :
        deuxdroite.turn(100,360,True)
    """ le 4 reculer"""
    if i==2 :
        deux.turn(-100,360,True)
        
def InitComm():
  brick=rechercher_brique("NXT5")
  gauche = nxt.Motor(brick, PORT_B)
  droite = nxt.Motor(brick, PORT_C)
  deux = nxt.SynchronizedMotors(gauche,droite,0)
  deuxgauche = nxt.SynchronizedMotors(gauche, droite, 100)
  deuxdroite = nxt.SynchronizedMotors(droite, gauche, 100)



"""commande(1,brick)
sleep(0.1)
commande(2,brick)
sleep(0.1)
commande(3,brick)
sleep(0.1)
commande(4,brick)
printVersion(brick)"""


    
