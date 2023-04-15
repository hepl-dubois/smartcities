# Led_Neo

## Introduction

Leo_Neopixel est une bibliothèque de programmation pour le Raspberry Pi Pico qui permet de contrôler des LEDs WS2812B, également connues sous le nom de NeoPixel.

Cette bibliothèque offre des fonctions pour changer la couleur des LEDs, contrôler leur luminosité et leur fréquence de rafraîchissement.

Elle utilise généralement une interface de communication série pour envoyer des données aux NeoPixels.

## Répertoire de programme lié au Led Néopixel

### [Lesson_12](Lesson_12) : Utilisation d'un néopixel

  ==> [Sensor_1.py](Lesson_6/Sensor_1.py) est un programme qui lit et affiche la valeur du potentiomètre
  
  ==> [Sensor_2.py](Lesson_6/Sensor_2.py) est un programme qui allume une led en fonction de la valeur du potentiomètre (ici supérieur a 30000)
  
  
## Fonctionnement

Vous pouvez retrouver toutes les vidéos/photos dans le fichier "Lesson" qui correspond au programme.

Une explication détaillée se trouve directement dans le code de chaque programme.

#### Exemple [fade.py](Lesson_7/fade.py) de la [Lesson_7](Lesson_7)
![IMG_3259](https://user-images.githubusercontent.com/125505805/224554588-02c6f2c4-70d6-414f-87db-64dfa2886b55.gif)

![image](https://user-images.githubusercontent.com/125505805/224557625-9183961d-847f-4b10-a521-87361036837a.png)


## Description des fonctions utilisées

### - Read_u16()

La fonction read_u16() permet de lire la valeur numérique d'un capteur ou d'un périphérique connecté au Raspberry Pi Pico en utilisant un format de données de 16 bits.

### - Freq()

La fonction freq() permet de régler la fréquence d'un signal numérique envoyé à un périphérique connecté au Raspberry Pi Pico.

### - Duty_16()

La fonction duty_16() permet de régler le rapport cyclique d'un signal numérique envoyé à un périphérique connecté au Raspberry Pi Pico en utilisant un format de données de 16 bits.



