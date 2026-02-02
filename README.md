# Driver Drowsiness Detection System 🏍️👁️

A real-time **driver drowsiness detection system** based on **eye behavior analysis** using **MediaPipe FaceMesh** and **Eye Aspect Ratio (EAR)**.  
The system works reliably **with spectacles and without spectacles** and provides **voice alerts** when drowsiness is detected.

This project is developed as part of a **Final Year Engineering Project**.

---
 
## 📌 Overview

Driver drowsiness is a major cause of road accidents.  
This project monitors the driver’s eye state using a webcam and detects prolonged eye closure, which is a strong indicator of drowsiness. When detected, the system generates a **real-time voice alert** to warn the driver.

---

## ✨ Key Features

- Real-time eye detection using **MediaPipe FaceMesh**
- Works **with spectacles and without spectacles**
- Eye Aspect Ratio (EAR) based drowsiness detection
- Voice alert using **Windows Text-to-Speech (SAPI)**
- Prevents repeated voice alerts using a speech-lock mechanism
- Smooth and stable real-time video processing
- No external hardware required (webcam only)

---

## 🧠 Working Principle

1. Webcam captures live video using OpenCV  
2. MediaPipe FaceMesh detects facial landmarks  
3. Eye landmarks are extracted from the face mesh  
4. Eye Aspect Ratio (EAR) is calculated  
5. If EAR remains below a threshold for a fixed duration, drowsiness is detected  
6. A voice alert is generated to wake the driver  

---

## 🛠️ Technologies Used

- **Python 3.10**
- **OpenCV**
- **MediaPipe**
- **NumPy**
- **Windows SAPI (Text-to-Speech)**

---

## 📂 Project Structure

    driver-drowsiness-detection/
    │
    ├── drowsiness_detection.py
    ├── README.md
    ├── requirements.txt
    ├── .gitignore
    └── venv/
---


## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
    ```bash
    git clone https://github.com/your-username/driver-drowsiness-detection.git
    cd driver-drowsiness-detection

---

### 2️⃣ Create and Activate Virtual Environment (Recommended)
    ```bash
    python -m venv venv
    venv\Scripts\activate

### 3️⃣ Install Dependencies
    ```bash
    pip install -r requirements.txt

### ▶️ Run the Project
    ```bash
    python drowsiness_detection.py


Press ESC to exit the program

Ensure proper lighting for best detection accuracy
---

## 🧪 Detection Logic

    EAR Threshold: Determines whether eyes are open or closed
    
    Time Threshold: Drowsiness is detected only if eyes remain closed for a predefined duration
    
    Speech Lock: Ensures only one alert per drowsiness event
---

## ⚠️ Limitations

    Performance depends on lighting conditions
    
    Designed for single-face detection
    
    Requires Windows OS for voice alert feature
---

## 🚀 Future Enhancements

    Yawning detection
    
    Head pose estimation
    
    Night-time detection using IR camera
    
    Mobile or embedded system deployment
    
    Integration with smart helmet or vehicle system
