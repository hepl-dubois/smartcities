# LCD

## Introduction

Un écran LCD (Liquid Crystal Display) est un dispositif qui permet d'afficher des informations en utilisant des cristaux liquides. Il est souvent utilisé pour afficher des textes et des images en noir et blanc ou en couleur. Pour afficher du texte ou des images, le contrôleur de l'écran LCD reçoit des signaux numériques du Raspberry Pi Pico et les convertit en commandes qui modifient l'état des cristaux liquides pour afficher les informations. Le contrôleur de l'écran LCD et le Raspberry Pi Pico sont généralement connectés par une interface de communication comme le protocole I2C ou SPI.

## Répertoire de programme lié au LCD

### [Lesson_9](Lesson_9) : Utilisation d'un LCD

  ==> [Lcd_hello_world.py](Lesson_9/Lcd_hello_world.py) est un programme qui affiche un texte sur un LCD
  
  ==> [LCD_Knob.py](Lesson_9/LCD_Knob.py) est un programme qui affiche sur un LCD les valeurs en degrée d'un potentiomètre

  ==> [LCD_Led.py](Lesson_9/LCD_Led.py) est un programme qui affiche sur un LCD les valeurs en degrée d'un potentiomètre et fait varier la lumiosité d'une led en fonction du potentiomètre
  
  
## Fonctionnement

Vous pouvez retrouver toutes les vidéos/photos dans le fichier "Lesson" qui correspond au programme.

Une explication détaillée se trouve directement dans le code de chaque programme.

#### Exemple [Lcd_hello_world.py](Lesson_9/Lcd_hello_world.py) de la [Lesson_9](Lesson_9)

![lcd_1](https://user-images.githubusercontent.com/125505805/226180941-e9bb745e-bd30-4fc7-96b8-547d32b82715.gif)


## Description des fonctions utilisées

### - lcd1602.py (bibliothèque)

La bibliothèque "lcd1602.py" est une bibliothèque Python qui permet de contrôler un écran LCD 1602 à partir d'un Raspberry Pi Pico. Elle contient des fonctions pour initialiser l'écran LCD, afficher du texte, définir la position du curseur et activer ou désactiver le rétroéclairage. La bibliothèque utilise généralement le protocole I2C pour communiquer avec l'écran LCD.




