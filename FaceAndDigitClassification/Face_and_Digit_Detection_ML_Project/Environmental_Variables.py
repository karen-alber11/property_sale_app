# Training data percentage
Percentage = 1
Percentage_value =0.1

######################################################################################################

digit_testing_mtrcs = []
digit_testing_lbls = []

digit_validation_mtrcs = []
digit_validation_lbls = []

digit_training_lbls = []
digit_mtrcs = []

#######################################################################################################

face_testing_mtrcs = []
face_testing_lbls = []

face_validation_mtrcs = []
face_validation_lbls = []

face_training_lbls = []
face_mtrcs = []

#######################################################################################################

weights = []
feature_values = []

#######################################################################################################

# Function that creates a feature vector for all images in training set
def Create_Feature_Vector_for_Training(mtrcs, function_arr):
    feature_vectors = []
    for i in range(len(mtrcs)):
        arr_feature = []
        for func in function_arr:
            value = func(mtrcs, i)
            arr_feature.append(value)
        feature_vectors.append(arr_feature)
    return feature_vectors

######################################################################################################

# Function that creates a feature vector for queried image
def Calculating_Feature_Vector(mtrx, index, function_arr):
    feature_vector = []
    for arr in function_arr:
        value = arr(mtrx, index)
        feature_vector.append(value)
    return feature_vector

######################################################################################################