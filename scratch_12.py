#import numpy as np
import cv2

data_dir='/home/user/PycharmProjects/GTA V FIRE/'
video_filename='Euphoria physics.mp4'
cap = cv2.VideoCapture(data_dir+video_filename)

while cap.isOpened():
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()