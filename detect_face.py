import cv2
import os
import re
import scipy.misc
import warnings
import face_recognition.api as face_recognition
import sys


def get_coordinates(image_path):
    img = face_recognition.load_image_file(image_path)
    locations = face_recognition.face_locations(img)
    location_json=[]
    for coordinates in locations:
        json_dict={
            'ymin':coordinates[0],
            'xmin':coordinates[1],
            'ymax':coordinates[2],
            'xmax':coordinates[3]}

        location_json.append(json_dict)
    return locations,location_json

if __name__ == "__main__":
    image_path=sys.argv[1]
    result,_=get_coordinates(image_path)    
    print("Coordinates: ",result)
    img = cv2.imread(sys.argv[1], 0) 


    for coordinates in result:
        ymin, xmin, ymax, xmax = coordinates
        cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (255,255,0), 2)

        # xmin,ymin ------
        # |          |
        # |          |
        # |          |
        # --------xmax,ymax
  
    # will show the image in a window 
    cv2.imshow('image', img) 
    k = cv2.waitKey(0) & 0xFF
    
    # wait for ESC key to exit 
    if k == 27:  
        cv2.destroyAllWindows() 
        
    # wait for 's' key to save and exit 
    elif k == ord('s'):  
        cv2.imwrite('messigray.png',img) 
        cv2.destroyAllWindows() 