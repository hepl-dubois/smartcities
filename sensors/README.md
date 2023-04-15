# Sensors

## Introduction

Un capteur, ou "sensor" en anglais, est un dispositif qui permet de mesurer une grandeur physique telle que la température, l'humidité, la pression, la lumière, le son, etc. Les capteurs sont utilisés dans de nombreux domaines pour collecter des données sur l'environnement ou les systèmes, et sont souvent connectés à un microcontrôleur comme le Raspberry Pi Pico pour traiter les données collectées.

## Répertoire de programme lié au Sensors

### [Lesson_10](Lesson_10) : Utilisation d'un détecteur d'humidité/température

  ==> [temp_humid.py](Lesson_10/temp_humid.py) est un programme qui affiche la température et l'humidité sur LCD
  
  ==> [temp_humid_alarm.py](Lesson_10/temp_humid_alarm.py) est un programme qui affiche la température et l'humidité sur LCD en plus de sonner sous un certain seuil
  
  
### [Lesson_11](Lesson_11) : Utilisation d'un mini-ventilateur

  ==> [minifan.py](Lesson_11/minifan.py) est un programme qui active un mini-ventilateur à l'aide d'un bouton poussoir
  
  ==> [temp_mini_fan.py](Lesson_11/temp_mini_fan.py) est un programme qui active un mini-ventilateur par le biais d'un capteur de température/humidité

### [Lesson_13](Lesson_13) : Utilisation d'un capteur pir & d'un servomoteur

  ==> [servo.py](Lesson_13/servo.py) est un programme qui active un servo-moteur
  
  ==> [pir_servo.py](Lesson_13/pir_servo.py) est un programme qui qui active un servo-moteur àl'aide d'un capteur "pir" qui dectecte un mouvement
  
  
  
## Fonctionnement

Vous pouvez retrouver toutes les vidéos/photos dans le fichier "Lesson" qui correspond au programme.

Une explication détaillée se trouve directement dans le code de chaque programme.

#### Exemple [temp_mini_fan.py](Lesson_11/temp_mini_fan.py) de la [Lesson_11](Lesson_11)

![IMG_3564](https://user-images.githubusercontent.com/125505805/232223433-85059a41-0379-44ff-8dc9-b900a35feb98.gif)

## Description des fonctions utilisées

### - dht.readTempHumid()

La fonction dht.readTempHumid() est une méthode qui permet de lire la température et l'humidité à partir d'un capteur DHT11 connecté à un Raspberry Pi Pico. Cette fonction utilise un protocole de communication propriétaire pour communiquer avec le capteur et renvoie les valeurs de température et d'humidité en tant que variables numériques.

### - servo.turn()

La fonction servo.turn() est une méthode qui permet de contrôler un servo-moteur connecté à un Raspberry Pi Pico. Cette fonction envoie un signal de contrôle au servo-moteur pour le faire tourner à un angle spécifié en degrés, généralement entre 0 et 180 degrés. Le signal de contrôle est généré en utilisant une impulsion de largeur d'onde modulée (PWM) pour commander la vitesse et la position du servo-moteur.

### - miniPir.value()

La fonction miniPir.value() est une méthode qui permet de lire la valeur du capteur PIR (détecteur de mouvement) connecté à un Raspberry Pi Pico. Cette fonction retourne la valeur détectée par le capteur, qui est généralement un signal numérique indiquant la présence ou l'absence de mouvement dans la zone de détection.

