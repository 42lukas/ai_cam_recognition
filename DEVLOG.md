# Projekt-Progress Log (Devlog)

[Zurück zum Projekt](./)

## 07.04.2025 - Beginn
- Projekt initialisiert
- Git-Repository erstellt
- `.gitignore` strukturiert
- erste kleine Version basierend auf existierenden Modell erstellt
- erste Idee für Devlog gehabt :)

## 30.04.2025 - NAO Projekt SetUp
- Connection via code und NAO hergestellt
- Video von einem Ball aufgenommen für Trainingsdaten

## 02.05.2025 - Trainingsdaten vorbereiten
- alle 15 Frames des Videos in ein Bild umgewandelt
- jedes Bild mit labellmg gelabelt
- erstes training für das model

## 04.05.2025 - KI-Training und test
- ich habe die KI mit den Daten trainieren lassen und ein Modell erstellen lassen
- schließlich mit dem gespeicherten Modell "val" Bilder genutzt um zu testen, ob das Modell nun den Ball zuverlässig erkennt
- vorerst Erfolgreich

## 04.05.2025
- ich habe mit Roboflow neue trainingsbilder generiert
- aus den vorhandenen Bildern wurde welche mit rauschen, anderer Helligkeit, usw.
- insgesamt nun über 350 trainingsbilder und 75 Epochen
- neues besseres/robusteres KI-Modell
- vorerst Erfolgreich

## 07.05.2025
- live kamera test durchgeführt mit aktuellstem Modell
- Test war vorerst Erfolgreich, blauer Ball wurde konstant erkannt, rot und gelb eher nicht
- neue Trainingsdaten in Form eines Videos für den gelben und roten Ball aufgenommen
- Trainingsdaten für den gelben Ball vorbereitet
- neues Modell trainiert

## 09.05.2025
- Trainingsdaten aus dem Video des roten Ball vorbereitet (labeln)
- neues KI Modell trainineren
- erste mal über die GPU trainiert => viel schneller als mit Mac CPU (4 Std. gegen wenige Min)


# ToDo:
1. mehr trainingsdaten erstellen und labeln
2. Model weiter trainieren
3. live Kamera test mit LapTop
4. live Kamera test mit NAO