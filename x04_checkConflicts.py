#!python3
import time
import x01_map
import x02_convert
'''
##### 4. Check for conflicts
It is not possible for a boat to occupy the same space as another boat.  
We would need to add a tool to check to see if a boat that we are trying 
to place is overlapping with another boat, so that if it is, we can re-create it.

One strategy:
Create a function that converts all existing boats to a list of coordinates and add them to
a list of "occupied" squares
Check each of your new ship squares to see if there is a conflict
The two functions that have been created here might be helpful
'''


def battleship():
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

battleship()

