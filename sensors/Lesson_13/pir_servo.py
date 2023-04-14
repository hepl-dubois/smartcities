from machine import Pin # importer la classe Pin pour gérer les broches GPIO
from utime import sleep # importer la fonction sleep pour ajouter des délais
from servo import SERVO # importer la classe SERVO pour gérer le servo-moteur

servo = SERVO(Pin(20)) # créer un objet SERVO sur la broche 20
miniPir = Pin(18, Pin.IN) # créer un objet Pin pour le capteur PIR sur la broche 18 en entrée

while True: # boucle infinie
    if miniPir.value()== 1: # si le capteur PIR détecte un mouvement
        print('Motion Detected') # afficher un message
        servo.turn(100) # tourner le servo-moteur à 100 degrés
        sleep(2) # attendre 10 secondes
        
        servo.turn(0) # tourner le servo-moteur à 0 degré pour revenir à la position initiale
