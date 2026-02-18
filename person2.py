from ultralytics import YOLO   
import cv2, os,  requests
from datetime import datetime

FIREBASE_URL = "https://online--organ-donation-default-rtdb.firebaseio.com/"

model,cap =YOLO("yolov8n.pt"), cv2.VideoCapture(0)
os.makedirs("snapshots",exist_ok=True)
last_save = 0
last_firebase_update = 0

def send_to_firebase(person_detrection):
    try:
        data = {
            "person_detected": 1 if person_detrection else 0,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        response = requests.put(f"{FIREBASE_URL}/detection.json", json=data)
        if response.status_code == 200:
            print("Firebase updated: person_detected ={1 if person_detected else 0}")
        else:
            print(f"Firebase update failed: {response.status_code}") 
    except Exception as e: 
        print(f"Firebase update error: {e}") 
        
while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    r = results[0]
    person_count = sum(int(box.cls[0]) == 0 for box in r.boxes)
    frame = r.plot()
    cv2.putText(frame, f"Persons: {person_count}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 
                1, (0, 255, 0), 2)
    
    if (datetime.now().timestamp() - last_firebase_update) >= 2: 
        send_to_firebase ( person_count > 0)
        last_firebase_update = datetime.now().timestamp()

    if person_count > 0 and (datetime.now().timestamp() - last_save) >= 3:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cv2.rectangle(frame, (0, 0), (450, 60), (0, 0, 0), -1)
        cv2.putText(frame, f"{timestamp} | Persons: {person_count}", (10, 35),
                     cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.imwrite(f"snapshots/{datetime.now().strftime('%y%m%d_%H%M%S')}.jpg", frame)
        print("saved snapshot")
        last_save = datetime.now().timestamp()

    cv2.imshow("Person Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

send_to_firebase(False)
cap.release()
cv2.destroyAllWindows()
