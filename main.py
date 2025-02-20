#Marisol Morales and Andreas Moreno, CECS 277 Lab 9
#Minotaur Maze: allows the user to wander through a maze that is guarded by a minotaur.
# 4/9/2024
import maze 
import hero
import minotaur

def main():
  m =  maze.Maze()
  h = hero.Hero()
  min = minotaur.Minotaur()
  allowed_inputs = 'wasd'
  result = ""

  while result != "f" or result != "M":
    print(m)
    user_direction = input("Choose a direction (WASD): ").lower()

    while user_direction not in allowed_inputs or len(user_direction) != 1:
      print("Not a valid input, please try again using (WASD).")
      user_direction = input("Choose a direction (WASD): ").lower()

    print()
    min.move_minotaur()
    
    if user_direction == "w":
      result = h.go_up()
    elif user_direction == "a":
      result = h.go_left()
    elif user_direction == "s":
      result = h.go_down()
    elif user_direction == "d":
      result = h.go_right()

    

    if result == "M":
      print("Oh No! You ran into the Minotaur!")
      print("Better luck next time!")
      break
    elif result == "f":
      print ("You found the exit! Congratulations!")
      break

main()