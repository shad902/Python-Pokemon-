import csv
from random import randint
from random import seed
from copy import deepcopy
from pokemon import Pokemon
from pokemon import Move
seed(1) #Set the seed so that the same events always happen
#DO NOT CHANGE THIS!!!
# =============================================================================
element_id_list = [None, "normal", "fighting", "flying", "poison", "ground",
"rock",
 "bug", "ghost", "steel", "fire", "water", "grass",
"electric",
 "psychic", "ice", "dragon", "dark", "fairy"]
#Element list to work specifically with the moves.csv file.
# The element column from the moves.csv files gives the elements as integers.
# This list returns the actual element when given an index
# =============================================================================
def read_file_moves(fp):
    '''WRITE DOCSTRING HERE!!!'''
    ignore= fp.readline()
    movelst = []
    for line in fp:
        line = line.strip('\n')
        a = line.split(',')
        if a[2]!='1':
            continue
        if a[9]=='1':
            continue
        try:
            m = Move(a[1], element_id_list[int(a[3])], int(a[4]), int(a[6]),int(a[9]))
            movelst.append(m)
        except:
            pass
    return movelst
def read_file_pokemon(fp):
    '''WRITE DOCSTRING HERE!!!'''
    pokemonlst = []
    idset = set()
    ignore = fp.readline()
    for line in fp:
        line = line.strip('\n')
        a = line.split(',')
        if a[11] != '1':
            continue
        if a[0] not in idset:
            try:
                pokemon = Pokemon(a[1].lower(), a[2].lower(), a[3].lower(),None,int(a[5]), int(a[6]), int(a[7]), int(a[8]), int(a[9]))
                pokemonlst.append(pokemon)
                idset.add(a[0])
            except:
                pass
    return pokemonlst
def choose_pokemon(choice,pokemon_list):
    '''WRITE DOCSTRING HERE!!!'''
    if choice.isnumeric():
        if int(choice)<1 or int(choice)>len(pokemon_list):
            return None
        index = int(choice) - 1
        return deepcopy(pokemon_list[index])
    else:
        for pokemon in pokemon_list:
            if pokemon.get_name().lower() == choice.lower():
                return deepcopy(pokemon)
        return None
def add_moves(pokemon,moves_list):
    '''WRITE DOCSTRING HERE!!!'''
    move = moves_list[randint(0, len(moves_list) - 1)]
    pokemon.add_move(move)
    times = 0
    added = []
    added.append(move)
    while times < 200:
        move = moves_list[randint(0, len(moves_list) - 1)]
        if move not in pokemon.get_moves():
            if move.get_element() == pokemon.get_element1() or move.get_element() == pokemon.get_element2():
                pokemon.add_move(move)
                added.append(move)
        if len(added)==4:
            break
        times += 1
    if len(added)==4:
        return True
    return False
    
def turn (player_num, player_pokemon, opponent_pokemon):
    '''WRITE DOCSTRING HERE!!!'''
    print("Player {}'s turn".format(player_num))
    print(player_pokemon)
    while True:
        print("Show options: 'show ele', 'show pow', 'show acc'")
        opt = input("Select an attack between 1 and {} or show option or 'q':".format(len(player_pokemon.get_moves())))
        if opt == 'q':
            return 'q'
        if opt == 'show ele':
            line = ''
            for move in player_pokemon.get_moves():
                line+='{:<15s}'.format(move.get_element())
            print(line)
        if opt == 'show pow':
            line = ''
            for move in player_pokemon.get_moves():
                line+='{:<15d}'.format(move.get_power())
        print(line)
    if opt == 'show acc':
        line = ''
        for move in player_pokemon.get_moves():
            line += '{:<15d}'.format(move.get_accuracy())
        print(line)
    if opt.isnumeric():
        index = int(opt)-1
        move = player_pokemon.get_moves()[index]
        print('selected move: {}'.format(move.get_name()))
        print('{} hp before:{}'.format(opponent_pokemon.get_name(),opponent_pokemon.get_hp()))
        player_pokemon.attack(move, opponent_pokemon)
        print('{} hp after:{}'.format(opponent_pokemon.get_name(),opponent_pokemon.get_hp()))
        return None
def play1choose(pokemons):
    pokemon = None
    while pokemon is None:
        choice = input('Player 1, choose a pokemon by name or index: ')
        pokemon = choose_pokemon(choice, pokemons)
    print("pokemon1:")
    print(pokemon)
    return pokemon
def play2choose(pokemons):
    pokemon = None
    while pokemon is None:
        choice = input('Player 2, choose a pokemon by name or index: ')
        pokemon = choose_pokemon(choice, pokemons)
    print("pokemon2:")
    print(pokemon)
    return pokemon
    
def main():
    usr_inp = input("Would you like to have a pokemon battle? ").lower()
    while usr_inp != 'n' and usr_inp != 'q' and usr_inp != 'y':
        usr_inp = input("Invalid option! Please enter a valid choice: Y/y, N/n or Q/q: ").lower()
    if usr_inp != 'y':
        print("Well that's a shame, goodbye")
        return
    else:
        fp1 = open('moves.csv')
        fp2 = open('pokemon.csv')
        moves = read_file_moves(fp1)
        pokemons = read_file_pokemon(fp2)
        fp1.close()
        fp2.close()
        while True:
            p1 = play1choose(pokemons)
            p2 = play2choose(pokemons)
            add_moves(p1, moves)
            add_moves(p2, moves)
            while True:
                if turn(1, p1, p2)=='q':
                    print("Player 1 quits, Player 2 has won the pokemon battle!")
                    break
                else:
                    if p2.get_hp() <= 0:
                        print("Player 2's pokemon fainted, Player 1 has won the pokemon battle!")
                        break
                if turn(2, p2, p1)=='q':
                    print("Player 2 quits, Player 1 has won the pokemon battle!")
                    break
                else:
                    if p1.get_hp() <= 0:
                        print("Player 1's pokemon fainted, Player 2 has won the pokemon battle!")
                        break
                print('Player 1 hp after: {}'.format(p1.get_hp()))
                print('Player 2 hp after: {}'.format(p2.get_hp()))
            usr_inp = input('Battle over, would you like to have another?').lower()
            if usr_inp!='y':
                print("Well that's a shame, goodbye")
                break
if __name__ == "__main__":
    main()



        
        

                
                
                
                
                