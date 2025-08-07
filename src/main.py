import sys
import cv2
from hud.hud import ar_hud_display

def main():
    conflict_detected = True  # Example: will trigger HUD alert

    # Call the HUD display function
    ar_hud_display(conflict_detected=conflict_detected, conflict_txt="Conflict Detected!")

if __name__ == "__main__":
    main()