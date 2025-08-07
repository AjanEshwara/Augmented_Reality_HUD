import cv2

def ar_hud_display(conflict_detected, conflict_txt = "Conflict Detected!!"):
    
    # use web camera to display the HUD
     cap = cv2.VideoCapture(0)

     if not cap.isOpened():
          print("Error: Could not open video device.")
          return
     while True:
          ret, frame = cap.read()
          if not ret:
                print("Error: Could not read frame.")
                break
              
          height, width= frame.shape[:2]
          cv2.line(frame,(0, height//2), (width, height//2), (0, 255, 0), 2)

          if conflict_detected:
               cv2.rectangle(frame, (width -310, 30), (width - 20, 100), (0, 0, 255), -1)
               cv2.putText(frame, conflict_txt, (width - 300, 80), 
                           cv2.FONT_HERSHEY_SIMPLEX,1.0, (255,255,255), 2)

          cv2.imshow('AR HUD', frame)
          if cv2.waitKey(1) == 27:
               break

     cap.release()
     cv2.destroyAllWindows()
     
     