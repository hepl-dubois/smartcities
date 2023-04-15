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


## Description des fonctions utilisées

### - Read_u16()

La fonction read_u16() permet de lire la valeur numérique d'un capteur ou d'un périphérique connecté au Raspberry Pi Pico en utilisant un format de données de 16 bits.



