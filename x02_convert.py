#!python3
"""
Given a string literal convert it to a list that contains the coordinate. Your string literal should be able to remove whitespace and work with both lower and upper case values. "B3", "b3" , "B 3" and "b 3" should all correspond to the list item [1,2]
"""

def convert(coordinate):
  """
  input: coordinate is a string literal 
    examples: "B 3" "B3" "b3"
  return value: list containing 2 integers
  """

  lowercase = ["a","b","c","d","e","f","g","h","i","j","k"]
  uppercase = ["A","B","C","D","E","F","G","H","I","J","K"]
  numbers = ["1","2","3","4","5","6","7","8","9","10","0"]

  if coordinate[0] in lowercase:
    if len(coordinate) == 2:
      answer = (lowercase.index(coordinate[0]),(int(coordinate[1])-1))
    else:
      if coordinate[1] in numbers and coordinate[2] in numbers:
       answer = (lowercase.index(coordinate[0]),(9))
      else:
        answer = (lowercase.index(coordinate[0]),(int(coordinate[2])-1))

  elif coordinate[0] in uppercase:
    if len(coordinate) == 2:
      answer = (uppercase.index(coordinate[0]),(int(coordinate[1])-1))
    else:
      if coordinate[1] in numbers and coordinate[2] in numbers:
       answer = (uppercase.index(coordinate[0]),(9))
      elif str(coordinate[1]) != "0":
        answer = (uppercase.index(coordinate[0]),(int(coordinate[2])-1))
  
  return list(answer)


    


    
  



if __name__ == "__main__":
  assert convert("B3") == [1,2]
  assert convert("A10") == [0,9]
  assert convert("d 4") == [3,3]
  
