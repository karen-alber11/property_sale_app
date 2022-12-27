from Environmental_Variables import *


#Function that normalizes the continued values to discrete values
def Normalized_Value(value):
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

#####################################################################################################

#Function that tests whether the matrix either face matrix or digit matrix
def Calculate_Pixel_Density(row_range, column_range, mtrx, image_no):
    # --row_range and --column_range are queues that have start and end indices both inclusive
    # --image_no is the image you are reading from the input file that needs to go through matrix

    total_pixels = (row_range[1] - row_range[0] + 1)*(column_range[1] - column_range[0] + 1)
    colored_pixels = 0

    for i in range(column_range[0], column_range[1] + 1):
        for k in range(row_range[0], row_range[1]+1):
            if(mtrx[image_no][i][k].isspace() is False):
                colored_pixels = colored_pixels + 1
    if(total_pixels == 0):
        total_pixels = 1
    freq = colored_pixels/total_pixels
    return freq

#####################################################################################################

def Split(mtrx, img_no, block_no):
    [topMost, bottomMost] = Vertical_Image_Bounds_Tuple(mtrx[img_no])
    [leftMost, rightMost] = Horizontal_Image_Bounds_Tuple(mtrx[img_no])

    # columns splitting
    column_split_length = int((abs(rightMost - leftMost) + 1)/3)
    remainder = (abs(rightMost - leftMost) + 1)%3

    c1 = [leftMost, leftMost + column_split_length - 1]
    c2 = [c1[1] + 1, c1[1] + 1 + column_split_length - 1]
    c3 = [c2[1] + 1, rightMost]

    # rows splitting
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

#####################################################################################################

#                                         < Horizontal Image >

def Horizontal_Image_Bounds_Tuple(img):
    leftMost = 1000
    rightMost = 0
    j = 0
    for line in img:
        for char in line:
            if(char == "#" or char == "+"):
                if(j > rightMost):
                    rightMost = j
                if(j < leftMost):
                    leftMost = j
            j += 1
        j = 0
    return [leftMost, rightMost]


def Horizontal_Image_Bounds(img):
    leftMost = 1000
    rightMost = 0
    j = 0
    for line in img:
        for char in line:
            if(char == "#" or char == "+"):
                if(j > rightMost):
                    rightMost = j
                if(j < leftMost):
                    leftMost = j
            j += 1
        j = 0
    return int((leftMost + rightMost) / 2)

#####################################################################################################

#                                         < Vertical Image >

def Vertical_Image_Bounds_Tuple(img):
    topMost = 1000
    bottomMost = 0
    i = 0
    for line in img:
        for char in line:
            if(char == "#" or char == "+"):
                if(i > bottomMost):
                    bottomMost = i
                if(i < topMost):
                    topMost = i
        i += 1
    return [topMost, bottomMost]


def Vertical_Image_Bounds(img):
    topMost = 1000
    bottomMost = 0
    i = 0
    for line in img:
        for char in line:
            if(char == "#" or char == "+"):
                if(i > bottomMost):
                    bottomMost = i
                if(i < topMost):
                    topMost = i
        i += 1
    return int((topMost + bottomMost) / 2)

#####################################################################################################

#                                         < Pixel Density Blocks [1-12] >

def Pixel_Density_Block_1(mtrx, img_no):
    value = Split(mtrx, img_no, 1)
    rightBound = value[1][1]
    leftBound = value[1][0]
    topBound = value[0][0]
    bottomBound = value[0][1]
    if(mtrx == face_mtrcs):
        r1 = [0, 17]
        c1 = [0, 19]
    else:
        r1 = [0, 6]
        c1 = [0, 9]
    r1 = [leftBound, rightBound]
    c1 = [topBound, bottomBound]
    return Normalized_Value(Calculate_Pixel_Density(r1, c1, mtrx, img_no))

def Pixel_Density_Block_2(mtrx, img_no):
    value = Split(mtrx, img_no, 2)
    rightBound = value[1][1]
    leftBound = value[1][0]
    topBound = value[0][0]
    bottomBound = value[0][1]
    if(mtrx == face_mtrcs):
        r1 = [0, 17]
        c2 = [20, 39]
    else:
        r1 = [0, 6]
        c2 = [10, 19]
    r1 = [leftBound, rightBound]
    c2 = [topBound, bottomBound]
    return Normalized_Value(Calculate_Pixel_Density(r1, c2, mtrx, img_no))

def Pixel_Density_Block_3(mtrx, img_no):
    value = Split(mtrx, img_no, 3)
    rightBound = value[1][1]
    leftBound = value[1][0]
    topBound = value[0][0]
    bottomBound = value[0][1]
    if(mtrx == face_mtrcs):
        r1 = [0, 17]
        c3 = [40, 60]
    else:
        r1 = [0, 6]
        c3 = [20, 28]
    r1 = [leftBound, rightBound]
    c3 = [topBound, bottomBound]
    return Normalized_Value(Calculate_Pixel_Density(r1, c3, mtrx, img_no))

def Pixel_Density_Block_4(mtrx, img_no):
    value = Split(mtrx, img_no, 4)
    rightBound = value[1][1]
    leftBound = value[1][0]
    topBound = value[0][0]
    bottomBound = value[0][1]
    if(mtrx == face_mtrcs):
        r2 = [18, 34]
        c1 = [0, 19]
    else:
        r2 = [7, 13]
        c1 = [0, 9]
    r2 = [leftBound, rightBound]
    c1 = [topBound, bottomBound]
    return Normalized_Value(Calculate_Pixel_Density(r2, c1, mtrx, img_no))

def Pixel_Density_Block_5(mtrx, img_no):
    value = Split(mtrx, img_no, 5)
    rightBound = value[1][1]
    leftBound = value[1][0]
    topBound = value[0][0]
    bottomBound = value[0][1]
    if(mtrx == face_mtrcs):
        r2 = [18, 34]
        c2 = [20, 39]
    else:
        r2 = [7, 13]
        c2 = [10, 19]
    r2 = [leftBound, rightBound]
    c2 = [topBound, bottomBound]
    return Normalized_Value(Calculate_Pixel_Density(r2, c2, mtrx, img_no))

def Pixel_Density_Block_6(mtrx, img_no):
    value = Split(mtrx, img_no, 6)
    rightBound = value[1][1]
    leftBound = value[1][0]
    topBound = value[0][0]
    bottomBound = value[0][1]
    if(mtrx == face_mtrcs):
        r2 = [18, 34]
        c3 = [40, 60]
    else:
        r2 = [7, 13]
        c3 = [20, 28]
    r2 = [leftBound, rightBound]
    c3 = [topBound, bottomBound]
    return Normalized_Value(Calculate_Pixel_Density(r2, c3, mtrx, img_no))

def Pixel_Density_Block_7(mtrx, img_no):
    value = Split(mtrx, img_no, 7)
    rightBound = value[1][1]
    leftBound = value[1][0]
    topBound = value[0][0]
    bottomBound = value[0][1]
    if(mtrx == face_mtrcs):
        r3 = [35, 51]
        c1 = [0, 19]
    else:
        r3 = [14, 20]
        c1 = [0, 9]
    r3 = [leftBound, rightBound]
    c1 = [topBound, bottomBound]
    return Normalized_Value(Calculate_Pixel_Density(r3, c1, mtrx, img_no))

def Pixel_Density_Block_8(mtrx, img_no):
    value = Split(mtrx, img_no, 8)
    rightBound = value[1][1]
    leftBound = value[1][0]
    topBound = value[0][0]
    bottomBound = value[0][1]
    if(mtrx == face_mtrcs):
        r3 = [35, 51]
        c2 = [20, 39]
    else:
        r3 = [14, 20]
        c2 = [10, 19]
    r3 = [leftBound, rightBound]
    c2 = [topBound, bottomBound]
    return Normalized_Value(Calculate_Pixel_Density(r3, c2, mtrx, img_no))

def Pixel_Density_Block_9(mtrx, img_no):
    value = Split(mtrx, img_no, 9)
    rightBound = value[1][1]
    leftBound = value[1][0]
    topBound = value[0][0]
    bottomBound = value[0][1]
    if(mtrx == face_mtrcs):
        r3 = [35, 51]
        c3 = [40, 60]
    else:
        r3 = [14, 20]
        c3 = [20, 28]
    r3 = [leftBound, rightBound]
    c3 = [topBound, bottomBound]
    return Normalized_Value(Calculate_Pixel_Density(r3, c3, mtrx, img_no))

def Pixel_Density_Block_10(mtrx, img_no):
    value = Split(mtrx, img_no, 10)
    rightBound = value[1][1]
    leftBound = value[1][0]
    topBound = value[0][0]
    bottomBound = value[0][1]
    if(mtrx == face_mtrcs):
        r4 = [52, 69]
        c1 = [0, 19]
    else:
        r4 = [21, 27]
        c1 = [0, 9]
    r4 = [leftBound, rightBound]
    c1 = [topBound, bottomBound]
    return Normalized_Value(Calculate_Pixel_Density(r4, c1, mtrx, img_no))

def Pixel_Density_Block_11(mtrx, img_no):
    value = Split(mtrx, img_no, 11)
    rightBound = value[1][1]
    leftBound = value[1][0]
    topBound = value[0][0]
    bottomBound = value[0][1]
    if(mtrx == face_mtrcs):
        r4 = [52, 69]
        c2 = [20, 39]
    else:
        r4 = [21, 27]
        c2 = [10, 19]
    r4= [leftBound, rightBound]
    c2 = [topBound, bottomBound]
    return Normalized_Value(Calculate_Pixel_Density(r4, c2, mtrx, img_no))

def Pixel_Density_Block_12(mtrx, img_no):
    value = Split(mtrx, img_no, 12)
    rightBound = value[1][1]
    leftBound = value[1][0]
    topBound = value[0][0]
    bottomBound = value[0][1]
    if(mtrx == face_mtrcs):
        r4 = [52, 69]
        c3 = [40, 60]
    else:
        r4 = [21, 27]
        c3 = [20, 28]
    r4 = [leftBound, rightBound]
    c3 = [topBound, bottomBound]
    return Normalized_Value(Calculate_Pixel_Density(r4, c3, mtrx, img_no))

#####################################################################################################

#                                         < Lines Direction >

def Vertical_Lines(mtrx, img_no):
    image = mtrx[img_no]
    rotated = [list(reversed(column)) for column in zip(*image)]
    count = 0
    spaces = 0
    lines = []
    for line in rotated:
        if(count > 6):
            lines.append(1)
        else:
            lines.append(0)
        count = 0
        spaces = 0
        for char in line:
            if(char == "+" or char == "#"):
                if(spaces > 0):
                    count = 0
                    spaces = 0
                count += 1
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


def Horizontal_Lines(mtrx, img_no):
    image = mtrx[img_no]
    count = 0
    spaces = 0
    lines = []
    for line in image:
        if(count > 6):
            lines.append(1)
        else:
            lines.append(0)
        count = 0
        spaces = 0
        for char in line:
            if(char == "+" or char == "#"):
                if(spaces > 0):
                    count = 0
                    spaces = 0
                count += 1
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


def Loop(mtrx, img_no):
    image = mtrx[img_no]
    lines = []
    topLines = 0
    spaces = 0
    for line in image:
        begin = False
        end = False
        count = 0
        topLines = 0
        spaces = 0
        for char in line:
            if(char == "+" or char == "#"):
                if(spaces > 0):
                    topLines = 0
                    spaces = 0
                topLines += 1
                if(not begin):
                    begin = True
                else:
                    if(not end and count > 1):
                        end = True
                        break
            elif(begin and char == " "):
                count += 1
                spaces += 1

        if(topLines > 6):
            lines.append(-1)
        elif(not end):
            lines.append(0)
            count = 0
        else:
            lines.append(1)
    countLoop = 0
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
            countLoop += 1
    return countLoop

#####################################################################################################

#                                         < Skew Direction >

def Vertical_Skew_Direction(mtrx, img_no):
    bottom = 0
    top = 0
    middleIndex = Vertical_Image_Bounds(mtrx[img_no])
    i = 0
    j = 0
    for line in mtrx[img_no]:
        for _ in line:
            char = mtrx[img_no][i][j]
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


def Symmetrical(mtrx, img_no):
    left = 0
    right = 0
    middleIndex = Horizontal_Image_Bounds(mtrx[img_no])
    j = 0
    for line in mtrx[img_no]:
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


def Horizontal_Skew_Direction(mtrx, img_no):
    left = 0
    right = 0
    middleIndex = Horizontal_Image_Bounds(mtrx[img_no])
    i = 0
    j = 0
    for line in mtrx[img_no]:
        for _ in line:
            char = mtrx[img_no][i][j]
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

###################################################################################################

# Digit array of all properties functions
digit_array = [Pixel_Density_Block_1, Pixel_Density_Block_2, Pixel_Density_Block_3, Pixel_Density_Block_4, Pixel_Density_Block_5, Pixel_Density_Block_6, Pixel_Density_Block_7, Pixel_Density_Block_8, Pixel_Density_Block_9, Pixel_Density_Block_10, Pixel_Density_Block_11, Pixel_Density_Block_12, Horizontal_Lines, Vertical_Lines, Loop, Horizontal_Skew_Direction, Vertical_Skew_Direction]

# Face array of all properties functions
face_array = [Pixel_Density_Block_1, Pixel_Density_Block_2, Pixel_Density_Block_3, Pixel_Density_Block_4, Pixel_Density_Block_5, Pixel_Density_Block_6, Pixel_Density_Block_7, Pixel_Density_Block_8, Pixel_Density_Block_9, Pixel_Density_Block_10, Pixel_Density_Block_11, Pixel_Density_Block_12, Symmetrical]

####################################################################################################
