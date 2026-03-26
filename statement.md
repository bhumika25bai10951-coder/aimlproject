 Project Statement – Study Focus Detector

 Project Title  
Study Focus Detector Using OpenCV (Motion Detection System)

---

 Problem Statement  
Many students face difficulty in maintaining focus during study sessions due to distractions such as unnecessary movement, phone usage, or leaving their study place frequently.
It becomes hard to monitor personal discipline while studying, especially during long study hours.
There is a need for a simple system that can help identify whether a student is staying focused or becoming distracted during study time.

---

 Proposed Solution  
This project proposes a **Study Focus Detector** using **Python and OpenCV**. The system uses a webcam to continuously monitor the student’s movement.

The program captures video frames and compares the current frame with the previous one. If there is a large difference between the frames, it indicates significant movement. Based on the amount of movement detected, the system displays:

- FOCUSED (if movement is low)
- DISTRACTED (if movement is high)

This helps in monitoring study behavior in real time.

---

 Project Objectives  
- To capture live video using a webcam.
- To process video frames using grayscale conversion.
- To detect movement using frame difference technique.
- To classify user activity as **Focused** or **Distracted**.
- To display the focus status on the screen in real time.
- To design the program in a modular format for better readability and management.

---

Expected Outcome  
The expected outcome of this project is a real-time webcam-based application that identifies distraction based on motion detection. The system will help students stay aware of their activity during study time and improve self-discipline.

 Scope of the Project  
This project is useful for:
- Students studying at home
- Online learning environments
- Basic study monitoring systems
