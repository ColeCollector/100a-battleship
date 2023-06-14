#! python3

"""
* Take a list of coordinates and draw a map showing occupied squares
* The map is a 10x10 grid
* (0,0) is the coordinate in the bottom left (like a regular (x,y) grid system)

```
Sample Data1:
[[1, 1], [2, 1], [4, 0], [5, 0], [6, 0], [0, 1], [0, 2], [0, 3], [1, 8], [2, 8], [3, 8], [4, 8], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7]]

Suggested Output:
..........
.xxxx.....
....x.....
....x.....
....x.....
....x.....
x...x.....
x.........
xxx.......
....xxx...

Sample Data2:
[[0, 0], [1, 0], [8, 6], [8, 7], [8, 8], [7, 5], [7, 6], [7, 7], [1, 1], [1, 2], [1, 3], [1, 4], [0, 6], [1, 6], [2, 6], [3, 6], [4, 6]]

..........
........x.
.......xx.
xxxxx..xx.
.......x..
.x........
.x........
.x........
.x........
xx........
```
"""



def map():
 occupied = ([[1, 1], [2, 1], [4, 0], [5, 0], [6, 0], [0, 1], [0, 2], [0, 3], [1, 8], [2, 8], [3, 8], [4, 8], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7]])
 

 defaultmap = ["..........","..........","..........","..........","..........","..........","..........","..........","..........",".........."]


 for i in range(0,16):
  coords = occupied[i]
  x = coords[0]
  y = coords[1]

  line = defaultmap[y]
  lines = [line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8],line[9]]
  
  lines.pop(x)
  lines.insert(x,"x")


  defaultmap.pop(y)
  defaultmap.insert(y,f"{lines[0]}{lines[1]}{lines[2]}{lines[3]}{lines[4]}{lines[5]}{lines[6]}{lines[7]}{lines[8]}{lines[9]}")

 for i in range(0,10):
  print(defaultmap[i])

map()