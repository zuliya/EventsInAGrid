import numpy as np
import sys
import re

score = []
x = sys.argv[1]
y = sys.argv[2]

#TODO check for bad input

def checkIn(x,y):
    if x > 10 or x < -10 or y>10 or y< -10:
        print("Please input the correct coordinates in range (-10 to 10)")
        return False
    if x == None:
        print("Please input your x coordinates")
        return False
    if y == None:
        print("Please input your y coordinates")
        return False
    if x!= int or y!= int:
        print("Please input your coordinates as a string")
        return False
    else:
        return True



#Represent the coordinates as a 2 dimensional matrix
def makeGrid():
    array = []
    for i in range(0, 20):
        dest = []
        for j in range(0, 20 ):
            dest.append(None)
        score.append(dest)
    return score
    # print(np.matrix(score))


# Spec says grid (-10 to +10 )
def changeCoordinates(x,y):
    # Assume input coordinates will be given as negatives (-10, -10  will be 0,0)
    x = int(x)+10
    y = int(y)+10
    return x,y

def coordinatesUserFormat(x,y):
    x = int(x)-10
    y = int(y)-10
    return x,y

# index = unique key
def generateSeed(index):
    event = []
    prices = []
    event.append(index)
    # number of prices generated
    for i in range (0,10):
        # random price to 100
        prices.append(np.random.randint(0,100))
    event.append(prices)
    return event

# n = number random events
def populateSeed(n):
    score = makeGrid()
        #unique key =  num random events
    for uniqueIndex in range (0,n):
        x = np.random.randint(0,20)
        y = np.random.randint(0,20)
        score[x][y] = generateSeed(uniqueIndex)
    print(np.matrix(score))
    return score


def getClosest(x,y):
    #add 20 ramdom  events
    populateSeed(20)
    (x,y) = changeCoordinates(x,y)
    h,w = 20,20
    closestEvents = []
    # go through the etire matirx
    for x in range (0,h):
        for y in range (0,w):
            i = 0
            j = 0
            #increase grid by 2 (x,y;1*1 3*3; 5*5...)
            for regionY in range(y-i,y+i+1):
                for  regionX in range (x-j,x+j+1):
                    i +=2
                    j +=2
                    #out of boudaries Error ignore
                    if regionY < 0 or regionY > h - 1 or regionX < 0 or regionX > w - 1:
                        continue
                    if score[regionY][regionX]!= None:
                        foundEvent = []
                        #foundEvent = x,y, unique key, prices
                        foundEvent.append(x)
                        foundEvent.append(y)
                        foundEvent.append(score[regionY][regionX])
                        closestEvents.append(foundEvent)
                    if len(closestEvents) == 5:
                        return closestEvents
def getUserOutput(event):
    #get Lowest price
    removeXY = list(event[2])
    prices = removeXY[1]
    sortedPrice = (sorted(prices))
    #return x y LowPrice
    newEvent = event[:2]
    #Coordinates to user -10 / 10
    newEvent[0] = int(newEvent[0]-10)
    newEvent[1] = int(newEvent[1]-10)
    newEvent.append(sortedPrice[0])
    return newEvent


#return 5 closest events with the  lowest price
def returnEvent(x,y):
    closestEvents = getClosest(x, y)
    print(closestEvents)
    allEvents = []
    for i in range (5):
        newEvent = getUserOutput(closestEvents[i])
        allEvents.append((newEvent))
        print(allEvents)
    return allEvents




