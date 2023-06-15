#!python3
import time
import x01_map

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
  print("Please give your answer in two numbers (x and y). ")
  print("ex: 0 1 or 9 2")
  time.sleep(1)
  occupied = []
  tugboat = 2
  sub = 3 
  destroyer = 3
  carrier = 4
  battle = 5

  boatsize = [2, 3, 3, 4, 5]
  boats = ["Tugboat", "Submarine", "Destoyer", "Carrier", "Battleship"]

  for i in range(0,4):
    print(occupied)
    coord = input(f"Where would you like to place your {boats[i]}? ")
    direction = input("Vertical (v) or Horizontal? (h) ")
    for i in range(1,boatsize[i]):
      print(i)
      coord = list(coord)
      occupied.append((int(coord[0]),int(coord[2])))
      
      if direction == "v":
        newy = int(coord[2]) + i
        occupied.append((int(coord[0]),newy))

      elif direction == "h":
        newx = int(coord[0]) + i
        occupied.append((newx,int(coord[2])))
      occupied = [*set(occupied)] 
      occupied.sort()
  return occupied


x = create()
x01_map.map(x)