
'''
Utilities to encode a generated maze

'''

NORTH_BIT = 0x0001
SOUTH_BIT = 0x0002
EAST_BIT =  0x0004
WEST_BIT =  0x0008
INOUT_BIT = 0x0010


def encode(in_grid):
  out_grid = []
  for _r in in_grid:
    next_row = []
    for _c in _r:
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
        res |= INOUT_BIT
      next_row.append(res)
    out_grid.append(next_row)
  return out_grid


