from PIL import Image,ImageDraw
import math
from Properties import *
import time


with open('facedatatest.txt', 'r') as f1:
    line_1 = f1.readlines()
with open('testimages.txt', 'r') as f2:
    line_2 = f2.readlines()



detected_as_faces=[]
detected_as_nonfaces=[]

faces_detected_as_faces=[]
faces_detected_as_nonfaces=[]

nonfaces_detected_as_faces=[]
nonfaces_detected_as_nonfaces=[]

#####################################################################################################

digits_detected=[[], [], [], [], [], [], [], [], [], []]

face_indexes = []
nonface_indexes = []

digitZero = []
digitOne = []
digitTwo = []
digitThree = []
digitFour = []
digitFive = []
digitSix = []
digitSeven = []
digitEight = []
digitNine = []

######################################################################################################

# Function that prints the "all images detected as Faces"
def Detected_as_Faces_func():

    width = 60
    height = 70

    for i in range(len(detected_as_faces)):

        # Create a new image with a white background
        image = Image.new('RGB', (width, height), (255, 255, 255))

        # Get a drawing context
        draw = ImageDraw.Draw(image)

        min = detected_as_faces[i] * 70
        max = min + 70

        for y, line in enumerate(line_1):
            if (y >= min and y < max):
                for x, character in enumerate(line):
                    if character == '#':
                        draw.point((x, y-min), (0, 0, 0))
        g = "All Detected as Faces\Image no."
        g = g + str(detected_as_faces[i]) + ".png"
        image.save(g)
    print("All images classified as detected as Faces will be found in <All Detected as Faces> Folder ")

######################################################################################################

# Function that prints the "all images detected as Non Faces"
def Detected_as_NonFaces():

    width = 60
    height = 70

    for i in range(len(detected_as_nonfaces)):

        # Create a new image with a white background
        image = Image.new('RGB', (width, height), (255, 255, 255))

        # Get a drawing context
        draw = ImageDraw.Draw(image)

        min = detected_as_nonfaces[i] * 70
        max = min + 70

        for y, line in enumerate(line_1):
            if (y >= min and y < max):
                for x, character in enumerate(line):
                    if character == '#':
                        draw.point((x, y-min), (0, 0, 0))
        g = "All Detected as Non-Faces\Image no."
        g = g + str(detected_as_nonfaces[i]) + ".png"
        image.save(g)
    print("All images classified as detected as Non-Faces will be found in <All Detected as Non-Faces> Folder ")

#####################################################################################################

# Function that prints the "faces detected as Faces"
def Faces_Detected_as_Faces_func():

    width = 60
    height = 70

    for i in range(len(faces_detected_as_faces)):

        # Create a new image with a white background
        image = Image.new('RGB', (width, height), (255, 255, 255))

        # Get a drawing context
        draw = ImageDraw.Draw(image)

        min = faces_detected_as_faces[i] * 70
        max = min + 70

        for y, line in enumerate(line_1):
            if (y >= min and y < max):
                for x, character in enumerate(line):
                    if character == '#':
                        draw.point((x, y-min), (0, 0, 0))
        g = "Faces Detected as Faces\Image no."
        g = g + str(faces_detected_as_faces[i]) + ".png"
        image.save(g)
    print("Images classified as Faces Detected as Faces will be found in <Faces Detected as Faces> Folder ")

#####################################################################################################

# Function that prints the "faces detected as Non Faces"
def Faces_Detected_as_NonFaces_func():

    width = 60
    height = 70

    for i in range(len(faces_detected_as_nonfaces)):

        # Create a new image with a white background
        image = Image.new('RGB', (width, height), (255, 255, 255))

        # Get a drawing context
        draw = ImageDraw.Draw(image)

        min = faces_detected_as_nonfaces[i] * 70
        max = min + 70

        for y, line in enumerate(line_1):
            if (y >= min and y < max):
                for x, character in enumerate(line):
                    if character == '#':
                        draw.point((x, y-min), (0, 0, 0))
        g = "Faces Detected as Non-Faces\Image no."
        g = g + str(faces_detected_as_nonfaces[i]) + ".png"
        image.save(g)
    print("Images classified as Faces Detected as Non-Faces will be found in <Faces Detected as Non-Faces> Folder ")

#####################################################################################################

# Function that prints the "non faces detected as Non Faces"
def NonFaces_Detected_as_NonFaces_func():

    width = 60
    height = 70

    for i in range(len(nonfaces_detected_as_nonfaces)):

        # Create a new image with a white background
        image = Image.new('RGB', (width, height), (255, 255, 255))

        # Get a drawing context
        draw = ImageDraw.Draw(image)

        min = nonfaces_detected_as_nonfaces[i] * 70
        max = min + 70

        for y, line in enumerate(line_1):
            if (y >= min and y < max):
                for x, character in enumerate(line):
                    if character == '#':
                        draw.point((x, y - min), (0, 0, 0))
        g = "Non-Faces Detected as Non-Faces\Image no."
        g = g + str(nonfaces_detected_as_nonfaces[i]) + ".png"
        image.save(g)
    print("Images classified as Non-Faces Detected as Non-Faces will be found in <Non-Faces Detected as Non-Faces> Folder ")

####################################################################################################

# Function that prints the "non faces detected as Faces"
def NonFaces_Detected_As_Faces_func():

    width = 60
    height = 70

    for i in range(len(nonfaces_detected_as_faces)):

        # Create a new image with a white background
        image = Image.new('RGB', (width, height), (255, 255, 255))

        # Get a drawing context
        draw = ImageDraw.Draw(image)

        min = nonfaces_detected_as_faces[i] * 70
        max = min + 70

        for y, line in enumerate(line_1):
            if (y >= min and y < max):
                for x, character in enumerate(line):
                    if character == '#':
                        draw.point((x, y - min), (0, 0, 0))
        g = "Non-Faces Detected as Faces\Image no."
        g = g + str(nonfaces_detected_as_faces[i]) + ".png"
        image.save(g)
    print("Images classified as Non-Faces Detected as Faces will be found in <Non-Faces Detected as Faces> Folder ")

####################################################################################################

# Function that prints the "digits detected"
def Digits_Detected():

    width = 28
    height = 28

    for digit in digits_detected:
        for i in range(len(digit)):

            # Create a new image with a white background
            image = Image.new('RGB', (width, height), (255, 255, 255))

            # Get a drawing context
            draw = ImageDraw.Draw(image)

            min = digit[i] * 28
            max = min + 28

            for y, line in enumerate(line_2):
                if (y >= min and y < max):
                    for x, character in enumerate(line):
                        if character == '+':
                            draw.point((x, y-min), (200, 200, 200))
                        if character == '#':
                            draw.point((x, y - min), (0, 0, 0))
            g = "Digits Detected\\"
            g= g + str(digits_detected.index(digit)) + "\\"
            g = g + str(digit[i]) + ".png"
            image.save(g)
        print("Images classified as Digits Detected like: " + str(digits_detected.index(digit)) + " will be found in <Digits Detected> Folder ")

#####################################################################################################

# Function that creates array of face indices and non face indices
def Face_Marginal_Probability_func(mtrx_labels):
    for i in range(int(451)):
        #lbl refers to label
        lbl = mtrx_labels[i]
        if(lbl == "1"):
            face_indexes.append(i)
        else:
            nonface_indexes.append(i)

#####################################################################################################

# Function that creates array for each digit [0-9] and
# append in each one the indices it matched from digit_labels array
def Digit_Marginal_Probability_func(digit_labels):
    for i in range(int(5000)):
        lbl = digit_labels[i]
        if(lbl == "0"):
            digitZero.append(i)
        if(lbl == "1"):
            digitOne.append(i)
        elif(lbl == "2"):
            digitTwo.append(i)
        elif(lbl == "3"):
            digitThree.append(i)
        elif(lbl == "4"):
            digitFour.append(i)
        elif(lbl == "5"):
            digitFive.append(i)
        elif(lbl == "6"):
            digitSix.append(i)
        elif(lbl == "7"):
            digitSeven.append(i)
        elif(lbl == "8"):
            digitEight.append(i)
        elif(lbl == "9"):
            digitNine.append(i)

#####################################################################################################

# Function that calculates the prior probability of image being a face
def Face_Prior_Probability():
    return round(len(face_indexes) / int(len(face_training_lbls)), 2)

# Function that calculates the prior probability of image not being a face
def Non_Face_Prior_Probability():
    return round((int(len(face_training_lbls)) - len(face_indexes)) / int(len(face_training_lbls)), 2)

# Function that calculates the prior probability of digit zero
def Digit_Zero_Prior_Probability():
    return round(len(digitZero) / int(len(digit_training_lbls)), 2)

# Function that calculates the prior probability of digit one
def Digit_One_Prior_Probability():
    return round(len(digitOne) / int(len(digit_training_lbls)), 2)

# Function that calculates the prior probability of digit two
def Digit_Two_Prior_Probability():
    return round(len(digitTwo) / int(len(digit_training_lbls)), 2)

# Function that calculates the prior probability of digit three
def Digit_Three_Prior_Probability():
    return round(len(digitThree) / int(len(digit_training_lbls)), 2)

# Function that calculates the prior probability of digit four
def Digit_Four_Prior_Probability():
    return round(len(digitFour) / int(len(digit_training_lbls)), 2)

# Function that calculates the prior probability of digit five
def Digit_Five_Prior_Probability():
    return round(len(digitFive) / int(len(digit_training_lbls)), 2)

# Function that calculates the prior probability of digit six
def Digit_Six_Prior_Probability():
    return round(len(digitSix) / int(len(digit_training_lbls)), 2)

# Function that calculates the prior probability of digit seven
def Digit_Seven_Prior_Probability():
    return round(len(digitSeven) / int(len(digit_training_lbls)), 2)

# Function that calculates the prior probability of digit eight
def Digit_Eight_Prior_Probability():
    return round(len(digitEight) / int(len(digit_training_lbls)), 2)

# Function that calculates the prior probability of digit nine
def Digit_Nine_Prior_Probability():
    return round(len(digitNine) / int(len(digit_training_lbls)), 2)

#####################################################################################################

#                  < Functions that calculates the condition probability for each digit >

def Calculating_Condition_Probability_Digit_Zero(feature_vectors, feature_vector):
    probability = 1
    i = 0
    k = 1
    for value in feature_vector:
        count = k
        for index in digitZero:
            vector = feature_vectors[index]
            if(vector[i] == value):
                count += 1
        probability *= count / (len(digitZero) + k)
        i += 1
    return math.log(probability)

def Calculating_Condition_Probability_Digit_One(feature_vectors, feature_vector):
    probability = 1
    i = 0
    k = 1
    for value in feature_vector:
        count = k
        for index in digitOne:
            vector = feature_vectors[index]
            if(vector[i] == value):
                count += 1
        probability *= count / (len(digitOne) + k)
        i += 1
    return math.log(probability)

def Calculating_Condition_Probability_Digit_Two(feature_vectors, feature_vector):
    probability = 1
    i = 0
    k = 1
    for value in feature_vector:
        count = k
        for index in digitTwo:
            vector = feature_vectors[index]
            if(vector[i] == value):
                count += 1
        probability *= count / (len(digitTwo) + k)
        i += 1
    return math.log(probability)

def Calculating_Condition_Probability_Digit_Three(feature_vectors, feature_vector):
    probability = 1
    i = 0
    k = 1
    for value in feature_vector:
        count = k
        for index in digitThree:
            vector = feature_vectors[index]
            if(vector[i] == value):
                count += 1
        probability *= count / (len(digitThree) + k)
        i += 1
    return math.log(probability)

def Calculating_Condition_Probability_Digit_Four(feature_vectors, feature_vector):
    probability = 1
    i = 0
    k = 1
    for value in feature_vector:
        count = k
        for index in digitFour:
            vector = feature_vectors[index]
            if(vector[i] == value):
                count += 1
        probability *= count / (len(digitFour) + k)
        i += 1
    return math.log(probability)

def Calculating_Condition_Probability_Digit_Five(feature_vectors, feature_vector):
    probability = 1
    i = 0
    k = 1
    for value in feature_vector:
        count = k
        for index in digitFive:
            vector = feature_vectors[index]
            if(vector[i] == value):
                count += 1
        probability *= count / (len(digitFive) + k)
        i += 1
    return math.log(probability)

def Calculating_Condition_Probability_Digit_Six(feature_vectors, feature_vector):
    probability = 1
    i = 0
    k = 1
    for value in feature_vector:
        count = k
        for index in digitSix:
            vector = feature_vectors[index]
            if(vector[i] == value):
                count += 1
        probability *= count / (len(digitSix) + k)
        i += 1
    return math.log(probability)

def Calculating_Condition_Probability_Digit_Seven(feature_vectors, feature_vector):
    probability = 1
    i = 0
    k = 1
    for value in feature_vector:
        count = k
        for index in digitSeven:
            vector = feature_vectors[index]
            if(vector[i] == value):
                count += 1
        probability *= count / (len(digitSeven) + k)
        i += 1
    return math.log(probability)

def Calculating_Condition_Probability_Digit_Eight(feature_vectors, feature_vector):
    probability = 1
    i = 0
    k = 1
    for value in feature_vector:
        count = k
        for index in digitEight:
            vector = feature_vectors[index]
            if(vector[i] == value):
                count += 1
        probability *= count / (len(digitEight) + k)
        i += 1
    return math.log(probability)

def Calculating_Condition_Probability_Digit_Nine(feature_vectors, feature_vector):
    probability = 1
    i = 0
    k = 1
    for value in feature_vector:
        count = k
        for index in digitNine:
            vector = feature_vectors[index]
            if(vector[i] == value):
                count += 1
        probability *= count / (len(digitNine) + k)
        i += 1
    return math.log(probability)

####################################################################################################

# Function that calculates the conditional probability of a face
def Calculating_Condition_Probability_Face(feature_vectors, feature_vector):
    probability = 1
    i = 0
    for value in feature_vector:
        count = 1
        for index in face_indexes:
            vector = feature_vectors[index]
            if(vector[i] == value):
                count += 1
        probability *= count / (len(face_indexes) + 1)
        i += 1
    return math.log(probability)

# Function that calculates the conditional probability of not a face
def Calculating_Condition_Probability_NonFace(feature_vectors, feature_vector):
    probability = 1
    i = 0
    for value in feature_vector:
        count = 1
        for index in nonface_indexes:
            vector = feature_vectors[index]
            if(vector[i] == value):
                count += 1
        probability *= count / (len(nonface_indexes) + 1)
        i += 1
    return math.log(probability)

###################################################################################################

#                                    < Naive Bayes Faces >

def NaiveBayes_Face_testing(face_mtrx, index, feature_vectors, function_arr):
    feature_vector = Calculating_Feature_Vector(face_mtrx, index, function_arr)
    face_Prior_Probability = Face_Prior_Probability()
    nonface_prior_probability = Non_Face_Prior_Probability()


    face_Condition_Probability = Calculating_Condition_Probability_Face(feature_vectors, feature_vector)
    nonface_Condition_Probability = Calculating_Condition_Probability_NonFace(feature_vectors, feature_vector)

    if((face_Condition_Probability * face_Prior_Probability) > (nonface_Condition_Probability * nonface_prior_probability)):
        detected_as_faces.append(index)
        if(face_testing_lbls[index] == "1"):
            faces_detected_as_faces.append(index)
            return 0
        else:
            nonfaces_detected_as_faces.append(index)
            return 1
    else:
        detected_as_nonfaces.append(index)
        if(face_testing_lbls[index] == "0"):
            nonfaces_detected_as_nonfaces.append(index)
            return 0
        else:
            faces_detected_as_nonfaces.append(index)
            return 1


def NaiveBayes_Face_Validtaion(face_mtrx, index, feature_vectors, function_arr):
    feature_vector = Calculating_Feature_Vector(face_mtrx, index, function_arr)
    face_prior_prob = Face_Prior_Probability()
    nonface_prior_prob = Non_Face_Prior_Probability()

    face_Condition_Probability = Calculating_Condition_Probability_Face(feature_vectors, feature_vector)
    nonface_Condition_Probability = Calculating_Condition_Probability_NonFace(feature_vectors, feature_vector)

    if((face_Condition_Probability * face_prior_prob) > (nonface_Condition_Probability * nonface_prior_prob)):
        if(face_validation_lbls[index] == "1"):
            return 0
        else:
            return 1
    else:
        if(face_validation_lbls[index] == "0"):
            return 0
        else:
            return 1


def Run_NaiveBayes_Faces_Testing():
    beginning = time.process_time()
    right = 0
    wrong = 0
    feature_vectors = Create_Feature_Vector_for_Training(face_mtrcs, face_array)
    print("Testing...")
    for i in range(int(150 )):
        value = NaiveBayes_Face_testing(face_testing_mtrcs, i, feature_vectors, face_array)
        if (value == 0):
            right += 1
        else:
            wrong += 1

    print("Success rate for Faces Testing is: " + str((right / (right + wrong)) * 100) + "%" + " Time taken to test: " + str(
        time.process_time() - beginning) + " Seconds")

def Run_NaiveBayes_Faces_Validation():
    beginning = time.process_time()
    right = 0
    wrong = 0
    print("Learning...")
    feature_vectors = Create_Feature_Vector_for_Training(face_mtrcs, face_array)
    print("Validating...")
    for i in range(int(301)):
        value = NaiveBayes_Face_Validtaion(face_validation_mtrcs, i, feature_vectors, face_array)
        if(value == 0):
            right += 1
        else:
            wrong += 1
    print("Success rate for Faces Validating is: " + str((right / (right + wrong)) * 100) + "%" + " Time taken to validate: " + str(time.process_time() - beginning) + " Seconds")

def Run_NaiveBayes_Faces():
    Face_Marginal_Probability_func(face_training_lbls)
    Run_NaiveBayes_Faces_Validation()
    Run_NaiveBayes_Faces_Testing()
    print("-----------------------------------------------------------------------------")
    Detected_as_NonFaces()
    Detected_as_Faces_func()
    Faces_Detected_as_Faces_func()
    Faces_Detected_as_NonFaces_func()
    NonFaces_Detected_as_NonFaces_func()
    NonFaces_Detected_As_Faces_func()

######################################################################################################

#                                    < Naive Bayes Digits >

def NaiveBayes_Digit(digit_mtrx, index, feature_vectors, function_arr):
    feature_vector = Calculating_Feature_Vector(digit_mtrx, index, function_arr)

    digitZeroPriorProb = Digit_Zero_Prior_Probability()
    digitOnePriorProb = Digit_One_Prior_Probability()
    digitTwoPriorProb = Digit_Two_Prior_Probability()
    digitThreePriorProb = Digit_Three_Prior_Probability()
    digitFourPriorProb = Digit_Four_Prior_Probability()
    digitFivePriorProb = Digit_Five_Prior_Probability()
    digitSixPriorProb = Digit_Six_Prior_Probability()
    digitSevenPriorProb = Digit_Seven_Prior_Probability()
    digitEightPriorProb = Digit_Eight_Prior_Probability()
    digitNinePriorProb = Digit_Nine_Prior_Probability()

    digitZeroConditionProb = Calculating_Condition_Probability_Digit_Zero(feature_vectors, feature_vector)
    digitOneConditionProb = Calculating_Condition_Probability_Digit_One(feature_vectors, feature_vector)
    digitTwoConditionProb = Calculating_Condition_Probability_Digit_Two(feature_vectors, feature_vector)
    digitThreeConditionProb = Calculating_Condition_Probability_Digit_Three(feature_vectors, feature_vector)
    digitFourConditionProb = Calculating_Condition_Probability_Digit_Four(feature_vectors, feature_vector)
    digitFiveConditionProb = Calculating_Condition_Probability_Digit_Five(feature_vectors, feature_vector)
    digitSixConditionProb = Calculating_Condition_Probability_Digit_Six(feature_vectors, feature_vector)
    digitSevenConditionProb = Calculating_Condition_Probability_Digit_Seven(feature_vectors, feature_vector)
    digitEightConditionProb = Calculating_Condition_Probability_Digit_Eight(feature_vectors, feature_vector)
    digitNineConditionProb = Calculating_Condition_Probability_Digit_Nine(feature_vectors, feature_vector)

    zeroProbability = digitZeroPriorProb * digitZeroConditionProb
    oneProbability = digitOnePriorProb * digitOneConditionProb
    twoProbability = digitTwoPriorProb * digitTwoConditionProb
    threeProbability = digitThreePriorProb * digitThreeConditionProb
    fourProbability = digitFourPriorProb * digitFourConditionProb
    fiveProbability = digitFivePriorProb * digitFiveConditionProb
    sixProbability = digitSixPriorProb * digitSixConditionProb
    sevenProbability = digitSevenPriorProb * digitSevenConditionProb
    eightProbability = digitEightPriorProb * digitEightConditionProb
    nineProbability = digitNinePriorProb * digitNineConditionProb


    arr = [zeroProbability, oneProbability, twoProbability, threeProbability, fourProbability, fiveProbability, sixProbability, sevenProbability, eightProbability, nineProbability]

    index = arr.index(max(arr))
    if(index == 0):
        return 0
    elif(index == 1):
        return 1
    elif(index == 2):
        return 2
    elif(index == 3):
        return 3
    elif(index == 4):
        return 4
    elif(index == 5):
        return 5
    elif(index == 6):
        return 6
    elif(index == 7):
        return 7
    elif(index == 8):
        return 8
    elif(index == 9):
        return 9


def Run_NaiveBayes_Digits_Testing():
    beginning = time.process_time()
    right = 0
    wrong = 0
    feature_vectors = Create_Feature_Vector_for_Training(digit_mtrcs, digit_array)
    print("Testing...")
    for i in range(int(1000 )):
        value = NaiveBayes_Digit(digit_testing_mtrcs, i, feature_vectors, digit_array)
        digits_detected[value].append(i)
        if (value == int(digit_testing_lbls[i])):
            right += 1
        else:
            wrong += 1
    Taken = time.process_time() - beginning
    print("Success rate for Digit Testing is: " + str((right / (right + wrong)) * 100) + "%" + " Time taken to test: " + str(
        Taken) + " Seconds")


def Run_NaiveBayes_Digits_Validation():
    beginning = time.process_time()
    right = 0
    wrong = 0
    print("Learning...")
    feature_vectors = Create_Feature_Vector_for_Training(digit_mtrcs, digit_array)
    print("Validating...")
    for i in range(int(1000 )):
        value = NaiveBayes_Digit(digit_validation_mtrcs, i, feature_vectors, digit_array)
        if (value == int(digit_validation_lbls[i])):
            right += 1
        else:
            wrong += 1
    Taken = time.process_time() - beginning
    print("Success rate for Digit Validating is: " + str((right / (right + wrong)) * 100) + "%" + " Time taken to validate: " + str(
        Taken) + " Seconds")


def Run_NaiveBayes_Digits():
    Digit_Marginal_Probability_func(digit_training_lbls)
    Run_NaiveBayes_Digits_Validation()
    Run_NaiveBayes_Digits_Testing()
    print("-----------------------------------------------------------------------------")
    Digits_Detected()

######################################################################################################
