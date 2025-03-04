# ✋ Hand Gesture Volume Control using AI 🤖🎚️

## 📌 Overview
This project is an **AI-powered Hand Gesture Volume Control System** that utilizes **MediaPipe for real-time hand tracking** and **Pycaw for audio control**. By simply moving your fingers, you can **increase, decrease, or mute the system volume**—all without touching the keyboard! 🚀

## 🔍 How It Works
1. **Hand landmarks** are detected using **MediaPipe Hands**.
2. The distance between **thumb & index finger** is calculated to control volume.
3. **Pycaw** is used to change the system's master volume based on the hand gesture.
4. The **FPS (frames per second)** is calculated and displayed for performance tracking.
5. **Real-time visualization** with OpenCV to enhance user experience. 🎥

## ✋ Hand Detection Logic
The **MediaPipe Hands API** detects **21 key landmarks** on the hand, which helps in gesture recognition.
```python
mp_hands = mp.solutions.hands
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7) as hands:
```

Once detected, **specific landmarks (thumb & index finger)** are extracted:
```python
x1, y1 = lmList[4][1], lmList[4][2]  # Thumb Tip
x2, y2 = lmList[8][1], lmList[8][2]  # Index Finger Tip
```

A line is drawn between them for better visualization:
```python
cv2.line(image, (x1, y1), (x2, y2), (255, 0, 255), 3)  # Pink Line
```

## 🧠 Logic Behind Volume Control & Other Libraries
### 🎯 **MediaPipe Hand Tracking**
- **Detects hands** in real-time and provides **landmark positions**.
- **Tracks hand movements**, ensuring smooth volume control.

### 🔊 **Pycaw for Volume Control**
- Extracts the system's **audio control interface**:
```python
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
```
- Maps **finger distance** to volume levels:
```python
vol = np.interp(length, [50, 220], [minVol, maxVol])
volume.SetMasterVolumeLevel(vol, None)
```

### 📏 **Mathematics Behind Volume Scaling**
- **Hypotenuse formula** is used to calculate the finger distance:
```python
length = math.hypot(x2 - x1, y2 - y1)
```
- The volume bar dynamically adjusts based on the finger position:
```python
volBar = np.interp(length, [50, 220], [400, 150])
volPer = np.interp(length, [50, 220], [0, 100])
```

## 🛠️ Code Breakdown
### **1️⃣ Initializing Libraries & Webcam**
```python
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # Width
cam.set(4, 480)  # Height
```

### **2️⃣ Detecting Hand Landmarks**
```python
results = hands.process(image)
if results.multi_hand_landmarks:
    for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
```

### **3️⃣ Controlling Volume Based on Finger Distance**
```python
if len(lmList) != 0:
    length = math.hypot(x2 - x1, y2 - y1)
    vol = np.interp(length, [50, 220], [minVol, maxVol])
    volume.SetMasterVolumeLevel(vol, None)
```

### **4️⃣ Displaying Volume Bar & FPS**
```python
cv2.rectangle(image, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
cv2.putText(image, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)
```

## 📦 Requirements
Before running the project, install the necessary dependencies:
```bash
pip install opencv-python mediapipe numpy pycaw comtypes
```

## 🚀 How to Run
1. **Clone the repository**:
   ```bash
   git clone https://github.com/debanganghosh08/hand_gesture_volume_control.git
   cd hand_gesture_volume_control
   ```
2. **Run the script**:
   ```bash
   main.py
   ```
3. **Use hand gestures** to control system volume! 🖐️🎚️

## 🎯 Future Enhancements
🔹 Add **gesture support for play/pause music** 🎵  
🔹 Improve **gesture recognition for multi-hand control** ✋🤚  
🔹 Implement **AI-based hand gesture prediction** 🧠  

📢 **Let’s collaborate!** Fork the repo, experiment, and share your ideas. 🚀


