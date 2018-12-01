import generator as gen
import actions as ac
import parser as parse

def main():
    HEIGHT = 10
    WIDTH = 10
    NUM_BOMBS = 30
    game_state = gen.generation(HEIGHT, WIDTH, NUM_BOMBS)
    gen.render(game_state)
    print(ac.neighbours(game_state, (1, 1)))

if __name__ == '__main__':
    main()
