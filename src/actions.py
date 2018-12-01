STATE = 'state'
FLAGGED = 'flagged'
def fixLoc(loc):
    return loc[0] -1, loc[1] -1


def inBound(game_state, loc):
    """
    a filter for neighbours
    """
    x_in_bounds = loc[0] > 0 and loc[0] <= len(game_state[0])
    y_in_bounds = loc[1] > 0 and loc[1] <= len(game_state)
    return x_in_bounds and y_in_bounds

def neighbours(game_state, loc, filter=None):
    """
    list<list<dict>>, list<int>, function -> list<list<int>>
    """
    x, y = loc
    res = [[x-1, y-1], [x, y-1], [x+1, y-1],
            [x-1, y], [x+1, y],
            [x-1, y+1], [x, y+1], [x+1, y+1]]
    loc = fixLoc(loc)

    res = [loc for loc in res if inBound(game_state, loc)]

    if filter:
        res = [loc for loc in res if filter(game_state, loc)]

    return res

def click(game_state, loc):
    """
    list<list<dict>>, list<int> -> list<list<dict>>
    modifies game_state and returns modified game_state after the cell is
    clicked
    :param game_state: game_state as defined in generator.py
    :param loc: the (x, y) location of the cell you want to click
    :returns: gamestate after the cell at provided loc is clicked
    """
    loc = fixLoc(loc)
    cell = game_state[loc[0]][loc[1]]
    for neighbour in neighbours:
        click(game_state, neighbour)
    return None

def flag(game_state, loc):
    """
    list<list<dict>>, list<int> -> list<list<dict>>
    modifies game_state and returns modified game_state after the cell is
    flagged
    :param game_state: game_state as defined in generator.py
    :param loc: the (x, y) location of the cell you want to click
    :returns: game_state after the cell at loc is flagged
    """
    # flag 15 10
    loc = fixLoc(loc)
    cell = game_state[loc[0]][loc[1]]
    cell[STATE] = FLAGGED
    return game_state

def auto(game_state, loc):
    """
    list<list<dict>>, list<int> -> list<list<dict>>
    modifies game_state and returns modified game_state after auto is invoked
    on the cell
    :param game_state: game state as defined in generator.py
    :param loc: the (x, y) location of the cell you want to invoke auto on
    :returns: game_state after auto is invoked on the cell
    """
    return None
