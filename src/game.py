import generator as gen
import actions as ac
import interpreter as inter
import checks as ck

def main():
    print('enter height width number_bombs')

    tokens = input().split(' ')
    tokens = [int(x) for x in tokens]
    HEIGHT, WIDTH, NUM_BOMBS = tokens

    game_state = gen.generation(HEIGHT, WIDTH, NUM_BOMBS)
    gen.render(game_state)
    # gen.render(game_state, show_bombs=True) # for debugging

    while True:
        print('input a command')
        command = input()
        inter.parse(game_state, command)
        gen.render(game_state)

        if ck.won(game_state):
            print('Congratulations! You won!')
            break
        if ck.lost(game_state):
            gen.render(game_state, show_bombs=True)
            print('Feels bad man, you lost!')
            break


if __name__ == '__main__':
    main()
