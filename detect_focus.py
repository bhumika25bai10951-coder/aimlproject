def decide_focus_status(movement, threshold_value=800000):
    if movement is None:
        return "STARTING...", (255, 255, 0)

    if movement > threshold_value:
        return "DISTRACTED", (0, 0, 255)   # Red
    else:
        return "FOCUSED", (0, 255, 0)      # Green
