# GPIO

## Introduction

Les broches GPIO (General Purpose Input/Output) sont des ports sur le Raspberry Pi Pico qui permettent une communication bidirectionnelle entre le microcontrôleur et des composants externes. En d'autres termes, elles permettent de transmettre et de recevoir des signaux.

Pour utiliser les broches GPIO, vous devez d'abord configurer leur mode d'opération, qui peut être en entrée (pour recevoir des signaux) ou en sortie (pour envoyer des signaux). Vous pouvez également configurer la broche pour une résistance pull-up ou pull-down, qui aide à stabiliser le signal et à éviter les interférences.

## Répertoire des programmes lier au GPIO

### [Lesson_3](Lesson_3) : Contrôle d'une LED 

  ==> [led1.py](Lesson_3/led1.py) est un programme qui allume une led
  
  ==> [led2.py](Lesson_3/led2.py) est un programme qui éteint une led
  

### [Lesson_4](Lesson_4) : Utilisation de la bibliothèque time & d'une boucle

==> [Blink_1.py](Lesson_4/Blink_1.py) est un programme qui allume et éteint une led 10 fois

==> [Blink_2.py](Lesson_4/Blink_2.py) est un programme qui fais clignoter une led à l'infini avec deux temps de pause et un temps d'allumage

==> [Blink_3.py](Lesson_4/Blink_3.py) est un programme qui fais clignoter une led à l'infini


### [Lesson_5](Lesson_5) : Lecture du bouton poussoir & interruption

==> [Button_Led_1.py](Lesson_5/Button_Led_1.py) est un programme qui allume une led avec un bouton poussoir par interrruption

==> [Button_Led_2.py](Lesson_5/Button_Led_2.py) est un programme qui allume une led avec un bouton poussoir par interrruption par le biais d'une variable


## Fonctionnement

Vous pouvez retrouver toute les vidéos/photos dans le fichier "Lesson" qui correspond au programme

Une explication détaillé se trouve directement dans le code de chaque programme

#### Exemple [Blink_2.py](Lesson_4/Blink_2.py) de la [Lesson_4](Lesson_4)
![Blink_2](https://user-images.githubusercontent.com/125505805/224541846-fb4c1db4-3126-4f0a-997c-0b854ab8b169.gif)

![image](https://user-images.githubusercontent.com/125505805/224542300-899dda4b-29ac-4a37-ac0e-d4362f426542.png)

## Description des fonction utilisées

### - pin()

La fonction Pin permet de configurer et de contrôler les broches du Raspberry Pi Pico. Elle permet de spécifier les modes d'entrée/sortie, d'activer/désactiver les broches, et de lire/écrire des valeurs numériques. La fonction Pin est donc essentielle pour interagir avec les périphériques connectés au Pico via ses broches.

### - toggle()

### - irq()

### - import()

### - value()

### - sleep()

### - while true

### - variable


