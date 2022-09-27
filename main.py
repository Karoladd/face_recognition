""" https://www.youtube.com/watch?v=5yPeKQzCPdI """
""" https://pysource.com/2021/08/16/face-recognition-in-real-time-with-opencv-and-python/ """
""" https://stackoverflow.com/questions/53888878/opencv-warn0-terminating-async-callback-when-attempting-to-take-a-picture """
""" https://github.com/Heisenberg301116/Lens-OpenCV-Project/tree/888ffde4fcf02672ec9722f309174473c5895230/OpenCV%20Lens/3%20-%20Face%20Recognition%20from%20webcam """
import cv2
from simple_facerec import SimpleFacerec    # SimpleFacerec is a module while simple_facerec is a library
import subprocess

# Encode faces from a folder
sfr = SimpleFacerec()       # To initialize SimpleFacerec package
sfr.load_encoding_images("images/")    # To load images from the mentioned folder and store their encoding and names

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


while cap.isOpened():
    ret, frame = cap.read()
    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)  # detect_known_faces() will return 2 things: i) a list containing tuples for all images with each tuple represented as: (y2,x1,y1,x2) which stores the image location. ii) a list containing face name of all the images.

    for face_loc, name in zip(face_locations, face_names):      # The Python zip() function accepts iterable items and merges them into a single tuple. The resultant value is a zip object that stores pairs of iterables. You can pass lists, tuples, sets, or dictionaries through the zip() function.
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)
        if(name=="karol"):
             subprocess.call("application.py", shell=True)
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()

