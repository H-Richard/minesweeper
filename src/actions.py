STATE = 'state'
FLAGGED = 'flagged'
NEIGH = 'neigh'
MINE = 'mine'
CLICKED = 'clicked'

def fixLoc(loc):
    return loc[0] -1, loc[1] -1

def inBound(game_state, loc):
    """
    a filter for neighbours
    """
    x_in_bounds = loc[0] > 0 and loc[0] <= len(game_state[0])
    y_in_bounds = loc[1] > 0 and loc[1] <= len(game_state)
    return x_in_bounds and y_in_bounds

def zeroBombsNotBomb(game_state, loc):
    loc = fixLoc(loc)
    cell = game_state[loc[0]][loc[1]]
    return cell[NEIGH] == 0 and not cell[MINE]

def isBomb(game_state, loc):
    loc = fixLoc(loc)
    cell = game_state[loc[0]][loc[1]]
    return cell[MINE]

def hasNeigh(game_state, loc):
    a, b = fixLoc(loc)
    cell = game_state[a][b]
    return cell[NEIGH] > 0

def notClicked(game_state, loc):
    loc = fixLoc(loc)
    cell = game_state[loc[0]][loc[1]]
    return cell[STATE] != CLICKED

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

def isFlag(game_state, loc):
    a, b = fixLoc(loc)
    cell = game_state[a][b]
    return cell[STATE] == FLAGGED


def click(game_state, loc):
    """
    list<list<dict>>, list<int> -> list<list<dict>>
    modifies game_state and returns modified game_state after the cell is
    clicked
    :param game_state: game_state as defined in generator.py
    :param loc: the (x, y) location of the cell you want to click
    :returns: gamestate after the cell at provided loc is clicked
    """
    oLoc = loc
    loc = fixLoc(loc)
    cell = game_state[loc[0]][loc[1]]
    if isFlag(game_state, oLoc):
        return
    elif isBomb(game_state, oLoc):
        cell[STATE] = CLICKED
    elif hasNeigh(game_state, oLoc):
        cell[STATE] = CLICKED
    else:
        cell[STATE] = CLICKED
        for neighbour in neighbours(game_state, oLoc):
            if notClicked(game_state, neighbour):
                click(game_state, neighbour)

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

def isFlagged(game_state, loc):
    return None

def auto(game_state, loc):
    """
    list<list<dict>>, list<int> -> list<list<dict>>
    modifies game_state and returns modified game_state after auto is invoked
    on the cell
    :param game_state: game state as defined in generator.py
    :param loc: the (x, y) location of the cell you want to invoke auto on
    :returns: game_state after auto is invoked on the cell
    """
    list = neighbours(game_state, loc, filter=None)
    #loc = fixLoc(loc)
    cell = game_state[loc[0]][loc[1]]
    cell_number = game_state[loc[0]][loc[1]][NEIGH]
    cell_state = game_state[loc[0]][loc[1]][STATE]

    neigh_flag_count = 0

    print(list)
    print(cell_state)

    if cell[STATE] != FLAGGED:
        for neigh in list:
            neigh = fixLoc(neigh)
            neigh = game_state[neigh[0]][neigh[1]]
            if neigh[STATE] == FLAGGED:
                print("flag 1")
                neigh_flag_count +=1

        print(neigh_flag_count)
        if cell_number == neigh_flag_count:
            print("equal")
            for neigh in list:
                neigh = fixLoc(neigh)
                neigh = game_state[neigh[0]][neigh[1]]
                if neigh[STATE] != FLAGGED:
                    print(neigh)
                    click(game_state,neigh)
        else:
            print("not equal")
    return None
