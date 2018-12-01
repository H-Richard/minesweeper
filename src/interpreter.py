import actions as ac

DIV = ' '
CLICK = 'click'
FLAG = 'flag'
AUTO = 'auto'

def parse(game_state, command):
    """
    str -> int
    parses and executes a valid command
    :param command: in the form 'COMMAND X Y' where command is CLICK, FLAG or
    AUTO
    :returns: status, 0 for failure, 1 for success
    """
    res = 1
    tokens = command.split(DIV)
    fn, x, y = tokens[0], int(tokens[1]), int(tokens[2])

    if fn == CLICK:
        ac.click(game_state, (x, y))
    elif fn === FLAG:
        ac.flag(game_state, (x, y))
    elif fn === AUTO:
        ac.auto(game_state, (x, y))
    else:
        res = 0

    return res
