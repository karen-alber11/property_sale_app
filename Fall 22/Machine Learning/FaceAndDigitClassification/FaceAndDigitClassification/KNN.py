from NaiveBayes import *
from KNN import *
import matplotlib.pyplot as plt
import time

#####################################################################################################

#                                < Storing Maximum KNN  >

#  Face Recognition success rate
max_KNN_Face = 0
at_max_KNN_Face = 0

#  Digit Recognition success rate
max_KNN_digit = 0
at_max_KNN_digit = 0

#####################################################################################################

#                                     < Storing KNN >

#  Faces success rate
KNN_faces = []
success_faces = []

#  Digits success rate
KNN_digits=[]
success_digits=[]

#  Time taken for Faces recognition
faces_time=[]

#  Time taken for Digits recognition
digits_time=[]

####################################################################################################

#                                         < Digit Data >

# Test Images Opening
digit_test_images = open("./digitdata/testimages", "r")
digit_test_lbls = open("./digitdata/testlabels", "r")

# Training Images Opening
digit_training_images = open("./digitdata/trainingimages", "r")
digit_training_lbls = open("./digitdata/traininglabels", "r")

# Validation Images Opening
digit_validation_images = open("./digitdata/validationimages", "r")
digit_validation_lbls = open("./digitdata/validationlabels", "r")

####################################################################################################

#                                         < Face Data >

# Test Images Opening
face_test_images = open("./facedata/facedatatest", "r")
face_test_lbls = open("./facedata/facedatatestlabels", "r")

# Training Images Opening
face_training_images = open("./facedata/facedatatrain", "r")
face_training_lbls = open("./facedata/facedatatrainlabels", "r")

# Validation Images Opening
face_validation_images = open("./facedata/facedatavalidation", "r")
face_validation_lbls = open("./facedata/facedatavalidationlabels", "r")

####################################################################################################

#                                     < Digits Creation Functions >

# Function that creates an array of Digit Labels from Testing data
def Create_Testing_Digit_Lbls():
    for line in digit_test_lbls:
        digit_testing_lbls.append(line[0])

# Function that creates an array of Digit Labels from Training data
def Create_Training_Digit_Lbls():
    for line in digit_training_lbls:
        digit_training_lbls.append(line[0])

# Function that creates an array of Digit Labels from Validation data
def Create_Validation_Digit_Lbls():
    for line in digit_validation_lbls:
        digit_validation_lbls.append(line[0])



# Function that creates an array of 2D matrices of Testing digits
# reading 1000 test digits. Each digit is a picture made up of 28 lines.
def Create_Testing_Digit_Mtrx(digit_mtrcs):
    for i in range(1000):
        image_mtrx = []
        for i in range(28):
            image_mtrx.append(digit_test_images.readline())
        digit_mtrcs.append(image_mtrx)

# Function that creates an array of 2D matrices of Training Digits
def Create_Training_Digit_Mtrx(digit_mtrcs):
    for i in range(int(5000 )):
        image_mtrx = []
        for i in range(28):
            image_mtrx.append(digit_training_images.readline())
        digit_mtrcs.append(image_mtrx)

# Function that creates an array of 2D matrices of Validation Digits
def Create_Validation_Digit_Mtrx(digit_mtrcs):
    for i in range(int(1000 )):
        image_mtrx = []
        for i in range(28):
            image_mtrx.append(digit_validation_images.readline())
        digit_mtrcs.append(image_mtrx)

####################################################################################################

#                                     < Face Creation Functions >

# Function that creates an array of Face Labels from Testing data
def Create_Testing_Face_Lbls():
    for line in face_test_lbls:
        face_testing_lbls.append(line[0])

# Function that creates an array of Face Labels from Training data
def Create_Training_Face_Lbls():
    for line in face_training_lbls:
        face_training_lbls.append(line[0])

# Function that creates an array of Face Labels from Validation data
def Create_Validation_Face_Lbls():
    for line in face_validation_lbls:
        face_validation_lbls.append(line[0])



# Function that creates an array of 2D matrices of Testing Faces
def Create_Testing_Face_Mtrx(face_mtrcs):
    for i in range(int(150 )):
        image_mtrx = []
        for i in range(70):
            image_mtrx.append(face_test_images.readline())
        face_mtrcs.append(image_mtrx)

# Function that creates an array of 2D matrices of Training Faces
def Create_Training_Face_Mtrx(face_mtrcs):
    for i in range(int(451 )):
        image_mtrx = []
        for i in range(70):
            image_mtrx.append(face_training_images.readline())
        face_mtrcs.append(image_mtrx)

# Function that creates an array of 2D matrices of Validation Faces
def Create_Validation_Face_Mtrx(face_mtrcs):
    for i in range(int(301 )):
        image_mtrx = []
        for i in range(70):
            image_mtrx.append(face_validation_images.readline())
        face_mtrcs.append(image_mtrx)

####################################################################################################

#                                     < Initializing function >

def init():

    #          < Digits Creation >
    Create_Testing_Digit_Mtrx(digit_testing_mtrcs)
    Create_Testing_Digit_Lbls()

    Create_Training_Digit_Mtrx(digit_mtrcs)
    Create_Training_Digit_Lbls()

    Create_Validation_Digit_Mtrx(digit_validation_mtrcs)
    Create_Validation_Digit_Lbls()

    #          < Faces Creation >
    Create_Testing_Face_Mtrx(face_testing_mtrcs)
    Create_Testing_Face_Lbls()

    Create_Training_Face_Mtrx(face_mtrcs)
    Create_Training_Face_Lbls()

    Create_Validation_Face_Mtrx(face_validation_mtrcs)
    Create_Validation_Face_Lbls()

####################################################################################################

#                                             < Printing >

if __name__ == "__main__":

     init()
     print("\n-------FACE Recognition-------")
     print("-----NAIVE BAYES-----")
     Run_NaiveBayes_Faces()
     print("-----------------------------------------------------------------------------")
     print("\n\n-------DIGIT Recognition-------")
     print("[-----NAIVE BAYES-----]")
     Run_NaiveBayes_Digits()
     print("-----------------------------------------------------------------------------")

     for i in range(1,201):

       DigitTestingMtrcs = []
       DigitTestingLbls = []

       DigitValidationMtrcs = []
       DigitValidationLbls = []

       DigitLbls = []
       DigitMtrcs = []


       FaceTestingMtrcs = []
       FaceTestingLbls = []

       FaceValidationMtrcs = []
       FaceValidationLbls = []

       FaceLbls = []
       FaceMtrcs = []


     init()
     print("-------FACE Recognition-------")
     print("iteration number: "+str(i))
     print("-----KNN Algorithm-----")
     beginning = time.process_time()
     l = Run_KNN_Faces_func(i)
     time_taken = time.process_time() - beginning
     faces_time.append(time_taken)
     KNN_faces.append(i)
     success_faces.append(l)
     if(l > at_max_KNN_Face):
         at_max_KNN_Face = l
         max_KNN_Face = i
     print("Max K for Face = " + str(max_KNN_Face) + " at Success rate = " + str(at_max_KNN_Face))
     print("\n-------DIGIT Recognition-------")
     print("iteration number: " + str(i))
     print("-----KNN Algorithm-----")
     beginning = time.process_time()
     ld = Run_KNN_Digits_func(i)
     time_taken = time.process_time() - beginning
     digits_time.append(time_taken)
     KNN_digits.append(i)
     success_digits.append(ld)
     if (ld > at_max_KNN_digit):
         at_max_KNN_digit = ld
         max_KNN_digit = i

     print("Max K for Digit " + str(max_KNN_digit) + " at Success Rate = " + str(at_max_KNN_digit))
     print("-----------------------------------------------------------------------------")

####################################################################################################

#                                             < Plotting >

# Plotting Accuracy vs KNN in Facial recognition
     plt.plot(KNN_faces, success_faces)
     plt.xlabel('K')
     plt.ylabel('Accuracy')
     plt.title('Face Recognition')
     plt.show()

# Plotting Accuracy vs KNN in Digit Recognition
     plt.plot(KNN_digits, success_digits)
     plt.xlabel('K')
     plt.ylabel('Accuracy')
     plt.title('Digit Recognition')
     plt.show()

# Plotting Time vs KNN in Facial recognition
     plt.plot(KNN_faces, faces_time)
     plt.xlabel('K')
     plt.ylabel('Time')
     plt.title('Time Taken For Face Recognition')
     plt.show()

# Plotting Time vs KNN in Digit recognition
     plt.plot(KNN_digits, digits_time)
     plt.xlabel('K')
     plt.ylabel('Time')
     plt.title('Time Taken For Digit Recognition')
     plt.show()

#####################################################################################################