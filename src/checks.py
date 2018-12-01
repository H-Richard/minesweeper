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
            if block['state'] == 'clicked' and block['mine'] != 1:
                pass
    return True



gamestate = [[{'mine': 0, 'state': 'clicked', 'neigh': 1}, {'mine': 1, 'state': '', 'neigh': 0}], [{'mine': 0, 'state': 'clicked', 'neigh': 1}, {'mine': 0, 'state': 'clicked', 'neigh': 1}]]

if __name__ == "__main__":
    print(lost(gamestate))
    print(won(gamestate))

