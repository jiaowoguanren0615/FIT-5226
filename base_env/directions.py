class Directions:

    NORTH = 'North'
    SOUTH = 'South'
    EAST = 'East'
    WEST = 'West'
    STOP = 'Stop'

    LEFT = {
        NORTH: WEST,
        SOUTH: EAST,
        EAST:  NORTH,
        WEST:  SOUTH,
        STOP:  STOP
    }

    RIGHT = dict([(y,x) for x, y in LEFT.items()])

    REVERSE = {
        NORTH: SOUTH,
        SOUTH: NORTH,
        EAST: WEST,
        WEST: EAST,
        STOP: STOP
    }

    actions_mapping = {
        NORTH: 1,
        SOUTH: 2,
        EAST:  3,
        WEST:  4,
        STOP:  0
    }