import numpy as np
#assumed coordinates will be given as int in range -10 to 10
#assumed the standard Manhatan calc function will be okay to be used

#To support multiple events in the same location I would add more event objects in one cell of the grid

#To support a much larger word size:
#  I would use a bigger grid
# May represent the events as an actual matrix or graph to speed up the search and use Breadth Fist Search to find events



# Grid - GLOBAL
grid = []

# Initialise class event
class event:
    id = None
    tickets = None
    price = None
    manhattanDistance = None

    # Create a constructor
    def __init__(self, id, tickets, price):
        # Create objects (id,tickets,price)
        self.id = id
        self.tickets = tickets
        self.price = price

# Validation Function - Checking inputs are in good val.
def validateInput(x,y):
    # Check if it is int.
    try:
        x = int(x)
        y = int(y)
        # check if is in range -10 to 10
        if x > 10 or x < -10 or y > 10 or y < -10:
            print("ERROR: Please input the correct coordinates in range (-10 to 10).")
            return False
        else:
            return True

    except ValueError:
        print("ERROR: Please enter integer co-ordinates.")
        return False

# Function to convert coordinates to grid
def fixInput(x,y):
    x += 10
    y += 10
    return x,y

# Calculate distanc using Simple Manhatan Distance
def manhattanDistance(start, end):
    startX, startY = start
    endX, endY = end
    # A,B = (Ax-Bx)+(Ay-By) Manhatan distabce formula
    return abs(endX - startX) + abs(endY - startY)


# Generate grid and generate seed. First to run.
def seed():
    for x in range(0, 21):
        yAxis = []
        for y in range(0, 21):
            yAxis.append(None)
        grid.append(yAxis)

    # TODO - Check if the event exists at the point.

    # Generate Seed (In the grid insert 10 events (uniqueID, rand ticket, rand price))
    usedIDs = []
    for counter in range(10):
        # Generating 10 random unique ID's
        while True:
            #make sure id is unique int between 20
            id = np.random.randint(0, 20)
            if (id not in usedIDs):
                usedIDs.append(id)
                break
        grid[np.random.randint(0,20)][np.random.randint(0,20)] = event(id,np.random.randint(0,20),np.random.randint(0,100))

# Function to find events
def findEvents(inputX,inputY):
    # Events stored as dictionary so can sort by keys ( distances )
    events = {}

    #Finding events and populating the events array
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[y][x] != None:
                grid[y][x].manhattanDistance = manhattanDistance((inputX,inputY),(x,y))
                # Distance = key ; points to a specific event
                events[manhattanDistance((inputX,inputY),(x,y))] = grid[y][x]

    #pull distance from events in array
    distances = list(events.keys())
    distances.sort()
    eventReturn = []

    #Getting the 5 closest events
    for counter in range(5):
        eventReturn.append(events[distances[counter]])
    return eventReturn

#Get user input function.
def getUserInput():
    #Loop till correct input given
    while True:
        inputCoordinate = input("Please Input Coordinates:")

        # Checks
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
        print("Event "+str(event.id)+" - $"+str(event.price)+", Distance "+str(event.manhattanDistance))

#Main
#Generate matrix and seed.
seed()

while(True):
    inputX,inputY = getUserInput()
    printResults(findEvents(inputX,inputY))




