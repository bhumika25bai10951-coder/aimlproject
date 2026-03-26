import cv2

def initialize_camera():
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Camera not working")
        return None
    return camera
