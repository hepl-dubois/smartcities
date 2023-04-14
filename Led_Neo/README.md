# Led_Neo

## Introduction

Les broches AD (Analog to Digital) et PWM (Pulse Width Modulation) du Raspberry Pi Pico permettent des opérations plus avancées que les simples broches GPIO.

Les broches AD sont utilisées pour mesurer des signaux analogiques, tels que des tensions électriques ou des capteurs de température, en les convertissant en valeurs numériques que le microcontrôleur peut lire et interpréter.

Les broches PWM sont capables de générer des signaux électriques à des fréquences et durées d'impulsion spécifiques, ce qui permet de contrôler la vitesse des moteurs ou l'intensité des LED.

## Répertoire de programme lié au AD-PWM

### [Lesson_6](Lesson_6) : Utilisation d'un potentiomètre

  ==> [Sensor_1.py](Lesson_6/Sensor_1.py) est un programme qui lit et affiche la valeur du potentiomètre
  
  ==> [Sensor_2.py](Lesson_6/Sensor_2.py) est un programme qui allume une led en fonction de la valeur du potentiomètre (ici supérieur a 30000)
  
  ==> [Sensor_3.py](Lesson_6/Sensor_3.py) est un programme qui allume une led en fonction de la valeur du potentiomètre (ici entre 20000 & 40000)
  

### [Lesson_7](Lesson_7) : Utilisation de la fonction PWM sur une led

  ==> [Knob.py](Lesson_7/Knob.py) est un programme qui fait varier la lumiosité d'une led en fonction de la valeur d'un potentiomètre
  
  ==> [fade.py](Lesson_7/fade.py) est un programme qui fait varier progressivement la lumiosité d'une led en boucle

### [Lesson_8](Lesson_8) : Utilisation de la fonction PWM & d'un buzzer passif pour générer un son

  ==> [Buzzer_1.py](Lesson_8/Buzzer_1.py) est un programme qui joue une séquence de notes de musique en boucle (DO,RE,MI,FA,SOL,LA,SI)
  
  ==> [two_tiger.py](Lesson_8/two_tiger.py) est un programme qui joue une séquence (réutilisable) de notes de musique en boucle (DO,RE,MI,FA,SOL,LA,SI)
  
  ==> [Beethoven_Joie_Buzzer.py](Lesson_8/Beethoven_Joie_Buzzer.py) est un programme qui joue les 4 premières mesures de l'hymne à la joie de Beethoven en boucle
  
  
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



