STATE = 'state'
FLAGGED = 'flagged'
def fixLoc(loc):
    return loc[0] -1, loc[1] -1

def click(game_state, loc):
    """
    list<list<dict>>, list<int> -> list<list<dict>>
    modifies game_state and returns modified game_state after the cell is
    clicked
    :param game_state: game_state as defined in generator.py
    :param loc: the (x, y) location of the cell you want to click
    :returns: gamestate after the cell at provided loc is clicked
    """
    
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
