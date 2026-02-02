import cv2
import time
import numpy as np
import mediapipe as mp
import win32com.client

# ================= WINDOWS ASYNC VOICE =================
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Volume = 100
speaker.Rate = 0

speaking = False  # 🔒 voice lock

def speak_async(text):
    global speaking
    if speaking:
        return
    speaking = True

    # Purge any queued speech, then speak async
    speaker.Speak("", 3)      # SVSFPurgeBeforeSpeak
    speaker.Speak(text, 1)    # SVSFlagsAsync

# ================= MEDIAPIPE SETUP =================
mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

# ================= PARAMETERS =================
EAR_THRESHOLD = 0.20
EYE_CLOSED_TIME = 2.0
ALERT_INTERVAL = 2.5   # cooldown between alerts

# ================= CAMERA =================
cap = cv2.VideoCapture(0)

eyes_closed_start = None
last_alert_time = 0

def eye_aspect_ratio(eye):
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    return (A + B) / (2.0 * C)

print("INFO: Press ESC to exit")

# ================= MAIN LOOP =================
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = face_mesh.process(rgb)
    eyes_open = False

    if result.multi_face_landmarks:
        for landmarks in result.multi_face_landmarks:
            left_eye = np.array([
                (int(landmarks.landmark[i].x * w),
                 int(landmarks.landmark[i].y * h))
                for i in LEFT_EYE
            ])
            right_eye = np.array([
                (int(landmarks.landmark[i].x * w),
                 int(landmarks.landmark[i].y * h))
                for i in RIGHT_EYE
            ])

            ear = (eye_aspect_ratio(left_eye) +
                   eye_aspect_ratio(right_eye)) / 2.0

            if ear > EAR_THRESHOLD:
                eyes_open = True

            for (x, y) in np.concatenate((left_eye, right_eye)):
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

    current_time = time.time()

    # ================= DROWSINESS LOGIC =================
    if not eyes_open and result.multi_face_landmarks:
        if eyes_closed_start is None:
            eyes_closed_start = current_time

        if current_time - eyes_closed_start >= EYE_CLOSED_TIME:
            cv2.putText(frame, "DROWSINESS DETECTED",
                        (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 3)

            if current_time - last_alert_time >= ALERT_INTERVAL:
                speak_async("Wake up! Drowsiness detected")
                last_alert_time = current_time
    else:
        eyes_closed_start = None
        last_alert_time = 0
        speaking = False   # 🔓 allow next alert

    cv2.imshow("Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
