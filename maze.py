class Maze:
  _instance = None
  _initialized = False
  
  def __new__(cls):
  #if maze not been constructed,it is constructed and stored in _instance and returned
  #if it has been constructed, it is returned has been constructed, it is returned
    if cls._instance is None:
      cls._instance = super().__new__(cls)
    return cls._instance

  def __init__(self): 
  #creates and fills the 2D list from the file contents
    if not Maze._initialized:
      self._maze = []
      file = open("minomaze.txt")
      for line in file:
        list = []
        for ch in line:
          if ch != '\n':
            list.append(ch)
        self._maze.append(list)
      Maze._initialized = True

  def __getitem__(self, row):
  #returns the specified row from the maze
    return self._maze[row]

  def __len__(self):
  #returns the number of rows in the maze
    num_rows = len(self._maze)
    return num_rows

  def __str__(self): 
  #returns the maze as a string in a grid format
    maze_str = ""
    for row in self._maze:
      for ch in row:
        maze_str += ch + ' '
      maze_str += "\n"
    return maze_str

  def search_maze(self, ch):
  #returns the location of the character in the maze as two-item 1D list
    for row in range(len(self._maze)):
      for col in range(len(self._maze[row])):
        if self._maze[row][col] == ch:
          return [row, col]
    