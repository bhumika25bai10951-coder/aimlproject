import cv2
from camera_module import initialize_camera, capture_gray_frame
from movement_module import detect_movement
from focus_module import decide_focus_status
from display_module import display_frame


camera = initialize_camera()
if camera is None:
    exit()

previous_frame = None

while True:
    frame, gray_frame = capture_gray_frame(camera)

    if frame is None:
        break

    movement = detect_movement(previous_frame, gray_frame)
    status_text, color = decide_focus_status(movement)

    previous_frame = gray_frame

    if not display_frame(frame, status_text, color):
        break


camera.release()
cv2.destroyAllWindows()
