import random

import requests


# randomly picks a pokemon using a random id number from 1 to 151
# returns the name, id, height and weigh of the pokemon
def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight']
    }


def run():
    # displays the stats for the users' card
    my_pokemon = random_pokemon()
    print('Your card:')
    print('NAME      {}'.format(my_pokemon['name']))
    print('ID        {}'.format(my_pokemon['id']))
    print('WEIGHT    {}'.format(my_pokemon['height']))
    print('HEIGHT    {}'.format(my_pokemon['weight']))
    print('')

    stat_choice = input('Which stat do you want to use? (id, height or weight) ')
    print('')

    opponent_pokemon = random_pokemon()

    print('Opponent card:')
    print('NAME      {}'.format(opponent_pokemon['name']))
    print('ID        {}'.format(opponent_pokemon['id']))
    print('WEIGHT    {}'.format(opponent_pokemon['height']))
    print('HEIGHT    {}'.format(opponent_pokemon['weight']))
    print('')

    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]
    if my_stat > opponent_stat:
        print('You Win!')
    elif my_stat < opponent_stat:
        print('You Lose!')
    else:
        print('Draw!')


run()
