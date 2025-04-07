import cv2
from ultralytics import YOLO

# Modell laden (vortrainiertes YOLOv8 Nano)
model = YOLO("yolov8n.pt")

# Webcam starten
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Kamera konnte nicht gestartet werden.")
    exit()

print("📷 Kamera gestartet. Drücke Q zum Beenden.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Kein Frame erhalten.")
        break

    # Inferenz mit YOLO
    results = model(frame)

    # Ergebnis anzeigen
    annotated_frame = results[0].plot()
    cv2.imshow("YOLOv8 Live", annotated_frame)

    # Konsolenausgabe der Labels
    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        conf = float(box.conf[0])
        print(f"Erkannt: {label} mit Confidence {conf:.2f}")

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()