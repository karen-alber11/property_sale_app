from environmrntal_variables import *

#normalizes continues values to discrete values
def normalized_value(value):
    if(value < 0.05):
        return 0
    elif(value < 0.10):
        return 1
    elif(value < 0.15):
        return 2
    elif(value < 0.18):
        return 3
    elif(value < 0.21):
        return 4
    elif(value < 0.26):
        return 5
    elif(value < 0.31):
        return 6
    elif(value < 0.40):
        return 7
    else:
        return 8

#matrix is the matrix you want to be passed into the function: either faceMatrix or digitMatrix
#row_range and col_range are tupes with start and end indexes [start index, end index], inclusive
#image_no is the image you are reading from the input file, needed to go through matrix
def calculate_pixel_density(row_range, col_range, matrix, image_no):

    total_pixels = (row_range[1] - row_range[0] + 1)*(col_range[1] - col_range[0] + 1)
    colored_pixels = 0

    for i in range(col_range[0],col_range[1]+1):
        for k in range(row_range[0], row_range[1]+1):
            if matrix[image_no][i][k].isspace() is False:
                colored_pixels = colored_pixels + 1
    if total_pixels == 0:
        total_pixels = 1
    frequency = colored_pixels/total_pixels
    return frequency

def split(matrix, image_no, block_no):
    [topMost, bottomMost] = vertical_image_bounds_tuple(matrix[image_no])
    [leftMost, rightMost] = horizontal_image_bounds_tuple(matrix[image_no])

    #splitting columns
    col_split_length = int((abs(rightMost - leftMost) + 1)/3)
    remainder = (abs(rightMost - leftMost) + 1)%3

    c1 = [leftMost, leftMost + col_split_length - 1]
    c2 = [c1[1] + 1, c1[1] + 1 + col_split_length - 1]
    c3 = [c2[1] + 1, rightMost]

    #splitting rows
    row_split_length = int((abs(bottomMost -  topMost) + 1)/4)
    row_remainder = (abs(bottomMost -  topMost) + 1)%4

    r1 = [topMost, topMost + row_split_length - 1]
    r2 = [r1[1] + 1, r1[1] + 1 + row_split_length - 1]
    r3 = [r2[1] + 1, r2[1] + 1 + row_split_length - 1]
    r4 = [r3[1] + 1, bottomMost]

    if(block_no == 1):
        return [r1, c1]
    elif(block_no == 2):
        return [r1, c2]
    elif(block_no == 3):
        return [r1, c3]
    elif(block_no == 4):
        return [r2, c1]
    elif(block_no == 5):
        return [r2, c2]
    elif(block_no == 6):
        return [r2, c3]
    elif(block_no == 7):
        return [r3, c1]
    elif(block_no == 8):
        return [r3, c2]
    elif(block_no == 9):
        return [r3, c3]
    elif(block_no == 10):
        return [r4, c1]
    elif(block_no == 11):
        return [r4, c2]
    elif(block_no == 12):
        return [r4, c3]

def horizontal_image_bounds_tuple(image):
    leftMost = 1000
    rightMost = 0
    j = 0
    for line in image:
        for char in line:
            if(char == "#" or char == "+"):
                if(j > rightMost):
                    rightMost = j
                if(j < leftMost):
                    leftMost = j
            j += 1
        j = 0
    return [leftMost, rightMost]

def vertical_image_bounds_tuple(image):
    topMost = 1000
    bottomMost = 0
    i = 0
    for line in image:
        for char in line:
            if(char == "#" or char == "+"):
                if(i > bottomMost):
                    bottomMost = i
                if(i < topMost):
                    topMost = i
        i += 1
    return [topMost, bottomMost]




def horizontal_image_bounds(image):
    leftMost = 1000
    rightMost = 0
    j = 0
    for line in image:
        for char in line:
            if(char == "#" or char == "+"):
                if(j > rightMost):
                    rightMost = j
                if(j < leftMost):
                    leftMost = j
            j += 1
        j = 0
    return int((leftMost + rightMost) / 2)

def vertical_image_bounds(image):
    topMost = 1000
    bottomMost = 0
    i = 0
    for line in image:
        for char in line:
            if(char == "#" or char == "+"):
                if(i > bottomMost):
                    bottomMost = i
                if(i < topMost):
                    topMost = i
        i += 1
    return int((topMost + bottomMost) / 2)

def pixel_density_block_1(matrix, image_no):
    return_value = split(matrix, image_no, 1)
    rightBound = return_value[1][1]
    leftBound = return_value[1][0]
    topBound = return_value[0][0]
    bottomBound = return_value[0][1]
    if(matrix == faceMatrices):
        r1 = [0, 17]
        c1 = [0, 19]
    else:
        r1 = [0, 6]
        c1 = [0, 9]
    r1 = [leftBound, rightBound]
    c1 = [topBound, bottomBound]
    return normalized_value(calculate_pixel_density(r1, c1, matrix, image_no))

def pixel_density_block_2(matrix, image_no):
    return_value = split(matrix, image_no, 2)
    rightBound = return_value[1][1]
    leftBound = return_value[1][0]
    topBound = return_value[0][0]
    bottomBound = return_value[0][1]
    if(matrix == faceMatrices):
        r1 = [0, 17]
        c2 = [20, 39]
    else:
        r1 = [0, 6]
        c2 = [10, 19]
    r1 = [leftBound, rightBound]
    c2 = [topBound, bottomBound]
    return normalized_value(calculate_pixel_density(r1, c2, matrix, image_no))

def pixel_density_block_3(matrix, image_no):
    return_value = split(matrix, image_no, 3)
    rightBound = return_value[1][1]
    leftBound = return_value[1][0]
    topBound = return_value[0][0]
    bottomBound = return_value[0][1]
    if(matrix == faceMatrices):
        r1 = [0, 17]
        c3 = [40, 60]
    else:
        r1 = [0, 6]
        c3 = [20, 28]
    r1 = [leftBound, rightBound]
    c3 = [topBound, bottomBound]
    return normalized_value(calculate_pixel_density(r1, c3, matrix, image_no))

def pixel_density_block_4(matrix, image_no):
    return_value = split(matrix, image_no, 4)
    rightBound = return_value[1][1]
    leftBound = return_value[1][0]
    topBound = return_value[0][0]
    bottomBound = return_value[0][1]
    if(matrix == faceMatrices):
        r2 = [18, 34]
        c1 = [0, 19]
    else:
        r2 = [7, 13]
        c1 = [0, 9]
    r2 = [leftBound, rightBound]
    c1 = [topBound, bottomBound]
    return normalized_value(calculate_pixel_density(r2, c1, matrix, image_no))

def pixel_density_block_5(matrix, image_no):
    return_value = split(matrix, image_no, 5)
    rightBound = return_value[1][1]
    leftBound = return_value[1][0]
    topBound = return_value[0][0]
    bottomBound = return_value[0][1]
    if(matrix == faceMatrices):
        r2 = [18, 34]
        c2 = [20, 39]
    else:
        r2 = [7, 13]
        c2 = [10, 19]
    r2 = [leftBound, rightBound]
    c2 = [topBound, bottomBound]
    return normalized_value(calculate_pixel_density(r2, c2, matrix, image_no))

def pixel_density_block_6(matrix, image_no):
    return_value = split(matrix, image_no, 6)
    rightBound = return_value[1][1]
    leftBound = return_value[1][0]
    topBound = return_value[0][0]
    bottomBound = return_value[0][1]
    if(matrix == faceMatrices):
        r2 = [18, 34]
        c3 = [40, 60]
    else:
        r2 = [7, 13]
        c3 = [20, 28]
    r2 = [leftBound, rightBound]
    c3 = [topBound, bottomBound]
    return normalized_value(calculate_pixel_density(r2, c3, matrix, image_no))

def pixel_density_block_7(matrix, image_no):
    return_value = split(matrix, image_no, 7)
    rightBound = return_value[1][1]
    leftBound = return_value[1][0]
    topBound = return_value[0][0]
    bottomBound = return_value[0][1]
    if(matrix == faceMatrices):
        r3 = [35, 51]
        c1 = [0, 19]
    else:
        r3 = [14, 20]
        c1 = [0, 9]
    r3 = [leftBound, rightBound]
    c1 = [topBound, bottomBound]
    return normalized_value(calculate_pixel_density(r3, c1, matrix, image_no))

def pixel_density_block_8(matrix, image_no):
    return_value = split(matrix, image_no, 8)
    rightBound = return_value[1][1]
    leftBound = return_value[1][0]
    topBound = return_value[0][0]
    bottomBound = return_value[0][1]
    if(matrix == faceMatrices):
        r3 = [35, 51]
        c2 = [20, 39]
    else:
        r3 = [14, 20]
        c2 = [10, 19]
    r3 = [leftBound, rightBound]
    c2 = [topBound, bottomBound]
    return normalized_value(calculate_pixel_density(r3, c2, matrix, image_no))

def pixel_density_block_9(matrix, image_no):
    return_value = split(matrix, image_no, 9)
    rightBound = return_value[1][1]
    leftBound = return_value[1][0]
    topBound = return_value[0][0]
    bottomBound = return_value[0][1]
    if(matrix == faceMatrices):
        r3 = [35, 51]
        c3 = [40, 60]
    else:
        r3 = [14, 20]
        c3 = [20, 28]
    r3 = [leftBound, rightBound]
    c3 = [topBound, bottomBound]
    return normalized_value(calculate_pixel_density(r3, c3, matrix, image_no))

def pixel_density_block_10(matrix, image_no):
    return_value = split(matrix, image_no, 10)
    rightBound = return_value[1][1]
    leftBound = return_value[1][0]
    topBound = return_value[0][0]
    bottomBound = return_value[0][1]
    if(matrix == faceMatrices):
        r4 = [52, 69]
        c1 = [0, 19]
    else:
        r4 = [21, 27]
        c1 = [0, 9]
    r4 = [leftBound, rightBound]
    c1 = [topBound, bottomBound]
    return normalized_value(calculate_pixel_density(r4, c1, matrix, image_no))

def pixel_density_block_11(matrix, image_no):
    return_value = split(matrix, image_no, 11)
    rightBound = return_value[1][1]
    leftBound = return_value[1][0]
    topBound = return_value[0][0]
    bottomBound = return_value[0][1]
    if(matrix == faceMatrices):
        r4 = [52, 69]
        c2 = [20, 39]
    else:
        r4 = [21, 27]
        c2 = [10, 19]
    r4= [leftBound, rightBound]
    c2 = [topBound, bottomBound]
    return normalized_value(calculate_pixel_density(r4, c2, matrix, image_no))

def pixel_density_block_12(matrix, image_no):
    return_value = split(matrix, image_no, 12)
    rightBound = return_value[1][1]
    leftBound = return_value[1][0]
    topBound = return_value[0][0]
    bottomBound = return_value[0][1]
    if(matrix == faceMatrices):
        r4 = [52, 69]
        c3 = [40, 60]
    else:
        r4 = [21, 27]
        c3 = [20, 28]
    r4 = [leftBound, rightBound]
    c3 = [topBound, bottomBound]
    return normalized_value(calculate_pixel_density(r4, c3, matrix, image_no))

def vertical_lines(matrix, image_no):
    image = matrix[image_no]
    rotated = [list(reversed(col)) for col in zip(*image)]
    counter = 0
    spaces = 0
    lines = []
    for line in rotated:
        if(counter > 6):
            lines.append(1)
        else:
            lines.append(0)
        counter = 0
        spaces = 0
        for char in line:
            if(char == "+" or char == "#"):
                if(spaces > 0):
                    counter = 0
                    spaces = 0
                counter += 1
            else:
                spaces += 1
    count = 0
    value = 0
    for num in lines:
        if(num == 1):
            count += 1
        else:
            if(count > 1):
                value += 1
            count = 0
    return value


def horizontal_lines(matrix, image_no):
    image = matrix[image_no]
    counter = 0
    spaces = 0
    lines = []
    for line in image:
        if(counter > 6):
            lines.append(1)
        else:
            lines.append(0)
        counter = 0
        spaces = 0
        for char in line:
            if(char == "+" or char == "#"):
                if(spaces > 0):
                    counter = 0
                    spaces = 0
                counter += 1
            else:
                spaces += 1
    count = 0
    value = 0
    for num in lines:
        if(num == 1):
            count += 1
        else:
            if(count > 1):
                value += 1
            count = 0
    return value


def loop(matrix, image_no):
    image = matrix[image_no]
    lines = []
    topLines = 0
    spaces = 0
    for line in image:
        start = False
        end = False
        counter = 0
        topLines = 0
        spaces = 0
        for char in line:
            if(char == "+" or char == "#"):
                if(spaces > 0):
                    topLines = 0
                    spaces = 0
                topLines += 1
                if(not start):
                    start = True
                else:
                    if(not end and counter > 1):
                        end = True
                        break
            elif(start and char == " "):
                counter += 1
                spaces += 1

        if(topLines > 6):
            lines.append(-1)
        elif(not end):
            lines.append(0)
            counter = 0
        else:
            lines.append(1)
    loopCounter = 0
    topLine = False
    bottomLine = False
    emptySpace = False
    for num in lines:
        if(num == -1 and topLine == False):
            topLine = True
        elif(num == 1):
            emptySpace = True
        elif(num == -1 and topLine == True and emptySpace == True):
            bottomLine = True
        elif(num == 0):
            topLine = False
            emptySpace = False
            bottomLine = False
        if(topLine and emptySpace and bottomLine):
            topLine = False
            emptySpace = False
            bottomLine = False
            loopCounter += 1
    return loopCounter

def vertical_direction_skew(matrix, image_no):
    bottom = 0
    top = 0
    middleIndex = vertical_image_bounds(matrix[image_no])
    i = 0
    j = 0
    for line in matrix[image_no]:
        for _ in line:
            char = matrix[image_no][i][j]
            if(i <= middleIndex and (char == "#" or char == "+")):
                top += 1
            elif(i > middleIndex and (char == "#" or char == "+")):
                bottom += 1
            j += 1
        i += 1
        j = 0

    if(abs(top - bottom) <= 5):
        return -1
    elif(top > bottom):
        return 1
    elif(bottom > top):
        return 0


def symmetrical(matrix, image_no):
    left = 0
    right = 0
    middleIndex = horizontal_image_bounds(matrix[image_no])
    j = 0
    for line in matrix[image_no]:
        for char in line:
            if(j <= middleIndex and (char == "#" or char == "+")):
                left += 1
            elif(j > middleIndex and (char == "#" or char == "+")):
                right += 1
            j += 1
        j = 0

    if(abs(right - left) <= 50):
        return 1
    else:
        return 0


def horizontal_direction_skew(matrix, image_no):
    left = 0
    right = 0
    middleIndex = horizontal_image_bounds(matrix[image_no])
    i = 0
    j = 0
    for line in matrix[image_no]:
        for _ in line:
            char = matrix[image_no][i][j]
            if(j <= middleIndex and (char == "#" or char == "+")):
                left += 1
            elif(j > middleIndex and (char == "#" or char == "+")):
                right += 1
            j += 1
        i += 1
        j = 0

    if(abs(right - left) <= 5):
        return -1
    elif(right > left):
        return 1
    elif(left > right):
        return 0

#array of all feature functions
digit_function_arr = [pixel_density_block_1, pixel_density_block_2, pixel_density_block_3, pixel_density_block_4, pixel_density_block_5, pixel_density_block_6, pixel_density_block_7, pixel_density_block_8, pixel_density_block_9, pixel_density_block_10, pixel_density_block_11, pixel_density_block_12, horizontal_lines, vertical_lines, loop, horizontal_direction_skew, vertical_direction_skew]
face_function_arr = [pixel_density_block_1, pixel_density_block_2, pixel_density_block_3, pixel_density_block_4, pixel_density_block_5, pixel_density_block_6, pixel_density_block_7, pixel_density_block_8, pixel_density_block_9, pixel_density_block_10, pixel_density_block_11, pixel_density_block_12, symmetrical]
