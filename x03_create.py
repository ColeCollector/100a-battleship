#!python3
import time
import x01_map
import x02_convert
'''
There are 5 boats in battleship. They must occupy coordinates that are horizontal or vertical only (no diagonals). 
The size of the boats are 2, 3, 3, 4 and 5. Create a function that generates a list of the data for your boats.
'''

def create():
  '''
  You will need to specify what information you need as inputs, but the output should be a list
  Add whatever code you need for each of your different ships to specify what coordinates it
  occupies and/or whether it is vertical/horizontal
  '''
  print("Please give your answer with one letter and a number (number = x axis | letter = y axis ). ")
  print("ex: b3 or A 4")
  time.sleep(0.5)
  occupied = []
  boat = []

  boatsize = [2, 3, 3, 4, 5]
  boats = ["Tugboat", "Submarine", "Destoyer", "Carrier", "Battleship"]
  
  while True:
      nodupplicate = False
      for i in range(0,5):
        while nodupplicate == False:
          try:
            time.sleep(0.5)
            coord = input(f"Where would you like to place your {boats[i]}? ")
            direction = input("Vertical (v) or Horizontal? (h) ")
            coord = x02_convert.convert(coord)
            break
          except:
            print("Please enter a valid input")

          nodupplicate = True
          for i in range(1,boatsize[i]):

            boat.append((int(coord[0]),int(coord[1])))
              
            if direction == "v":
              newy = int(coord[1]) + i
              if newy > 10:
                boat.append((int(coord[0]),newy))

            elif direction == "h":
              newx = int(coord[0]) + i
              if newy > 10:
                boat.append((newx,int(coord[1])))
          for i in boat:
            if i in occupied:
              print("dupe")
              nodupplicate = False 
        print("ybrokenadsa")
        for i in range(0,len(boat)):
          print("adding")
          occupied.append(boat[i])
        print(occupied)
      break


  return occupied



x = create()
print(x)
x01_map.map(x)


"""
occupied = list of coordinates

add a boat:
  create list of coordianates for the boat
  if any of these coordinates are in occupied, make them choose again
  eg boat = [ [5,3], [5,4], [5,5]]


  for 1 boat
  boatDone = False
  while boatDone == False
    boatDone = True
    boat = generate coordinates
    for i in boat:
      if i in occupied:
        boatDone = False
  
  add the boat and append all of its coordinates to occupied
  
"""