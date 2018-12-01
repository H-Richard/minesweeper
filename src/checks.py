def lost(gamestate: [[{}]]) -> bool:
    """

    :param gamestate:
    :return:
    """

    for row in gamestate:
        for block in row:
            if block['state'] == 'clicked' and block['mine'] == 1:
                return True
    return False

def won(gamestate: [[{}]]) -> bool:
    """

    :param gamestate:
    :return:
    """

    for row in gamestate:
        for block in row:
            if block['state'] == 'clicked' and block['mine'] == 1:
                return False
            if block['state'] == '' and block['mine'] == 0:
                return False
    return True

