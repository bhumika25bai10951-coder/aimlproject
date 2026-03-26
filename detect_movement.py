def detect_movement(previous_frame, current_gray):
    if previous_frame is None:
        return None, "STARTING...", (255, 255, 0)

    difference = cv2.absdiff(previous_frame, current_gray)
    _, threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)

    movement = threshold.sum()
    return movement, None, None
