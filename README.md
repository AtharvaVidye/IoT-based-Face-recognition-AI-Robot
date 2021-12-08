# Abstract

The detection of human facial emotions is a major goal in the current world of technology. Robotic applications are used in almost all domains. In order for us to communicate effectively with robots, face recognition is essential. The project aims to develop and implement a new face recognition system based on CV (Computer Vision) and IoT (Internet of Things). The program is revealed in many facial images of people from different backgrounds and backgrounds. This creates a training database that helps in facial recognition. Then, when the robot detects a human face, it initiates a face recognition algorithm that uses the Local Binary Pattern (LBP) method.


### Face Detection

The face detector we use is made using the classic Histogram of Oriented Gradients (HOG) feature combined with a linear classifier, an image pyramid, and sliding window detection scheme. The pose estimator was created by using dlib’s implementation of the paper. When using a distance threshold of 0.6, the dlib model obtains an accuracy of 99.38% on the standard LFW face recognition benchmark, which is comparable to other state-of-the-art methods for face recognition as of February 2017. This accuracy means that, when presented with a pair of face images, the tool will correctly identify if the pair belongs to the same person or is from different people 99.38% of the time.

### Implementation

For Face Recognition we have used Python 3.6 using the Anaconda Spyder platform for debugging and coding. After that, we implemented it in Raspberry Pi Board 3.  We have used “face_recognition” library to recognize the face and used “pyttsx3” library to give the voice output when the face is recognized. Also used library “requests” and webhook Integromat to store the user’s data on Google Excel sheet. Implemented DHT11 temperature sensor to Raspberry Pi Board 3 to measure the temperature of the user and it will be recorded in the Google Excel sheet. 

### Block Diagram

<img src="F:\Atharva\TY sem II\IoT-based-Face-recognition-Robot\block diagram.png" alt="My cool logo"/>

