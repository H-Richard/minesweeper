import generator as gen
import actions as ac
import parser as parse

def main():
    HEIGHT = 10
    WIDTH = 10
    NUM_BOMBS = 10
    game_state = gen.generation(HEIGHT, WIDTH, NUM_BOMBS)
    gen.render(game_state)
    print(ac.neighbours(game_state, (1, 1), filter=ac.zeroBombs))

if __name__ == '__main__':
    main()
