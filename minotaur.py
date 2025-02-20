import random 
import maze 

class Minotaur:

  def __init__(self):
    #randomizes the starting location of the minotaur to any blank space in the maze
    #places "M" at that location in the maze
    m = maze.Maze()
    random_row = random.randint(0, len(m) - 1)
    random_col = random.randint(0, len(m[0]) - 1)
    while m[random_row][random_col] != " ":
      random_row = random.randint(0, len(m) - 1)
      random_col = random.randint(0, len(m[random_row]) - 1)
    m[random_row][random_col] = "M"

  def move_minotaur(self):
    #every turn the minotaur detects the hero location in maze
    #proceeds to move one space towards that direction
    #if the minotaur moves into the hero's location, the hero loses
    m = maze.Maze()
    hero_pos = m.search_maze('H')
    mino_pos = m.search_maze('M')
    row = mino_pos[0]  # of minotaur
    col = mino_pos[1]  # of minotaur
    row_diff = mino_pos[0] - hero_pos[0]
    col_diff = mino_pos[1] - hero_pos[1]

    move = ''  # will hold letter code for move
    # same row
    if row_diff == 0:
      if col_diff > 0 and m[row][col - 1] != '*' and m[row][
          col - 1] != 'f':  # if to the right of hero
        move = 'l'
      elif col_diff < 0 and m[row][col + 1] != '*' and m[row][
          col + 1] != 'f':  # if to the left of hero
        move = 'r'
      elif m[row + 1][col] != '*' and m[row + 1][col] != 'f':  # move down
        move = 'd'
      elif m[row - 1][col] != '*' and m[row - 1][col] != 'f':  # move up
        move = 'u'

    # same column
    elif col_diff == 0:
      if row_diff > 0 and m[row - 1][col] != '*' and m[
          row - 1][col] != 'f':  # if below hero
        move = 'u'
      elif row_diff < 0 and m[row + 1][col] != '*' and m[
          row + 1][col] != 'f':  # if above hero
        move = 'd'
      elif m[row][col - 1] != '*' and m[row][col - 1] != 'f':  # move left
        move = 'l'
      elif m[row][col + 1] != '*' and m[row][col + 1] != 'f':  # move right
        move = 'r'

    # if closer horizontally
    elif abs(col_diff) < abs(row_diff):
      if col_diff > 0 and m[row][col - 1] != '*' and m[row][
          col - 1] != 'f':  # if to the right of hero
        move = 'l'
      elif col_diff < 0 and m[row][col + 1] != '*' and m[row][
          col + 1] != 'f':  # if to the left of hero
        move = 'r'
      elif row_diff > 0 and m[row - 1][col] != '*' and m[
          row - 1][col] != 'f':  # if below hero (move up)
        move = 'u'
      elif row_diff < 0 and m[row + 1][col] != '*' and m[
          row + 1][col] != 'f':  # if above hero (move down)
        move = 'd'
      else:  # move to any available space
        if m[row + 1][col] != '*' and m[row + 1][col] != 'f':
          move = 'd'
        elif m[row][col + 1] != '*' and m[row][col + 1] != 'f':
          move = 'r'
        elif m[row - 1][col] != '*' and m[row - 1][col] != 'f':
          move = 'u'
        elif m[row][col - 1] != '*' and m[row][col - 1] != 'f':
          move = 'l'

    # if closer vertically (abs(col_diff) <= abs(row_diff))
    else:
      if row_diff > 0 and m[row - 1][col] != '*' and m[
          row - 1][col] != 'f':  # if below hero (move up)
        move = 'u'
      elif row_diff < 0 and m[row + 1][col] != '*' and m[
          row + 1][col] != 'f':  # if above hero (move down)
        move = 'd'
      elif col_diff > 0 and m[row][col - 1] != '*' and m[row][
          col - 1] != 'f':  # if to the right of hero
        move = 'l'
      elif col_diff < 0 and m[row][col + 1] != '*' and m[row][
          col + 1] != 'f':  # if to the left of hero
        move = 'r'
      else:  # move to any available space
        if m[row + 1][col] != '*' and m[row + 1][col] != 'f':
          move = 'd'
        elif m[row][col + 1] != '*' and m[row][col + 1] != 'f':
          move = 'r'
        elif m[row - 1][col] != '*' and m[row - 1][col] != 'f':
          move = 'u'
        elif m[row][col - 1] != '*' and m[row][col - 1] != 'f':
          move = 'l'

    if move == 'l':
      m[row][col] = ' '
      temp = m[row][col - 1]
      m[row][col - 1] = 'M'
    elif move == 'r':
      m[row][col] = ' '
      temp = m[row][col + 1]
      m[row][col + 1] = 'M'
    elif move == 'u':
      m[row][col] = ' '
      temp = m[row - 1][col]
      m[row - 1][col] = 'M'
    elif move == 'd':
      m[row][col] = ' '
      temp = m[row + 1][col]
      m[row + 1][col] = 'M'

    return temp  # return character that was at the location