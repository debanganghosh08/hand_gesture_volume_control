import cv2
import mediapipe as mp
import math
import numpy as np
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Solution APIs
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Volume Control Library Usage 
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol, maxVol, volBar, volPer = volRange[0], volRange[1], 400, 0

# Webcam Setup
wCam, hCam = 640, 480
cam = cv2.VideoCapture(0)
cam.set(3, wCam)
cam.set(4, hCam)

# FPS Calculation
prev_time = 0

# Mediapipe Hand Landmark Model
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7) as hands:

    while cam.isOpened():
        success, image = cam.read()
        if not success:
            continue

        # Convert Image for Processing
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Hand Landmark Detection and Drawing
        lmList = []
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2, circle_radius=5),  # White Points
                    mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2)  # Green Lines
                )

            # Extract Landmark Positions
            myHand = results.multi_hand_landmarks[0]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])          

        # Assigning variables for Thumb and Index Finger Position
        if len(lmList) != 0:
            x1, y1 = lmList[4][1], lmList[4][2]  # Thumb Tip
            x2, y2 = lmList[8][1], lmList[8][2]  # Index Finger Tip

            # Marking Thumb and Index Finger in Pink
            cv2.circle(image, (x1, y1), 15, (255, 0, 255), cv2.FILLED)  # Pink
            cv2.circle(image, (x2, y2), 15, (255, 0, 255), cv2.FILLED)  # Pink  
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 255), 3)  # Pink Line
            length = math.hypot(x2 - x1, y2 - y1)

            if length < 50:
                cv2.line(image, (x1, y1), (x2, y2), (255, 0, 255), 3)  # Stays Pink when close

            vol = np.interp(length, [50, 220], [minVol, maxVol])
            volume.SetMasterVolumeLevel(vol, None)
            volBar = np.interp(length, [50, 220], [400, 150])
            volPer = np.interp(length, [50, 220], [0, 100])

            # Volume Bar - Green
            cv2.rectangle(image, (50, 150), (85, 400), (0, 255, 0), 3)  # Green Border
            cv2.rectangle(image, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)  # Green Fill
            cv2.putText(image, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
                        1, (0, 255, 0), 3)  # Green Text

        # FPS Calculation & Display (Top-Left Corner)
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time
        cv2.putText(image, f'FPS: {int(fps)}', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

        # Show Webcam Feed
        cv2.imshow('Hand Gesture Volume Control', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release Resources
cam.release()
cv2.destroyAllWindows()
