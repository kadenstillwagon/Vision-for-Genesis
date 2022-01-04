from PIL import Image, ImageDraw
from matplotlib import image
from matplotlib import pyplot
#PIL = Python Image Library
#https://www.oreilly.com/library/view/programming-computer-vision/9781449341916/ch01.html


# Need to create different neurons that learn different things: edges, corners, straight lines, curves, circles, etc.






color1 = (0, 0, 0)  #black
color2 = (255, 255, 255)  #white
color3 = (255, 0, 0)  #red
color4 = (0, 255, 0)  #lime green
color5 = (0, 0, 255)  #blue
color6 = (255, 255, 0)  #yellow
color7 = (0, 255, 255)  #cyan
color8 = (255, 0, 255)  #magenta
color9 = (255, 140, 0)  #orange
color10 = (0, 100, 0)  #dark green
color11 = (0, 0, 139)  #dark blue
color12 = (128, 0, 128)  #purple
color13 = (139, 69, 19)  #brown
color14 = (135, 206, 250)  #light blue
color15 = (128, 128, 128)  #gray

Colors = [color1, color2, color3, color4, color5, color6, color7, color8, color9, color10, color11, color12, color13, color14, color15]


pixelsArray = []

def getXcord(pixelNum):
    xCord = pixelsArray[pixelNum][0][0]
    return xCord

def getYcord(pixelNum):
    yCord = pixelsArray[pixelNum][0][1]
    return yCord

def getGrayscale(pixelNum):
    grayscale = pixelsArray[pixelNum][1]
    return grayscale

def getColor1(pixelNum):
    red = pixelsArray[pixelNum][1][0]
    return red

def getColor2(pixelNum):
    green = pixelsArray[pixelNum][1][1]
    return green

def getColor3(pixelNum):
    blue = pixelsArray[pixelNum][1][2]
    return blue



def grayPixelData(pixels, xsize, ysize):
    for yval in range(0, ysize):
        y = yval
        for xval in range(0, xsize):
            # pixelNum += 1
            x = xval
            data = []
            data.append([x,y])
            data.append(pixels[x,y]) #pixels[x,y] gives the RGB or grayscale value for that pixel
            pixelsArray.append(data)
            # print("Grayscale: " + str(pixels[x,y]) + "  Coordinates: (" + str(x) + ", " + str(y) + ")")
    return pixelsArray

def colorPixelData(pixels, xsize, ysize):
    for yval in range(0, ysize):
        y = yval
        for xval in range(0, xsize):
            # pixelNum += 1
            x = xval
            data = []
            data.append([x,y])
            rgbCode = []
            rgbCode.append(pixels[x, y][0])
            rgbCode.append(pixels[x, y][1])
            rgbCode.append(pixels[x, y][2])
            data.append(rgbCode)
            pixelsArray.append(data)
            # print("Grayscale: " + str(pixels[x,y]) + "  Coordinates: (" + str(x) + ", " + str(y) + ")")
    return pixelsArray








def grayScaleReading(pixelsArray, xsize, ysize, pixels):
    borders = []
    pixelDict = {}
    pixelNumber = 0
    for pixel in pixelsArray:
        border = False
        X = getXcord(pixelNumber)
        Y = getYcord(pixelNumber)
        GS = getGrayscale(pixelNumber)
        if X < xsize - 1:
            GSr = getGrayscale(pixelNumber + ysize)
            difference = abs(GS - GSr)
            if difference > 35:  # IDEA: Create a function that finds how many colors in an image and uses to determine how the degree of difference needed to be a border
                border = True
        if Y < ysize - 1:
            GSd = getGrayscale(pixelNumber + 1)
            difference = abs(GS - GSd)
            if difference > 35:
                border = True
        coordinates = ()
        if border == True:
            # print("BORDER: (" + str(X) + ", " + str(Y) + ")")
            pixels[X, Y] = 1
            coordinates = (X, Y)
            borders.append(coordinates)
            pixelDict[coordinates] = True
        else:
            pixels[X, Y] = 255
            coordinates = (X, Y)
            pixelDict[coordinates] = False

        pixelNumber += 1

    return borders, pixelDict


# def colorScaleReading(pixelsArray, xsize, ysize, pixels):
#     borders = []
#     pixelDict = {}
#     pixelNumber = 0
#     for pixel in pixelsArray:
#         border = False
#         X = getXcord(pixelNumber)
#         Y = getYcord(pixelNumber)
#         RED = getColor1(pixelNumber)
#         GREEN = getColor2(pixelNumber)
#         BLUE = getColor3(pixelNumber)
#
#         overallColor = RED + GREEN + BLUE
#
#         if X < xsize - 1:
#             REDr = getColor1(pixelNumber + 1)
#             GREENr = getColor2(pixelNumber + 1)
#             BLUEr = getColor3(pixelNumber + 1)
#             overallColorR = REDr + GREENr + BLUEr
#             rDif = abs(RED - REDr)
#             gDif = abs(GREEN - GREENr)
#             bDif = abs(BLUE - BLUEr)
#             difference = abs(overallColor - overallColorR)
#             if difference > 150:  # IDEA: Create a function that finds how many colors in an image and uses to determine how the degree of difference needed to be a border
#                 border = True
#             if rDif > 25 and gDif > 25 and bDif > 25:
#                 border = True
#         if Y < ysize - 1:
#             REDd = getColor1(pixelNumber + xsize)
#             GREENd = getColor2(pixelNumber + xsize)
#             BLUEd = getColor3(pixelNumber + xsize)
#             overallColorD = REDd + GREENd + BLUEd
#
#             rDif = abs(RED - REDd)
#             gDif = abs(GREEN - GREENd)
#             bDif = abs(BLUE - BLUEd)
#
#             difference = abs(overallColor - overallColorD)
#             if difference > 150:
#                 border = True
#             if rDif > 25 and gDif > 25 and bDif > 25:
#                 border = True
#         coordinates = ()
#         if border == True:
#             pixels[X, Y] = (1, 1, 1) # Makes all border pixels black
#             coordinates = (X, Y)
#             borders.append(coordinates)
#             pixelDict[coordinates] = True
#         else:
#             pixels[X, Y] = (255, 255, 255) #Makes all non border pixels white
#             coordinates = (X, Y)
#             pixelDict[coordinates] = False
#
#         pixelNumber += 1
#
#     return borders, pixelDict





def colorObjectSeperation(pixelsArray, pixels):
    borders = []
    pixelDict = {}
    pixelNumber = 0

    group1 = []
    group2 = []
    group3 = []
    group4 = []
    group5 = []
    group6 = []
    group7 = []
    group8 = []
    group9 = []
    group10 = []
    group11 = []
    group12 = []
    group13 = []
    group14 = []
    group15 = []
    group16 = []
    group17 = []
    group18 = []
    group19 = []
    group20 = []
    group21 = []
    group22 = []
    group23 = []
    group24 = []
    group25 = []
    group26 = []
    group27 = []
    group28 = []
    group29 = []
    group30 = []
    group31 = []
    group32 = []
    group33 = []
    group34 = []
    group35 = []
    group36 = []
    group37 = []
    group38 = []
    group39 = []
    group40 = []
    Groups =[[group1, (300, 300, 300)], [group2, (300, 300, 300)], [group3, (300, 300, 300)], [group4, (300, 300, 300)], [group5, (300, 300, 300)], [group6, (300, 300, 300)], [group7, (300, 300, 300)], [group8, (300, 300, 300)], [group9, (300, 300, 300)], [group10, (300, 300, 300)], [group11, (300, 300, 300)], [group12, (300, 300, 300)], [group13, (300, 300, 300)], [group14, (300, 300, 300)], [group15, (300, 300, 300)], [group16, (300, 300, 300)], [group17, (300, 300, 300)], [group18, (300, 300, 300)], [group19, (300, 300, 300)], [group20, (300, 300, 300)], [group21, (300, 300, 300)], [group22, (300, 300, 300)], [group23, (300, 300, 300)], [group24, (300, 300, 300)], [group25, (300, 300, 300)], [group26, (300, 300, 300)], [group27, (300, 300, 300)], [group28, (300, 300, 300)], [group29, (300, 300, 300)], [group30, (300, 300, 300)], [group31, (300, 300, 300)], [group32, (300, 300, 300)], [group33, (300, 300, 300)], [group34, (300, 300, 300)], [group35, (300, 300, 300)], [group36, (300, 300, 300)], [group37, (300, 300, 300)], [group38, (300, 300, 300)], [group39, (300, 300, 300)], [group40, (300, 300, 300)]]
    createdGroups = [group1]

    pixelGroupDict = {}

    totalGroups = 0

    firstRun = True
    for num in range(0, 2):
        for pixel in pixelsArray:
            X = getXcord(pixelNumber)
            Y = getYcord(pixelNumber)
            coordinates = (X, Y)

            RED = getColor1(pixelNumber)
            GREEN = getColor2(pixelNumber)
            BLUE = getColor3(pixelNumber)

            rgbCode = (RED, GREEN, BLUE)

            overallColor = RED + GREEN + BLUE

            if firstRun == True:
                Groups[0][1] = rgbCode
                Groups[0][0].append(coordinates)
                pixelGroupDict[coordinates] = 0


            if firstRun == False:
                groupCount = 0
                groupFits = 0
                options = []

                for group in createdGroups:
                    diffR = abs(RED - Groups[groupCount][1][0])
                    diffG = abs(GREEN - Groups[groupCount][1][1])
                    diffB = abs(BLUE - Groups[groupCount][1][2])
                    totalDiff = diffR + diffG + diffB

                    if (diffR < 90 and diffG < 90 and diffB < 90): #IDEA: refactor the groups rgb codes when a new entity is added
                        options.append((groupCount, totalDiff))
                        groupFits += 1
                    groupCount += 1

                if groupFits > 1:
                    bestDiff = 800
                    groupNumber = 0
                    for option in options:
                        if option[1] < bestDiff:
                            bestDiff = option[1]
                            groupNumber = option[0]

                    Groups[groupNumber][0].append(coordinates)
                    pixels[X, Y] = Groups[groupNumber][1]
                    pixelGroupDict[coordinates] = groupNumber

                if groupFits == 1:
                    groupNumber = options[0][0]
                    Groups[groupNumber][0].append(coordinates)
                    pixels[X, Y] = Groups[groupNumber][1]
                    pixelGroupDict[coordinates] = groupNumber

                if groupFits == 0:
                    totalGroups += 1
                    print("Pixel: " + str(pixelNumber) + "  Total Groups: " + str(totalGroups+1))
                    Groups[totalGroups][0].append(coordinates)
                    Groups[totalGroups][1] = rgbCode
                    createdGroups.append(Groups[totalGroups][0])
                    pixels[X, Y] = Groups[totalGroups][1]
                    pixelGroupDict[coordinates] = totalGroups

            firstRun = False
            pixelNumber += 1

        if num == 0:
            for group in Groups:
                group[0] = []
                pixelGroupDict = {}
                pixelNumber = 0


    groupNum = 0
    groups = len(Groups)
    for group in range(0, groups):
        if Groups[groupNum][1] == (300, 300, 300):
            Groups.pop(groupNum)
            groupNum -= 1
        groupNum += 1



    return Groups, pixelGroupDict


# # Testing with refactoring algorithm
#
# def refactoringColorObjectSeperation(pixelsArray, pixels):
#     borders = []
#     pixelDict = {}
#     pixelNumber = 0
#     currentGroup = 0
#
#     group1 = []
#     group2 = []
#     group3 = []
#     group4 = []
#     group5 = []
#     group6 = []
#     group7 = []
#     group8 = []
#     group9 = []
#     group10 = []
#     group11 = []
#     group12 = []
#     group13 = []
#     group14 = []
#     group15 = []
#     Groups =[[group1, (300, 300, 300)], [group2, (300, 300, 300)], [group3, (300, 300, 300)], [group4, (300, 300, 300)], [group5, (300, 300, 300)], [group6, (300, 300, 300)], [group7, (300, 300, 300)], [group8, (300, 300, 300)], [group9, (300, 300, 300)], [group10, (300, 300, 300)], [group11, (300, 300, 300)], [group12, (300, 300, 300)], [group13, (300, 300, 300)], [group14, (300, 300, 300)], [group15, (300, 300, 300)]]
#     createdGroups = [group1]
#
#     totalGroups = 0
#
#     firstRun = True
#
#     for pixel in pixelsArray:
#         X = getXcord(pixelNumber)
#         Y = getYcord(pixelNumber)
#         coordinates = (X, Y)
#
#         RED = getColor1(pixelNumber)
#         GREEN = getColor2(pixelNumber)
#         BLUE = getColor3(pixelNumber)
#
#         rgbCode = (RED, GREEN, BLUE)
#
#         overallColor = RED + GREEN + BLUE
#
#
#
#
#         if firstRun == False:
#             groupCount = 0
#             groupFits = 0
#             options = []
#
#             for group in createdGroups:
#                 diffR = abs(RED - Groups[groupCount][1][0])
#                 diffG = abs(GREEN - Groups[groupCount][1][1])
#                 diffB = abs(BLUE - Groups[groupCount][1][2])
#                 totalDiff = diffR + diffG + diffB
#
#                 if (diffR < 90 and diffG < 90 and diffB < 90): #IDEA: refactor the groups rgb codes when a new entity is added
#                     options.append((groupCount, totalDiff))
#                     groupFits += 1
#                 groupCount += 1
#
#             if groupFits > 1:
#                 bestDiff = 270
#                 group = 0
#                 for option in options:
#                     if option[1] < bestDiff:
#                         bestDiff = option[1]
#                         group = option[0]
#
#                 tuplePlaceholder = list(Groups[group][1])
#                 tuplePlaceholder[0] = Groups[group][1][0] + round((RED - Groups[group][1][0]) / (len(Groups[group][0])))
#                 tuplePlaceholder[1] = Groups[group][1][1] + round((GREEN - Groups[group][1][1]) / (len(Groups[group][0])))
#                 tuplePlaceholder[2] = Groups[group][1][2] + round((BLUE - Groups[group][1][2]) / (len(Groups[group][0])))
#
#                 Groups[group][1] = tuple(tuplePlaceholder)
#
#                 Groups[group][0].append(coordinates)
#                 pixels[X, Y] = Colors[group]
#
#             if groupFits == 1:
#                 group = options[0][0]
#
#                 tuplePlaceholder = list(Groups[group][1])
#                 tuplePlaceholder[0] = Groups[group][1][0] + round((RED - Groups[group][1][0]) / (len(Groups[group][0])))
#                 tuplePlaceholder[1] = Groups[group][1][1] + round((GREEN - Groups[group][1][1]) / (len(Groups[group][0])))
#                 tuplePlaceholder[2] = Groups[group][1][2] + round((BLUE - Groups[group][1][2]) / (len(Groups[group][0])))
#
#                 Groups[group][1] = tuple(tuplePlaceholder)
#
#                 Groups[group][0].append(coordinates)
#                 pixels[X, Y] = Colors[group]
#
#             if groupFits == 0:
#                 totalGroups += 1
#                 print("Pixel: " + str(pixelNumber) + "  Total Groups: " + str(totalGroups))
#                 Groups[totalGroups][0].append(coordinates)
#                 Groups[totalGroups][1] = rgbCode
#                 createdGroups.append(Groups[totalGroups][0])
#                 pixels[X, Y] = Colors[totalGroups]
#
#
#         if firstRun == True:
#             Groups[currentGroup][0].append(coordinates)
#             Groups[0][1] = rgbCode
#
#             firstRun = False
#
#         pixelNumber += 1
#
#
#     return Groups



def objectBorders(Groups, pixelGroupDict, pixels, xsize, ysize):
    borders = []

    for y in range(0, ysize):
        for x in range(0, xsize):

            coordinates = (x, y)

            pixelGroupDict2 = pixelGroupDict

            if x < xsize - 8:
                if pixelGroupDict[(x + 1, y)] != pixelGroupDict[(x, y)]:
                    if pixelGroupDict[(x + 2, y)] != pixelGroupDict[(x, y)]:
                        if pixelGroupDict[(x + 3, y)] != pixelGroupDict[(x, y)]:
                            if pixelGroupDict[(x + 4, y)] != pixelGroupDict[(x, y)]:
                                if pixelGroupDict[(x + 5, y)] != pixelGroupDict[(x, y)]:
                                    if pixelGroupDict[(x + 6, y)] != pixelGroupDict[(x, y)]:
                                        if pixelGroupDict[(x + 7, y)] != pixelGroupDict[(x, y)]:
                                            if pixelGroupDict[(x + 8, y)] != pixelGroupDict[(x, y)]:
                                                borders.append(coordinates)
                                            else:
                                                Groups[pixelGroupDict[x + 1, y]][0].remove((x + 1, y))
                                                Groups[pixelGroupDict[x, y]][0].append((x + 1, y))
                                                pixelGroupDict[(x + 1, y)] = pixelGroupDict[(x, y)]

                                                Groups[pixelGroupDict[x + 2, y]][0].remove((x + 2, y))
                                                Groups[pixelGroupDict[x, y]][0].append((x + 2, y))
                                                pixelGroupDict[(x + 2, y)] = pixelGroupDict[(x, y)]

                                                Groups[pixelGroupDict[x + 3, y]][0].remove((x + 3, y))
                                                Groups[pixelGroupDict[x, y]][0].append((x + 3, y))
                                                pixelGroupDict[(x + 3, y)] = pixelGroupDict[(x, y)]

                                                Groups[pixelGroupDict[x + 4, y]][0].remove((x + 4, y))
                                                Groups[pixelGroupDict[x, y]][0].append((x + 4, y))
                                                pixelGroupDict[(x + 4, y)] = pixelGroupDict[(x, y)]

                                                Groups[pixelGroupDict[x + 5, y]][0].remove((x + 5, y))
                                                Groups[pixelGroupDict[x, y]][0].append((x + 5, y))
                                                pixelGroupDict[(x + 5, y)] = pixelGroupDict[(x, y)]

                                                Groups[pixelGroupDict[x + 6, y]][0].remove((x + 6, y))
                                                Groups[pixelGroupDict[x, y]][0].append((x + 6, y))
                                                pixelGroupDict[(x + 6, y)] = pixelGroupDict[(x, y)]

                                                Groups[pixelGroupDict[x + 7, y]][0].remove((x + 7, y))
                                                Groups[pixelGroupDict[x, y]][0].append((x + 7, y))
                                                pixelGroupDict[(x + 7, y)] = pixelGroupDict[(x, y)]
                                        else:
                                            Groups[pixelGroupDict[x + 1, y]][0].remove((x + 1, y))
                                            Groups[pixelGroupDict[x, y]][0].append((x + 1, y))
                                            pixelGroupDict[(x + 1, y)] = pixelGroupDict[(x, y)]

                                            Groups[pixelGroupDict[x + 2, y]][0].remove((x + 2, y))
                                            Groups[pixelGroupDict[x, y]][0].append((x + 2, y))
                                            pixelGroupDict[(x + 2, y)] = pixelGroupDict[(x, y)]

                                            Groups[pixelGroupDict[x + 3, y]][0].remove((x + 3, y))
                                            Groups[pixelGroupDict[x, y]][0].append((x + 3, y))
                                            pixelGroupDict[(x + 3, y)] = pixelGroupDict[(x, y)]

                                            Groups[pixelGroupDict[x + 4, y]][0].remove((x + 4, y))
                                            Groups[pixelGroupDict[x, y]][0].append((x + 4, y))
                                            pixelGroupDict[(x + 4, y)] = pixelGroupDict[(x, y)]

                                            Groups[pixelGroupDict[x + 5, y]][0].remove((x + 5, y))
                                            Groups[pixelGroupDict[x, y]][0].append((x + 5, y))
                                            pixelGroupDict[(x + 5, y)] = pixelGroupDict[(x, y)]

                                            Groups[pixelGroupDict[x + 6, y]][0].remove((x + 6, y))
                                            Groups[pixelGroupDict[x, y]][0].append((x + 6, y))
                                            pixelGroupDict[(x + 6, y)] = pixelGroupDict[(x, y)]
                                    else:
                                        Groups[pixelGroupDict[x + 1, y]][0].remove((x + 1, y))
                                        Groups[pixelGroupDict[x , y]][0].append((x + 1, y))
                                        pixelGroupDict[(x + 1, y)] = pixelGroupDict[(x, y)]

                                        Groups[pixelGroupDict[x + 2, y]][0].remove((x + 2, y))
                                        Groups[pixelGroupDict[x , y]][0].append((x + 2, y))
                                        pixelGroupDict[(x + 2, y)] = pixelGroupDict[(x, y)]

                                        Groups[pixelGroupDict[x + 3, y]][0].remove((x + 3, y))
                                        Groups[pixelGroupDict[x , y]][0].append((x + 3, y))
                                        pixelGroupDict[(x + 3, y)] = pixelGroupDict[(x, y)]

                                        Groups[pixelGroupDict[x + 4, y]][0].remove((x + 4, y))
                                        Groups[pixelGroupDict[x , y]][0].append((x + 4, y))
                                        pixelGroupDict[(x + 4, y)] = pixelGroupDict[(x, y)]

                                        Groups[pixelGroupDict[x + 5, y]][0].remove((x + 5, y))
                                        Groups[pixelGroupDict[x , y]][0].append((x + 5, y))
                                        pixelGroupDict[(x + 5, y)] = pixelGroupDict[(x, y)]
                                else:
                                    Groups[pixelGroupDict[x + 1, y]][0].remove((x + 1, y))
                                    Groups[pixelGroupDict[x , y]][0].append((x + 1, y))
                                    pixelGroupDict[(x + 1, y)] = pixelGroupDict[(x, y)]

                                    Groups[pixelGroupDict[x + 2, y]][0].remove((x + 2, y))
                                    Groups[pixelGroupDict[x , y]][0].append((x + 2, y))
                                    pixelGroupDict[(x + 2, y)] = pixelGroupDict[(x, y)]

                                    Groups[pixelGroupDict[x + 3, y]][0].remove((x + 3, y))
                                    Groups[pixelGroupDict[x , y]][0].append((x + 3, y))
                                    pixelGroupDict[(x + 3, y)] = pixelGroupDict[(x, y)]

                                    Groups[pixelGroupDict[x + 4, y]][0].remove((x + 4, y))
                                    Groups[pixelGroupDict[x , y]][0].append((x + 4, y))
                                    pixelGroupDict[(x + 4, y)] = pixelGroupDict[(x, y)]
                            else:
                                Groups[pixelGroupDict[x + 1, y]][0].remove((x + 1, y))
                                Groups[pixelGroupDict[x , y]][0].append((x + 1, y))
                                pixelGroupDict[(x + 1, y)] = pixelGroupDict[(x, y)]

                                Groups[pixelGroupDict[x + 2, y]][0].remove((x + 2, y))
                                Groups[pixelGroupDict[x , y]][0].append((x + 2, y))
                                pixelGroupDict[(x + 2, y)] = pixelGroupDict[(x, y)]

                                Groups[pixelGroupDict[x + 3, y]][0].remove((x + 3, y))
                                Groups[pixelGroupDict[x , y]][0].append((x + 3, y))
                                pixelGroupDict[(x + 3, y)] = pixelGroupDict[(x, y)]
                        else:
                            Groups[pixelGroupDict[x + 1, y]][0].remove((x + 1, y))
                            Groups[pixelGroupDict[x , y]][0].append((x + 1, y))
                            pixelGroupDict[(x + 1, y)] = pixelGroupDict[(x, y)]

                            Groups[pixelGroupDict[x + 2, y]][0].remove((x + 2, y))
                            Groups[pixelGroupDict[x , y]][0].append((x + 2, y))
                            pixelGroupDict[(x + 2, y)] = pixelGroupDict[(x, y)]
                    else:
                        Groups[pixelGroupDict[x + 1, y]][0].remove((x + 1, y))
                        Groups[pixelGroupDict[x , y]][0].append((x + 1, y))
                        pixelGroupDict[(x + 1, y)] = pixelGroupDict[(x, y)]

    for y in range(0, ysize):
        for x in range(0, xsize):

            coordinates = (x, y)

            if y < ysize - 8:
                if pixelGroupDict2[(x, y + 1)] != pixelGroupDict2[(x, y)]:
                    if pixelGroupDict2[(x, y + 2)] != pixelGroupDict2[(x, y)]:
                        if pixelGroupDict2[(x, y + 3)] != pixelGroupDict2[(x, y)]:
                            if pixelGroupDict2[(x, y + 4)] != pixelGroupDict2[(x, y)]:
                                if pixelGroupDict2[(x, y + 5)] != pixelGroupDict2[(x, y)]:
                                    if pixelGroupDict2[(x, y + 6)] != pixelGroupDict2[(x, y)]:
                                        if pixelGroupDict2[(x, y + 7)] != pixelGroupDict2[(x, y)]:
                                            if pixelGroupDict2[(x, y + 8)] != pixelGroupDict2[(x, y)]:
                                                borders.append(coordinates)
                                            else:
                                                Groups[pixelGroupDict2[x, y + 1]][0].remove((x, y + 1))
                                                Groups[pixelGroupDict2[x, y]][0].append((x, y + 1))
                                                pixelGroupDict2[(x, y + 1)] = pixelGroupDict2[(x, y)]

                                                Groups[pixelGroupDict2[x, y + 2]][0].remove((x, y + 2))
                                                Groups[pixelGroupDict2[x, y]][0].append((x, y + 2))
                                                pixelGroupDict2[(x, y + 2)] = pixelGroupDict2[(x, y)]

                                                Groups[pixelGroupDict2[x, y + 3]][0].remove((x, y + 3))
                                                Groups[pixelGroupDict2[x, y]][0].append((x, y + 3))
                                                pixelGroupDict2[(x, y + 3)] = pixelGroupDict2[(x, y)]

                                                Groups[pixelGroupDict2[x, y + 4]][0].remove((x, y + 4))
                                                Groups[pixelGroupDict2[x, y]][0].append((x, y + 4))
                                                pixelGroupDict2[(x, y + 4)] = pixelGroupDict2[(x, y)]

                                                Groups[pixelGroupDict2[x, y + 5]][0].remove((x, y + 5))
                                                Groups[pixelGroupDict2[x, y]][0].append((x, y + 5))
                                                pixelGroupDict2[(x, y + 5)] = pixelGroupDict2[(x, y)]

                                                Groups[pixelGroupDict2[x, y + 6]][0].remove((x, y + 6))
                                                Groups[pixelGroupDict2[x, y]][0].append((x, y + 6))
                                                pixelGroupDict2[(x, y + 6)] = pixelGroupDict2[(x, y)]

                                                Groups[pixelGroupDict2[x, y + 7]][0].remove((x, y + 7))
                                                Groups[pixelGroupDict2[x, y]][0].append((x, y + 7))
                                                pixelGroupDict2[(x, y + 7)] = pixelGroupDict2[(x, y)]
                                        else:
                                            Groups[pixelGroupDict2[x, y + 1]][0].remove((x, y + 1))
                                            Groups[pixelGroupDict2[x, y]][0].append((x, y + 1))
                                            pixelGroupDict2[(x, y + 1)] = pixelGroupDict2[(x, y)]

                                            Groups[pixelGroupDict2[x, y + 2]][0].remove((x, y + 2))
                                            Groups[pixelGroupDict2[x, y]][0].append((x, y + 2))
                                            pixelGroupDict2[(x, y + 2)] = pixelGroupDict2[(x, y)]

                                            Groups[pixelGroupDict2[x, y + 3]][0].remove((x, y + 3))
                                            Groups[pixelGroupDict2[x, y]][0].append((x, y + 3))
                                            pixelGroupDict2[(x, y + 3)] = pixelGroupDict2[(x, y)]

                                            Groups[pixelGroupDict2[x, y + 4]][0].remove((x, y + 4))
                                            Groups[pixelGroupDict2[x, y]][0].append((x, y + 4))
                                            pixelGroupDict2[(x, y + 4)] = pixelGroupDict2[(x, y)]

                                            Groups[pixelGroupDict2[x, y + 5]][0].remove((x, y + 5))
                                            Groups[pixelGroupDict2[x, y]][0].append((x, y + 5))
                                            pixelGroupDict2[(x, y + 5)] = pixelGroupDict2[(x, y)]

                                            Groups[pixelGroupDict2[x, y + 6]][0].remove((x, y + 6))
                                            Groups[pixelGroupDict2[x, y]][0].append((x, y + 6))
                                            pixelGroupDict2[(x, y + 6)] = pixelGroupDict2[(x, y)]
                                    else:
                                        Groups[pixelGroupDict2[x, y + 1]][0].remove((x, y + 1))
                                        Groups[pixelGroupDict2[x, y]][0].append((x, y + 1))
                                        pixelGroupDict2[(x, y + 1)] = pixelGroupDict2[(x, y)]

                                        Groups[pixelGroupDict2[x, y + 2]][0].remove((x, y + 2))
                                        Groups[pixelGroupDict2[x, y]][0].append((x, y + 2))
                                        pixelGroupDict2[(x, y + 2)] = pixelGroupDict2[(x, y)]

                                        Groups[pixelGroupDict2[x, y + 3]][0].remove((x, y + 3))
                                        Groups[pixelGroupDict2[x, y]][0].append((x, y + 3))
                                        pixelGroupDict2[(x, y + 3)] = pixelGroupDict2[(x, y)]

                                        Groups[pixelGroupDict2[x, y + 4]][0].remove((x, y + 4))
                                        Groups[pixelGroupDict2[x, y]][0].append((x, y + 4))
                                        pixelGroupDict2[(x, y + 4)] = pixelGroupDict2[(x, y)]

                                        Groups[pixelGroupDict2[x, y + 5]][0].remove((x, y + 5))
                                        Groups[pixelGroupDict2[x, y]][0].append((x, y + 5))
                                        pixelGroupDict2[(x, y + 5)] = pixelGroupDict2[(x, y)]
                                else:
                                    Groups[pixelGroupDict2[x, y + 1]][0].remove((x, y + 1))
                                    Groups[pixelGroupDict2[x, y]][0].append((x, y + 1))
                                    pixelGroupDict2[(x, y + 1)] = pixelGroupDict2[(x, y)]

                                    Groups[pixelGroupDict2[x, y + 2]][0].remove((x, y + 2))
                                    Groups[pixelGroupDict2[x, y]][0].append((x, y + 2))
                                    pixelGroupDict2[(x, y + 2)] = pixelGroupDict2[(x, y)]

                                    Groups[pixelGroupDict2[x, y + 3]][0].remove((x, y + 3))
                                    Groups[pixelGroupDict2[x, y]][0].append((x, y + 3))
                                    pixelGroupDict2[(x, y + 3)] = pixelGroupDict2[(x, y)]

                                    Groups[pixelGroupDict2[x, y + 4]][0].remove((x, y + 4))
                                    Groups[pixelGroupDict2[x, y]][0].append((x, y + 4))
                                    pixelGroupDict2[(x, y + 4)] = pixelGroupDict2[(x, y)]
                            else:
                                Groups[pixelGroupDict2[x, y + 1]][0].remove((x, y + 1))
                                Groups[pixelGroupDict2[x, y]][0].append((x, y + 1))
                                pixelGroupDict2[(x, y + 1)] = pixelGroupDict2[(x, y)]

                                Groups[pixelGroupDict2[x, y + 2]][0].remove((x, y + 2))
                                Groups[pixelGroupDict2[x, y]][0].append((x, y + 2))
                                pixelGroupDict2[(x, y + 2)] = pixelGroupDict2[(x, y)]

                                Groups[pixelGroupDict2[x, y + 3]][0].remove((x, y + 3))
                                Groups[pixelGroupDict2[x, y]][0].append((x, y + 3))
                                pixelGroupDict2[(x, y + 3)] = pixelGroupDict2[(x, y)]
                        else:
                            Groups[pixelGroupDict2[x, y + 1]][0].remove((x, y + 1))
                            Groups[pixelGroupDict2[x, y]][0].append((x, y + 1))
                            pixelGroupDict2[(x, y + 1)] = pixelGroupDict2[(x, y)]

                            Groups[pixelGroupDict2[x, y + 2]][0].remove((x, y + 2))
                            Groups[pixelGroupDict2[x, y]][0].append((x, y + 2))
                            pixelGroupDict2[(x, y + 2)] = pixelGroupDict2[(x, y)]
                    else:
                        Groups[pixelGroupDict2[x, y + 1]][0].remove((x, y + 1))
                        Groups[pixelGroupDict2[x, y]][0].append((x, y + 1))
                        pixelGroupDict2[(x, y + 1)] = pixelGroupDict2[(x, y)]





    return borders, Groups











def reColor(Groups, xsize, ysize, removeBackground, borders):
    recolored = Image.new('RGB', (xsize, ysize), (1, 1, 1))
    pixels = recolored.load()
    groups = len(Groups)
    groupNum = 0
    if removeBackground == True:
        for group in range(0, groups):
            maxX = 0
            minX = xsize
            maxY = 0
            minY = ysize
            for pixel in Groups[groupNum][0]:
                if pixel[0] > maxX:
                    maxX = pixel[0]
                if pixel[0] < minX:
                    minX = pixel[0]
                if pixel[1] > maxY:
                    maxY = pixel[1]
                if pixel[1] < minY:
                    minY = pixel[1]

            if minX < 20 and maxX > xsize - 21 and minY < 20 and maxY > ysize - 21:
                Groups.remove(Groups[groupNum])
                groupNum -= 1
            else:
                for pixel in Groups[groupNum][0]:
                    pixels[pixel[0], pixel[1]] = Groups[groupNum][1]
            groupNum += 1
    else:
        for group in range(0, groups):
            for pixel in Groups[groupNum][0]:
                pixels[pixel[0], pixel[1]] = Groups[groupNum][1]
            groupNum += 1

    for border in borders:
        pixels[border[0], border[1]] = (0, 255, 0)

    recolored.show()
    return recolored, Groups





def seperateGroups(Groups, xsize, ysize):
    for group in Groups:
        aggAmount = group[1][0] + group[1][1] + group[1][2]
        if aggAmount < 120:
            groupFrame = Image.new('RGB', (xsize, ysize), (255, 255, 255))
        else:
            groupFrame = Image.new('RGB', (xsize, ysize), (1, 1, 1))
        pixels = groupFrame.load()

        for pixel in group[0]:
            pixels[pixel[0], pixel[1]] = group[1]
        print(group[1])

        groupFrame.show()


def boxes(Groups, recoloredImage, draw, xsize, ysize):
    for group in Groups:
        maxX = 0
        minX = xsize
        maxY = 0
        minY = ysize
        for pixel in group[0]:
            if pixel[0] > maxX:
                maxX = pixel[0]
            if pixel[0] < minX:
                minX = pixel[0]
            if pixel[1] > maxY:
                maxY = pixel[1]
            if pixel[1] < minY:
                minY = pixel[1]

        draw.rectangle((minX, minY, maxX, maxY), fill = None, outline = (255, 0, 0))

    recoloredImage.show()









def grayFilter(borders, pixelsDict, pixels, xsize, ysize):
    for pixel in borders:
        x = pixel[0]
        y = pixel[1]
        borderNum = 0
        bordersToRemove = []

        if x > 0 and x < xsize - 1 and y > 0 and y < ysize - 1:
            if pixelsDict[(x + 1, y)] == True:
                borderNum += 1
                bordersToRemove.append((x + 1, y))
            if pixelsDict[(x + 1, y + 1)] == True:
                borderNum += 1
                bordersToRemove.append((x + 1, y + 1))
            if pixelsDict[(x + 1, y - 1)] == True:
                borderNum += 1
                bordersToRemove.append((x + 1, y - 1))
            if pixelsDict[(x - 1, y)] == True:
                borderNum += 1
                bordersToRemove.append((x - 1, y))
            if pixelsDict[(x - 1, y + 1)] == True:
                borderNum += 1
                bordersToRemove.append((x - 1, y + 1))
            if pixelsDict[(x - 1, y - 1)] == True:
                borderNum += 1
                bordersToRemove.append((x - 1, y - 1))
            if pixelsDict[(x, y + 1)] == True:
                borderNum += 1
                bordersToRemove.append((x, y + 1))
            if pixelsDict[(x, y - 1)] == True:
                borderNum += 1
                bordersToRemove.append((x, y - 1))
            
        if borderNum < 2:
            pixels[x, y] = 255
            borders.remove((x, y))
            for pixel in bordersToRemove:
                X = pixel[0]
                Y =  pixel[1]
                pixels[X, Y] = 255
                try:
                    borders.remove((X, Y))
                except:
                    zz = 4

    return borders
            

def colorFilter(Groups, pixelGroupDict, pixelsArray, pixels, xsize, ysize):
    for pixel in pixelsArray:
        x = pixel[0][0]
        y = pixel[0][1]

        coordinates = (x, y)


        oldGroup = pixelGroupDict[coordinates]

        if x == 0:
            if y == 0:
                BM = pixelGroupDict[(x, y + 1)]
                BR = pixelGroupDict[(x + 1, y + 1)]
                RM = pixelGroupDict[(x + 1, y)]
                surrounding = [BM, BR, RM]

                newGroup = max(set(surrounding), key = surrounding.count)

            if y > 0 and y < ysize - 1:
                BM = pixelGroupDict[(x, y + 1)]
                BR = pixelGroupDict[(x + 1, y + 1)]
                RM = pixelGroupDict[(x + 1, y)]
                TR = pixelGroupDict[(x + 1, y - 1)]
                TM = pixelGroupDict[(x, y - 1)]
                surrounding = [BM, BR, RM, TR, TM]

                newGroup = max(set(surrounding), key = surrounding.count)

            if y == ysize - 1:
                RM = pixelGroupDict[(x + 1, y)]
                TR = pixelGroupDict[(x + 1, y - 1)]
                TM = pixelGroupDict[(x, y - 1)]
                surrounding = [RM, TR, TM]

                newGroup = max(set(surrounding), key = surrounding.count)

        if x > 0 and x < xsize - 1:
            if y == 0:
                LM = pixelGroupDict[(x - 1, y)]
                BL = pixelGroupDict[(x - 1, y + 1)]
                BM = pixelGroupDict[(x, y + 1)]
                BR = pixelGroupDict[(x + 1, y + 1)]
                RM = pixelGroupDict[(x + 1, y)]
                surrounding = [LM, BL, BM, BR, RM]

                newGroup = max(set(surrounding), key = surrounding.count)

            if y > 0 and y < ysize - 1:
                RM = pixelGroupDict[(x + 1, y)]
                BR = pixelGroupDict[(x + 1, y + 1)]
                TR = pixelGroupDict[(x + 1, y - 1)]
                LM = pixelGroupDict[(x - 1, y)]
                BL = pixelGroupDict[(x - 1, y + 1)]
                TL = pixelGroupDict[(x - 1, y - 1)]
                BM = pixelGroupDict[(x, y + 1)]
                TM = pixelGroupDict[(x, y - 1)]
                surrounding = [RM, BR, TR, LM, BL, TL, BM, TM]

                newGroup = max(set(surrounding), key = surrounding.count)

            if y == ysize - 1:
                RM = pixelGroupDict[(x + 1, y)]
                TR = pixelGroupDict[(x + 1, y - 1)]
                TM = pixelGroupDict[(x, y - 1)]
                TL = pixelGroupDict[(x - 1, y - 1)]
                LM = pixelGroupDict[(x - 1, y)]
                surrounding = [RM, TR, TM, TL, LM]

                newGroup = max(set(surrounding), key = surrounding.count)

        if x == xsize - 1:
            if y == 0:
                LM = pixelGroupDict[(x - 1, y)]
                BL = pixelGroupDict[(x - 1, y + 1)]
                BM = pixelGroupDict[(x, y + 1)]
                surrounding = [LM, BL, BM]

                newGroup = max(set(surrounding), key = surrounding.count)

            if y > 0 and y < ysize - 1:
                TM = pixelGroupDict[(x, y - 1)]
                TL = pixelGroupDict[(x - 1, y - 1)]
                LM = pixelGroupDict[(x - 1, y)]
                BL = pixelGroupDict[(x - 1, y + 1)]
                BM = pixelGroupDict[(x, y + 1)]
                surrounding = [TM, TL, LM, BL, BM]

                newGroup = max(set(surrounding), key = surrounding.count)

            if y == ysize - 1:
                TM = pixelGroupDict[(x, y - 1)]
                TL = pixelGroupDict[(x - 1, y - 1)]
                LM = pixelGroupDict[(x - 1, y)]
                surrounding = [TM, TL, LM]

                newGroup = max(set(surrounding), key = surrounding.count)
        if oldGroup != newGroup:
            pixels[x, y] = Groups[newGroup][1]
            Groups[oldGroup][0].remove(coordinates)
            Groups[newGroup][0].append(coordinates)
            # pixelGroupDict[coordinates] = newGroup #Maybe change dictionary too but would affect next ones in iteration




    return Groups


# def lineDetection(borders):
#     if




def grayAnalysis(ImageLink):
    xsize = 500
    ysize = 500
    image1Data = Image.open(ImageLink)  # Opens image, converts to RGB
    newSize = (xsize, ysize)
    image1Data = image1Data.resize(newSize)
    pixels = image1Data.load()

    pixelsArray = grayPixelData(pixels, xsize, ysize)

    borders, pixelsDict = grayScaleReading(pixelsArray, xsize, ysize, pixels)

    borders = grayFilter(borders, pixelsDict, pixels, xsize, ysize)

    image1Data.show()


def colorAnalysis(ImageLink):
    xsize = 300
    ysize = 300
    image1Data = Image.open(ImageLink) # Opens image, converts to RGB
    newSize = (xsize, ysize)
    image1Data = image1Data.resize(newSize)
    pixels = image1Data.load()

    pixelsArray = colorPixelData(pixels, xsize, ysize)

    # borders, pixelsDict = colorScaleReading(pixelsArray, xsize, ysize, pixels)

    groups, pixelGroupDict = colorObjectSeperation(pixelsArray, pixels) #Works better than refactoring function ATM
    borders = []
    # borders, groups = objectBorders(groups, pixelGroupDict, pixels, xsize, ysize)
    # groups = refactoringColorObjectSeperation(pixelsArray, pixels) Not as good
    # groups = colorFilter(groups, pixelGroupDict, pixelsArray, pixels, xsize, ysize) Worsens quality, doesn't help much with outliers



    removeBackground = False
    recoloredImage, Groups = reColor(groups, xsize, ysize, removeBackground, borders)

    draw = ImageDraw.Draw(recoloredImage)
    seperateGroups(groups, xsize, ysize)
    boxes(groups, recoloredImage, draw, xsize, ysize)


    # borders = colorFilter(borders, pixelsDict, pixels, xsize, ysize)








#Start Screen
print("Analyze Photo In: ")
print("1. Gray")
print("2. Color")
ans = input()

image = input("Enter a Photo to Analyze: ")
# neilArmstrongPhoto = 'Vision/TrainingPhotos/nielArmstrong.jpg'

if ans == "1":
    grayAnalysis(image)
if ans == "2":
    colorAnalysis(image)






# pyplot.imshow(image1Data)//plots image
# pyplot.show()//shows image




