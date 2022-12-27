import time
from Properties import *
from collections import Counter


# KNN_face = int(math.sqrt(len(faceLabels)) / 2)
KNN_face = 1

# KNN_digit = int(math.sqrt(len(digitLabels)))
KNN_digit = 1

######################################################################################################

#                                       < KNN Digits >

def KNN_digit_func(digit_mtrx, index, features):
    feature_vector = Calculating_Feature_Vector(digit_mtrx, index, digit_array)

    arr_diff = []

    for vector in features:
        sum = 0
        i = 0
        for value in feature_vector:
            sum += abs(vector[i] - value)
            i += 1
        arr_diff.append(sum)


    arr_index = []
    k = KNN_digit

    for _ in range(k):
        d = min(arr_diff)
        index = arr_diff.index(d)
        arr_index.append(index)
        arr_diff[index] = 10000000


    arr_value = []
    for index in arr_index:
        arr_value.append(digit_training_lbls[index])

    count = Counter(arr_value)
    value = count.most_common(1)[0][0]

    return value


# Function that returns the success rate of digit recognition (Accuracy)
def Run_KNN_Digits_func(f):
    beginning = time.process_time()
    global KNN_digit
    KNN_digit = f
    right = 0
    wrong = 0
    print("Learning...")
    feature_vectors = Create_Feature_Vector_for_Training(digit_mtrcs, digit_array)
    print("Validating...")
    for i in range(int(1000 * Percentage_value)):
        value = KNN_digit_func(digit_validation_mtrcs, i, feature_vectors)
        if(value == digit_validation_lbls[i]):
            right += 1
        else:
            wrong += 1
    time_taken = time.process_time() - beginning
    print("Success rate for KNN Digits recognition is: " + str((right / (right + wrong)) * 100) + "%"+" Time taken for recognition is: "+str(time_taken)+" Seconds")
    return ((right / (right + wrong)) * 100)

######################################################################################################

#                                       < KNN Faces >

def KNN_faces_func(face_mtrx, index, features):
    feature_vector = Calculating_Feature_Vector(face_mtrx, index, face_array)
    arr_diff = []
    for vector in features:
        sum = 0
        i = 0
        for value in feature_vector:
            sum += abs(vector[i] - value)
            i += 1
        arr_diff.append(sum)


    arr_index = []

    k = KNN_face
    for _ in range(k):
        d = min(arr_diff)
        index = arr_diff.index(d)
        arr_index.append(index)
        arr_diff[index] = 10000000


    arr_value = []
    for index in arr_index:
        arr_value.append(face_training_lbls[index])

    count = Counter(arr_value)
    value = count.most_common(1)[0][0]

    return value


# Function that returns the success rate of face recognition (Accuracy)
def Run_KNN_Faces_func(f):
    beginning = time.process_time()
    global KNN_face
    KNN_face = f
    right = 0
    wrong = 0
    print("Learning...")
    feature_vectors = Create_Feature_Vector_for_Training(face_mtrcs, face_array)
    print("Validating...")
    for i in range(int(301 * Percentage_value)):
        value = KNN_faces_func(face_validation_mtrcs, i, feature_vectors)
        if(value == face_validation_lbls[i]):
            right += 1
        else:
            wrong += 1
    time_taken = time.process_time() - beginning
    print("Success rate for KNN Faces recognition is: " + str((right / (right + wrong)) * 100) + "%"+" Time taken for recognition is: "+str(time_taken)+" Seconds")
    return ((right / (right + wrong)) * 100)

######################################################################################################
