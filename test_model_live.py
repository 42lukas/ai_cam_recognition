import cv2
from ultralytics import YOLO

# Modell nach dem Training laden
run_name = "ball_model_v4"
model_path = f"runs/train/{run_name}/weights/best.pt"
trained_model = YOLO(model_path)

# Webcam starten
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera konnte nicht gestartet werden.")
    exit()

print("Kamera gestartet. 'Q' zum Beenden.")


while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Kein Frame erhalten.")
        break

    # Inferenz mit YOLO
    results = trained_model(frame)

    # Ergebnis anzeigen
    annotated_frame = results[0].plot()
    cv2.imshow("NAO-Model Live", annotated_frame)

    # Konsolenausgabe der Labels
    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        label = trained_model.names[cls_id]
        conf = float(box.conf[0])
        print(f"Erkannt: {label} mit Confidence {conf:.2f}")

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()