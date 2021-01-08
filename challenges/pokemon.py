#!/usr/bin/env python3

# imports always go at the top of your code
import requests, wget

def main():
    print("\nWelcome to pokemonapi. Press q to quit anytime\n")
    while True:
        user_poke = input("\nWhat pokemon do you wanna find?... Use name or pokedex number\n").lower()
        if user_poke == "q":
            exit()
        pokeapi = requests.get(f"https://pokeapi.co/api/v2/pokemon/{user_poke}")
        if pokeapi.status_code != 200:
            print("Sorry thats not a correct input")
            continue
        pokeapi = pokeapi.json()
        wget.download(pokeapi["sprites"]["front_default"])
        print(f"\n{pokeapi['species']['name'].capitalize()} is in {len(pokeapi['game_indices'])} games. I went ahead and downloaded a pic for you bud.\n\nAlso, here are {pokeapi['species']['name'].capitalize()}'s moves:")
        moves = ""
        for move in pokeapi['moves']:
            moves += move['move']['name']+", "
        print(moves)


main()
