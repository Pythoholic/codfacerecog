import face_recognition
import os

if os.path.exists(os.path.abspath("recognize/images/images_cod.jpg")):
    image = face_recognition.load_image_file(os.path.abspath("recognize/images/images_cod.jpg"))
    face_locations = face_recognition.face_locations(image)
    face_landmarks_list = face_recognition.face_landmarks(image)
    print (face_locations)
    print (face_landmarks_list)
else:
    print ("Not found")
