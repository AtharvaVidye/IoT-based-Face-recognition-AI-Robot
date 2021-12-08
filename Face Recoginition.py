import face_recognition
import cv2
import numpy as np
#from espeak import espeak
import pyttsx3
import time
import datetime
import requests

data_to_send = {}


f=1
video_capture = cv2.VideoCapture(0)
#list of known family members for
#Roll No. 51 Shreenivas Telkar
shree_image = face_recognition.load_image_file("shree.jpeg")
shree_face_encoding = face_recognition.face_encodings(shree_image)[0]

#Roll No. 54 Onkar Thombare
onkar_image = face_recognition.load_image_file("onkar.jpeg")
onkar_face_encoding = face_recognition.face_encodings(onkar_image)[0]

#Roll No. 59 Sanket Veer
sanket_image = face_recognition.load_image_file("sanket.jpeg")
sanket_face_encoding = face_recognition.face_encodings(sanket_image)[0]

#Roll No. 61 Atharva Vidye
atharva_image = face_recognition.load_image_file("atharva.jpeg")
atharva_face_encoding = face_recognition.face_encodings(atharva_image)[0]

#Roll No. 62 Parikshit Wagh
parikshit_image = face_recognition.load_image_file("parikshit.jpeg")
parikshit_face_encoding = face_recognition.face_encodings(parikshit_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    shree_face_encoding,
    onkar_face_encoding,
    sanket_face_encoding,
    atharva_face_encoding,
    parikshit_face_encoding
]
known_face_names = [
    "shree",
    "onkar",
    "sanket",
    "atharva",
    "parikshit"
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
engine = pyttsx3.init()
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

   
       
       
    # Only process every other frame of video to save time
    if f == 1 :
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
   
            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"
               
                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]
   
                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    print("name is "+name)
                    engine.say("Hello" + name)
                    engine.say("Welcome to the OFFICE")
                    face_names.append(name)
                    #engine.say(name)
                    f=0
                    data_to_send["Date"] = str(datetime.datetime.now())
                    data_to_send["Name"] = name
                    data_to_send["Temperature"] = "temp"
                    
                    r = requests.post("https://hook.integromat.com/szwis6epibv8ldp8cjv3yysknjvidvh7",json = data_to_send)
                    print(r.status_code)
   
                    #espeak.set_voice("whisper")
                    #espeak.synth("I know you your name is")
                    #you can change the voice and language from here
                   
   
                face_names.append(name)
                engine.runAndWait()
               
               
                #espeak.synth(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)
    

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()