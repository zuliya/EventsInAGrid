import numpy as np

#Grid - GLOBAL
grid = []

#Object for event
class event:
    id = None
    tickets = None
    price = None
    manhattanDistance = None

    #Create object with id,tickets,pirce
    def __init__(self, id, tickets, price):
        self.id = id
        self.tickets = tickets
        self.price = price

#Validation Function - Checking inputs are in good val.
def validateInput(x,y):
    #Check if it is int.
    try:
        x = int(x)
        y = int(y)
        #check if is in range -10 to 10
        if x > 10 or x < -10 or y > 10 or y < -10:
            print("ERROR: Please input the correct coordinates in range (-10 to 10).")
            return False
        else:
            return True

    except ValueError:
        print("ERROR: Please enter integer co-ordinates.")
        return False

#Function to convert coordinates to grid
def fixInput(x,y):
    x += 10
    y += 10
    return x,y

def manhattanDistance(start, end):
    startX, startY = start
    endX, endY = end

    #A,B = (Ax-Bx)+(Ay-By) Manhatan distabce formula
    return abs(endX - startX) + abs(endY - startY)

#Generate grid and generate seed. First to run.
def seed():
    for x in range(0, 21):
        yAxis = []
        for y in range(0, 21):
            yAxis.append(None)
        grid.append(yAxis)

    #TODO - Check if the event exists at the point.
    #Generate Seed

    #Generating uniqueID and checking if it exists already.
    usedIDs = []

    for counter in range(10):
        #Generating ID
        while True:
            id = np.random.randint(0, 20)
            #check if id is taken
            if (id not in usedIDs):
                usedIDs.append(id)
                break
        #generate 10 events (id, ticket,price)
        grid[np.random.randint(0,20)][np.random.randint(0,20)] = event(id,np.random.randint(0,20),np.random.randint(0,100))

#Function to find events
def findEvents(inputX,inputY):

    #Distance => Events
    events = {}

    #Finding events and populating the events array
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            #go through grid and find all events and their distance
            if grid[y][x] != None:
                grid[y][x].manhattanDistance = manhattanDistance((inputX,inputY),(x,y))
                events[manhattanDistance((inputX,inputY),(x,y))] = grid[y][x]
    #sort distances
    distances = list(events.keys())
    distances.sort()

    #Return events
    eventReturn = []

    #Getting the 5 closest events
    for counter in range(5):
        eventReturn.append(events[distances[counter]])

    #Returing the list of 5 closest events
    return eventReturn

#Get user input function.
def getUserInput():
    #Loop till correct input given
    # inputCoordinate = input("Please Input Coordinates:")
    while True:
        inputCoordinate = input("Please Input Coordinates:")

        # Check if two values were entered
        if (len(inputCoordinate.split(",")) != 2):
            print("ERROR: Enter a valid co-ordinate. Example: 4,2")
            continue

        xInput,yInput = inputCoordinate.split(",")

       #IF the check passed proceed
        if (validateInput(xInput,yInput)):
            return int(xInput), int(yInput)

#Print events function.
def printResults(results):
    for event in results:
        print("Event: "+str(event.id)+" - $"+str(event.price)+", Distance "+str(event.manhattanDistance))

#Main
#Generate matrix and seed.
seed()

while(True):
    inputX,inputY = getUserInput()
    printResults(findEvents(inputX,inputY))




