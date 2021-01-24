import json
import math
#open the file 
myFile = open("./data.json", "r")

#load the file .. json to python 
cFile = json.load(myFile)

#print(cFile)  .. you must think that I'm stupid ..

myData = cFile["assignment_results"]

myRooms = myData[0]["shown_price"]

#print(myRooms)

roomKeys = list(myRooms.keys())
minPrice = math.inf 
minType = ""

for i in range(len(roomKeys)):
    if minPrice > float(myRooms[roomKeys[i]]):
        minPrice = float(myRooms[roomKeys[i]])
        minType = roomKeys[i]


print("THE MIN PRICE - > ", minPrice)
print("THE ROOM WITH THE MIN PRICE TYPE - >" , minType)
print("THE NUMBER OF GUEST ALLOWED FOR THE ROOM - >" , myData[0]["number_of_guests"])