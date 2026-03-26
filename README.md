# aimlprojecthttps://github.com/bhumika25bai10951-coder/aimlproject/edit/main/README.md
Study Focus Detector (OpenCV Project)

 Overview
The Study Focus Detector is a Python-based computer vision project that uses a webcam to detect whether a person is **FOCUSED** or **DISTRACTED** while studying.  
It works by comparing consecutive webcam frames and measuring the amount of movement.

 Low movement-FOCUSED
 High movement-DISTRACTED

This project is developed using Python and OpenCV.

---

 Features
- Live webcam feed detection
- Motion detection using frame difference
- Displays real-time status:
  -  FOCUSED
  -  DISTRACTED
  -  STARTING...
- Clean modular structure (5 separate files)
- Exit using ESC key

---

Technologies Used
- Python 
- OpenCV(cv2)
- Webcam camera

---
 Modules Explanation

 1. initialize_camera.py
Handles:
- Opening the webcam
- Capturing frames
- Converting frames to grayscale

---

2. detect_movement.py
Handles:
- Frame difference calculation
- Threshold conversion
- Motion calculation

---

3. defocus.py
Handles:
- Deciding if the user is focused or distracted

---

 4. display_module.py
Handles:
- Displaying text on webcam feed
- Showing the output window
- Exit detection (ESC key)

---

 5. main.py
Main file that connects all modules and runs the program loop.
---

---

## 📂 Project Structure
