import maze


class Hero:

  def __init__(self):
  #sets the hero’s starting location by finding the start position of maze 
  #based on ('s') and then places 'H' in the maze at that location
    m = maze.Maze()
    starting_location = m.search_maze('s')
    m[starting_location[0]][starting_location[1]] = 'H'

  def go_up(self):
    #moves the hero up one space and returns the coordinates 
    #if the hero runs into a wall it prints a message regarding that
    m = maze.Maze()
    coordinates = m.search_maze('H')
    if coordinates is None: # if minotaur captured the hero
      row, col = m.search_maze('M')
      return m[row][col]
    row = coordinates[0]
    col = coordinates[1]
    if m[row - 1][col] == '*':
      print("You ran into a wall.")
      return m[row][col]
    if m[row - 1][col] == 'M' or m[row - 1][col] == 'f': # game over
      return m[row - 1][col] 
    m[row][col] = ' '
    m[row - 1][col] = 'H'
    return m[row - 1][col]

  def go_down(self):
    #moves the hero down one space and returns the coordinates
    #if the hero runs into a wall it prints a message regarding that
    m = maze.Maze()
    coordinates = m.search_maze('H')
    if coordinates is None: # if minotaur captured the hero
      row, col = m.search_maze('M')
      return m[row][col]
    row = coordinates[0]
    col = coordinates[1]
    if m[row + 1][col] == '*':
      print("You ran into a wall.")
      return m[row][col]
    if m[row + 1][col] == 'M' or m[row + 1][col] == 'f': # game over
      return m[row + 1][col]
    m[row][col] = ' '
    m[row + 1][col] = 'H'
    return m[row + 1][col]

  def go_left(self):
    #moves the hero left one space and returns the coordinates
    #if the hero runs into a wall it prints a message regarding that
    m = maze.Maze()
    coordinates = m.search_maze('H')
    if coordinates is None: # if minotaur captured the hero
      row, col = m.search_maze('M')
      return m[row][col]
    row = coordinates[0]
    col = coordinates[1]
    if m[row][col - 1] == '*':
      print("You ran into a wall.")
      return m[row][col]
    if m[row][col - 1] == 'M' or m[row][col - 1] == 'f': # game over
      return m[row][col - 1]
    m[row][col] = ' '
    m[row][col - 1] = 'H'
    return m[row][col - 1]

  def go_right(self):
    #moves the hero right one space and returns the coordinates
    #if the hero runs into a wall it prints a message regarding that
    m = maze.Maze()
    coordinates = m.search_maze('H')
    if coordinates is None: # if minotaur captured the hero
      row, col = m.search_maze('M')
      return m[row][col]
    row = coordinates[0]
    col = coordinates[1]
    if m[row][col + 1] == '*':
      print("You ran into a wall.")
      return m[row][col]
    if m[row][col + 1] == 'M' or m[row][col + 1] == 'f': # game over
      return m[row][col + 1]
    m[row][col] = ' '
    m[row][col + 1] = 'H'
    return m[row][col + 1]
