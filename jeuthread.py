#! /usr/bin/env Python

import nxt.locator
from nxt.motor import *
import sys
from time import *
from nxt.sensor import *
import threading
import atexit

class Thread_commande (threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.numero=i
    def run(self):
        if self.numero==8:
            deux.turn(75,500,True)
            deux.idle()
        if self.numero==4:
            deuxgauche.brake()
            deuxgauche.reset_position(True)
            deuxgauche.turn(75,170,True)
        if self.numero==6 :
            deuxdroite.brake()
            deuxdroite.reset_position(True)
            deuxdroite.turn(75,170,True)
        if self.numero==2 :
            deux.turn(-75,500,True)
       

class Thread_lumiere(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global perdu
        lumiere.set_illuminated(True)
        lumens=lumiere.get_lightness()
        while th_C.is_alive() :
            if lumens>650 :
                lumens=lumiere.get_lightness()
            else :
                lumiere.set_illuminated(False)
                perdu=True
                th_L._Thread__stop()
                th_C._Thread__stop()
        
def rechercher_brique(nom_brick) :
    """ cherche la brique"""
    try :
        brick=nxt.locator.find_one_brick(name=nom_brick)
        """ trouve la brique"""
    except nxt.locator.BrickNotFoundError, cause :
        raise nxt.locator.BrickNotFoundError, " votre robot n'a pas été trouvé"
    return brick

def goodbye(name):
    print "Perdu, %s, merci d'avoir jouer." % (name)

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
global perdu
perdu = False



while (perdu==False) :
    print perdu
    a = input("entrez votre commande : ")
    if (a>0 and a<10 and perdu==False)  :
        th_C  =Thread_commande(a)
        th_L = Thread_lumiere()
        """commande(a)"""
        th_C.start()
        th_L.start()
        score=score+1

goodbye("Joce")
lumiere.set_illuminated(False)
print "Votre score est de: %s" %score
printVersion(brick)


    
