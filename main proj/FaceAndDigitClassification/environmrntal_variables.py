

#percent of training data to use
PERCENT = 1
VALPERCENT =0.1



faceValidationMatrices = []
faceValidationLabels = []

faceTestingMatrices = []
faceTestingLabels = []

digitTestingMatrices = []
digitTestingLabels = []

digitValidationMatrices = []
digitValidationLabels = []

digitLabels = []
digitMatrices = []

faceLabels = []
faceMatrices = []

weights = []
feature_values = []

#creates feature vector for all images in training set
def create_fv_for_training(matrices, function_arr):
    featureVectors = []
    for i in range(len(matrices)):
        featureArr = []
        for func in function_arr:
            value = func(matrices, i)
            featureArr.append(value)
        featureVectors.append(featureArr)
    return featureVectors

#creates feature vector for queried image
def calc_feature_vector(matrix, index, function_arr):
    feature_vector = []
    for arr in function_arr:
        value = arr(matrix, index)
        feature_vector.append(value)
    return feature_vector
