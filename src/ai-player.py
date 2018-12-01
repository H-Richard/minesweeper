import generator as gen
import actions as ac
import random
import checks
random.seed(101)

STATE = 'state'
CLICKED = 'clicked'

def randClick(game_state):
    rand_row = random.randint(0, len(game_state))
    rand_cell = random.randint(0, len(game_state[0]))
    ac.click(game_state, (rand_row, rand_cell))

def countClicks(game_state):
    clicks = 0
    for row in game_state:
        for cell in row:
            if cell[STATE] == CLICKED:
                clicks += 1
    return clicks

def getCells(game_state):
    res = []
    for i in range(len(game_state)):
        for j in range(len(game_state[0])):
                res.append([i, j])
    return res

def untouched(game_state, loc):
    a, b = ac.fixLoc(loc)
    cell = game_state[a][b]
    return cell[STATE] == ''

def clicked(game_state, loc):
    a, b = ac.fixLoc(loc)
    cell = game_state[a][b]
    return cell[STATE] == CLICKED

def onBorder(game_state, loc):
    locs = ac.neighbours(game_state, loc)
    locs = [loc for loc in locs if untouched(game_state, loc)]
    return locs

def uWin(game_state):
    if checks.won(game_state):
        print('you win')
        exit()

def uLost(game_state):
    if checks.lost(game_state):
        print('you lost')
        exit()

def bigCheck(game_state):
    uWin(game_state)
    uLost(game_state)

def play(game_state):
    """
    -> solved game
    """
    # early game
    gen.render(game_state)
    while countClicks(game_state) < round(len(game_state) * len(game_state[0]) * 0.05):
        bigCheck(game_state)
        randClick(game_state)
        gen.render(game_state)

    # mid game
    for i in range(50):
        bigCheck(game_state)
        ch_percent = 0
        ch_loc = 0
        cl_percent = 1
        cl_loc = 1

        border_locs = getCells(game_state)
        border_locs = [loc for loc in border_locs if clicked(game_state, loc)]
        border_locs = [loc for loc in border_locs if onBorder(game_state, loc)]
        for loc in border_locs:
            ney = ac.neighbours(game_state, loc)
            neyWithFlags = len([loc for loc in ney if ac.isFlagged(game_state, loc)])
            ney = [loc for loc in ney if untouched(game_state, loc)]

            new_percent = (get_cell(game_state, loc)['neigh'] - neyWithFlags) / len(ney)
            print(f'loc {ney[0]} percent {new_percent}')
            if  new_percent > ch_percent:
                ch_percent = new_percent
                ch_loc = ney[0]
            if new_percent < cl_percent:
                cl_percent = new_percent
                cl_loc = ney[0]
        if ch_percent == 1:
            ac.flag(game_state, ch_loc)
            gen.render(game_state)
        else:
            ac.click(game_state, cl_loc)
            gen.render(game_state)


def get_cell(game_state, loc):
    a, b = ac.fixLoc(loc)
    return game_state[a][b]

if __name__ == '__main__':
    game_state = gen.generation(10, 10, 10)
    gen.render(game_state, show_bombs=True)
    play(game_state)
