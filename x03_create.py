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
  print("Please give your answer with one letter and a number.\nkeep in mind the boat will go up/right of your starting point. ")
  print("ex: b3 or A 4\n")
  time.sleep(0.5)
  occupied = []
  boat = []

  boatsize = [2, 3, 3, 4, 5]
  boats = ["Tugboat", "Submarine", "Destoyer", "Carrier", "Battleship"]
  
  while True:
      for j in range(0,5):
        nodupplicate = False
        while nodupplicate == False:
          while True:
            boat.clear()
            try:
              time.sleep(0.5)
              coord = input(f"Where would you like to place your {boats[j]}? ")
              direction = input("Vertical (v) or Horizontal? (h) ")
              coord = x02_convert.convert(coord)
              break
              
            except:
              print("Please enter a valid input")

          nodupplicate = True

          boat.append((int(coord[0]),int(coord[1])))
          for i in range(1,boatsize[j]):

            if direction == "v":
              newy = int(coord[1]) + i
              if newy < 10:
                boat.append((int(coord[0]),newy))
              else:
                print("Keep your boat on the map")
                nodupplicate = False
                break

            elif direction == "h":
              newx = int(coord[0]) + i
              if newx < 10:
                boat.append((newx,int(coord[1])))
              else:
                print("Keep your boat on the map")
                nodupplicate = False
                break
            
            else:
              print("Please enter a valid input")
              nodupplicate = False
              
          for n in boat:
            if n in occupied:
              print("Your boat is overlapping another boat")
              nodupplicate = False 
              break
            
        for x in range(0,len(boat)):
          occupied.append(boat[x])
        
        x01_map.map(occupied)
      break
  return occupied

create()

