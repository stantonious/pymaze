
'''
Utilities to encode a generated maze

'''

NORTH_BIT = 0x0001
SOUTH_BIT = 0x0002
EAST_BIT =  0x0004
WEST_BIT =  0x0008
WALL_N  =0
WALL_E  =1
WALL_S  =2
WALL_W  =3

WALL_01_BIT = 0x0010
WALL_02_BIT = 0x0020
WALL_STAT_01_BIT = 0x0040
WALL_STAT_02_BIT = 0x0080

WALL_STAT_NONE=  0
WALL_STAT_IO = 1
WALL_STAT_HIGH = 2
WALL_STAT_LOW = 3

def encode(in_grid):
  out_grid = []
  inout_cells = []
  for _ir, _r in enumerate(in_grid):
    next_row = []
    for _ic, _c in enumerate(_r):
      res = 0
      if _c.walls["top"]:
        res |= NORTH_BIT
      if _c.walls["bottom"]:
        res |= SOUTH_BIT
      if _c.walls["left"]:
        res |= WEST_BIT
      if _c.walls["right"]:
        res |= EAST_BIT
      if _c.is_entry_exit:
        inout_cells.append((_ic,_ir))
      next_row.append(res)
    out_grid.append(next_row)

  #  for _n in inout_cells:
  #    print ("adding status cells",type(_n[0]),_n[0])
  #    add_status(out_grid,_n[0],_n[1],0,WALL_STAT_IO)
  return out_grid


def add_status(maze,cell_x,cell_y,wall,status):
  othercell = None
  otherwall = None
  if wall == WALL_N and cell_y-1 >=0:
      othercell = (cell_x,cell_y-1)
      otherwall = (wall + 2) % 4
  elif wall == WALL_S and cell_y+1 < len(maze[0]):
      othercell = (cell_x,cell_y+1)
      otherwall = (wall + 2) % 4
  elif wall == WALL_W and cell_x-1 >=0:
      othercell = (cell_x-1,cell_y)
      otherwall = (wall + 2) % 4
  elif wall == WALL_E and cell_x+1 < len(maze[0]):
      othercell = (cell_x+1,cell_y)
      otherwall = (wall + 2) % 4

  print ('s',status)
  maze[cell_y][cell_x] |= (wall << 4) 
  maze[cell_y][cell_x] |= (status << 6) 

  if othercell:
      print ('setting other wall',cell_x,cell_y,othercell)
      maze[othercell[1]][othercell[0]] |= (otherwall << 4) 
      maze[othercell[1]][othercell[0]] |= (status << 6) 
  


