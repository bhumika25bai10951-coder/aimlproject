def capture_gray_frame(camera):
    ret, frame = camera.read()
    if not ret:
        return None, None
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return frame, gray_frame
