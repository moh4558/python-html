import cv2
import numpy as np
import face_recognition
import os 

path = 'ImagerAttedance'
images = []
classNames = []
myList = os.listdir(path)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
    print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

# Example usage of the function
encodings = findEncodings(images)

# Display the first image
if len(images) > 0:
    cv2.imshow("Webcam", images[0])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
