# Project: Pokemon Characters Application


# Install the required packages
# pip install requests

# Import the required modules
import requests

while True:

    # User input Pokemon characters
    print("\nWhich Pokemon character do you want to find? ")
    print("""
        **********************
        -> ditto
        -> bulbasaur
        -> charmander
        -> charmeleon
        -> charizard
        -> squirtle
        -> pikachu
        -> dragonite
        **********************
    """)

    pokemon = input("Your Choice: ")

    # We assign it because strings are immutables
    pokemon = pokemon.lower()

    # Dynamic URL
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    # Fetch the data from URL
    response = requests.get(url)

    # Check HTTP Status Code
    if response.status_code == 200:
        # JSON Data
        data = response.json()

        # Print out the character's data in the form of dictionary
        print(f"Name:\t\t{data['name']}")
        print("Abilities:")
        for ability in data['abilities']:
            print(ability['ability']['name'])

    else:
        print("Pokemon not found!")
        break
