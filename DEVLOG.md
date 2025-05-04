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



# ToDo:
1. mehr trainingsdaten erstellen und labeln
2. Model weiter trainieren
3. live Kamera test mit LapTop
4. live Kamera test mit NAO