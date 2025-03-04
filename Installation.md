# 📥 Installation Guide for Hand Gesture Volume Control 🎚️🖐️

## 📌 Prerequisites
Before running the project, ensure your system meets the following requirements:

### 🖥️ System Requirements
- **Operating System**: Windows / macOS / Linux
- **Python Version**: 3.7 or higher
- **Webcam**: Required for real-time hand tracking

### 📦 Required Libraries
Make sure you have the following libraries installed:
- OpenCV (`opencv-python`)
- MediaPipe (`mediapipe`)
- NumPy (`numpy`)
- Pycaw (`pycaw`)
- Comtypes (`comtypes`)

## 🚀 Installation Steps

### 1️⃣ Clone the Repository
First, clone the repository from GitHub:
```bash
git clone https://github.com/debanganghosh08/hand_gesture_volume_control.git
```
Move into the project directory:
```bash
cd hand_gesture_volume_control
```

### 2️⃣ Set Up a Virtual Environment (Optional but Recommended)
To avoid package conflicts, create a virtual environment:
```bash
python -m venv env
```
Activate the virtual environment:
- **Windows:**
  ```bash
  env\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source env/bin/activate
  ```

### 3️⃣ Install Dependencies
Run the following command to install all necessary dependencies:
```bash
pip install -r requirements.txt
```
If you don’t have a `requirements.txt` file, manually install the required packages:
```bash
pip install opencv-python mediapipe numpy pycaw comtypes
```

### 4️⃣ Run the Project
Once the installation is complete, start the hand gesture volume control system:
```bash
python volume_control.py
```

## 🎯 Usage Instructions
- **Move your thumb & index finger** closer to **decrease volume** 🔉
- **Increase the gap** between them to **increase volume** 🔊
- **Bring fingers very close together** to **mute the volume** 🚫🔊
- Press **'Q'** to exit the application.

## ❓ Troubleshooting
- **ModuleNotFoundError:** Run `pip install <missing_module>` to install the required module.
- **Permission Denied Error:** Run the script with administrator privileges.
- **Webcam Issues:** Ensure your webcam is properly connected and accessible.

## 📬 Support
For any issues, open an issue on GitHub: [Hand Gesture Volume Control](https://github.com/debanganghosh08/hand_gesture_volume_control/issues)

🚀 Happy Coding! ✋🎚️

