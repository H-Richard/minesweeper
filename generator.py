import random


def generation (height:int, width:int, difficulty: int) -> [[{}]]:
    """
    Return list of list of dictionaries with keys 'mine', 'type', Generate int difficulty
    number of mines in the gamestate

    :param difficulty:
    :param height:
    :param width:
    :return:
    """

    gamestate = []
    while len(gamestate) < height:
        gamestate.append([])

    for row in gamestate:
        while len(row) < width:
            row.append({'mine': 0, 'state': ''})

    mine_count = 0
    while mine_count < difficulty:
        random_row = random.randint(0, height - 1)
        random_column = random.randint(0, width - 1)
        if gamestate[random_row][random_column]['mine'] != 1:
            gamestate[random_row][random_column]['mine'] = 1
            mine_count += 1

    final = check_gamestate(gamestate)
    return final


def render(gamestate: [[{}]]) -> [[]]:
    """

    :param gamestate:
    :return:
    """

    x_cord = '   '
    i = 1
    while i <= len(gamestate[0]):
        if len(str(i)) > 1:
            x_cord += str(i) + ' '
        else:
            x_cord += ' ' + str(i) + ' '
        i += 1
    print(x_cord)

    i = 0
    for row in gamestate:
        i += 1
        if len(str(i)) > 1:
            temp = str(i) + ' '
        else:
            temp = ' ' + str(i) + ' '
        for block in row:
            if block['state'] == '':
                temp = temp + '[ ]'
            if block['state'] == 'clicked':
                if block['mine'] == 0:
                    temp = temp + '[' + str(block['neigh']) + ']'
                if block['mine'] == 1:
                    temp = temp + '[' + 'B' + ']'
            if block['state'] == 'flagged':
                temp = temp + '[' + 'f' + ']'
        print(temp)


def check_gamestate (gamestate: [[{}]]) -> [[{}]]:
    """

    :param gamestate:
    :return:
    """
    row_index = 0
    while row_index in range(len(gamestate)):
        block_index = 0
        while block_index in range(len(gamestate[row_index])):
            mine_count = 0

            if row_index - 1 >= 0:
                previous_row = row_index - 1
                if block_index - 1 >= 0:
                    if gamestate[previous_row][block_index - 1]['mine'] == 1:
                        mine_count += 1
                if block_index + 1 < len(gamestate[row_index]):
                    if gamestate[previous_row][block_index + 1]['mine'] == 1:
                        mine_count += 1
                if gamestate[previous_row][block_index]['mine'] == 1:
                    mine_count += 1

            if row_index + 1 < len(gamestate):
                next_row = row_index + 1
                if block_index - 1 >= 0:
                    if gamestate[next_row][block_index - 1]['mine'] == 1:
                        mine_count += 1
                if block_index + 1 < len(gamestate[row_index]):
                    if gamestate[next_row][block_index + 1]['mine'] == 1:
                        mine_count += 1
                if gamestate[next_row][block_index]['mine'] == 1:
                    mine_count += 1

            if block_index - 1 >= 0:
                if gamestate[row_index][block_index - 1]['mine'] == 1:
                    mine_count += 1
            if block_index + 1 < len(gamestate[1]):
                if gamestate[row_index][block_index + 1]['mine'] == 1:
                    mine_count += 1

            gamestate[row_index][block_index]['neigh'] = mine_count
            block_index += 1
        row_index += 1

    return gamestate
