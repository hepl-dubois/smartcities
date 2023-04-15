# Led_Neo

## Introduction

Leo_Neopixel est une bibliothèque de programmation pour le Raspberry Pi Pico qui permet de contrôler des LEDs WS2812B, également connues sous le nom de NeoPixel.

Cette bibliothèque offre des fonctions pour changer la couleur des LEDs, contrôler leur luminosité et leur fréquence de rafraîchissement.

Elle utilise généralement une interface de communication série pour envoyer des données aux NeoPixels.

## Répertoire de programme lié au Led Néopixel

### [Lesson_12](Lesson_12) : Utilisation d'un néopixel

  ==> [rgb_led.py](Lesson_12/rgb_led.py) est un programme qui joue plusieurs couleur sur une led néopixel
  
  ==> [smart_light.py](Lesson_12/smart_light.py) est un programme qui joue plusieur couleur en fonction d'un capteur "Pir" et d'un microphone de détection
  
  
## Fonctionnement

Vous pouvez retrouver toutes les vidéos/photos dans le fichier "Lesson" qui correspond au programme.

Une explication détaillée se trouve directement dans le code de chaque programme.

#### Exemple [rgb_led.py](Lesson_12/rgb_led.py) de la [Lesson_12](Lesson_12)

![IMG_3565](https://user-images.githubusercontent.com/125505805/232225941-bbe73d02-386c-4b4f-bad4-bfaaf6462822.gif)


## Description des fonctions utilisées

### - Read_u16()

La fonction read_u16() permet de lire la valeur numérique d'un capteur ou d'un périphérique connecté au Raspberry Pi Pico en utilisant un format de données de 16 bits.



