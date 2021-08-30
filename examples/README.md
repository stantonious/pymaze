

To encode a maze

```
from pymaze.maze_manager import MazeManager
from pymaze.maze import Maze
from pymaze import encoder
manager = MazeManager()
maze = manager.add_maze(14, 14)

m=encoder.encode(maze.grid)


for _i in range(0,14,2):
  if m[_i][_i] & encoder.NORTH_BIT:
    encoder.add_status(m,_i,_i,encoder.NORTH_BIT, (_i%2)+2)
  elif m[_i][_i] & encoder.SOUTH_BIT:
    encoder.add_status(m,_i,_i,encoder.SOUTH_BIT, (_i%2)+2)
  elif m[_i][_i] & encoder.EAST_BIT:
    encoder.add_status(m,_i,_i,encoder.EAST_BIT, (_i%2)+2)
  elif m[_i][_i] & encoder.WEST_BIT:
    encoder.add_status(m,_i,_i,encoder.WEST_BIT, (_i%2)+2)


str(m).replace('[','{').replace(']','}')

```
