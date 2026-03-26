def display_frame(frame, status_text, color):
    cv2.putText(frame, status_text, (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

    cv2.imshow("Study Focus Detector", frame)

    key = cv2.waitKey(1)
    if key == 27:   # ESC
        return False
    return True
