Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

question_one = int(input("""
Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk 
"""))

if question_one == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif question_one == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print("Wrong input")

question_two = int(input("""
Q2) When I'm dead, I want people to remember me as: 
    1) The Good
    2) The Great
    3) The wise
    4) The Bold
"""))

if question_two == 1:
  Hufflepuff += 2
elif question_two == 2:
  Slytherin += 2
elif question_two == 3:
  Ravenclaw += 2
elif question_two == 4:
  Gryffindor += 2
else:
  print("Wrong input")

question_three = int(input("""
Q3) Which kind of instrument most pleases your ear? 
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum
"""))

if question_three == 1:
  Slytherin += 4
elif question_three == 2:
  Hufflepuff += 4
elif question_three == 3:
  Ravenclaw += 4
elif question_three == 4:
  Gryffindor += 4
else: 
  print("Wrong input")

#prints values
print(max(Hufflepuff, Slytherin, Ravenclaw, Gryffindor))
print("Hufflepuff:", Hufflepuff)
print("Slytherin:", Slytherin)
print("Ravenclaw:", Ravenclaw)
print("Gryffindor:", Gryffindor)

#prints highest value with corresponding house
highest_score = max(Hufflepuff, Slytherin, Ravenclaw, Gryffindor) 

if highest_score == Hufflepuff:
  print("House with most points: ", "Hufflepuff",Hufflepuff)
elif highest_score == Slytherin:
  print("House with most points: ", "Slytherin",Slytherin)
elif highest_score == Ravenclaw:
  print("House with most points: ", "Ravenclaw",Ravenclaw)
elif highest_score == Gryffindor:
  print("House with most points: ", "Gryffindor",Gryffindor)






