'''
Names = []


def add_name(name):
    Names.append(name)
    print("Added '" + name + "' to list")
    return


def remove_name(name):
    Names.remove(name)
    print("Removed '" + name + "' From list")
    return


def list_length():
    print("List length:" + str(len(Names)))
    return


def print_list():
    print(Names)


def main():
    while True:
        raw = input("Enter one of the following commands: Add, Remove, Length\n$")

        if raw == "Add":
            add_name(input("Enter a name to add: "))
        elif raw == "Remove":
            remove_name(str(input("Enter a name to remove:")))
        elif raw == "Length":
            list_length()
        elif raw == "Print":
            print_list()

        else:
            print("Not a recognized input, try again")
'''
'''
def Log():
line = "user,alex,pass,bio"
db = line.split(",")

def login(usr,pas):
    user = db.index("user") + 1
    password = db.index("pass") + 1
    if usr == db[user] and pas == db[password]:
            print("logged in")

    else: print("Failed to login")

print(db.index("user"))
print(db.index("user")+1)
tempuser = input("Enter your username:\n")
temppass = input("Enter your password: \n")



login(tempuser,temppass)
'''
'''
Poll = {"lists": "mutable list of items", "tuples": "immutable list of items"}
Poll["Dictionaries"] = "Array of items with keys"
Poll["Print"] = "Outputs data to the screen"

for term, detail in Poll.items():
    if term == "Print":
        print(term + " is a Python function that " + detail)
    else:
        print(term + " is a Python function that is a " + detail)

exit()  
'''
'''
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
'''
'''
# Make an empty list for storing aliens
aliens = []

# make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)

print("...")

# Show how many aliens have been created.
print("Total number of aliens:" + str(len(aliens)))

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = "red"
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 aliens:
for alien in aliens[0:5]:
    print(alien)
print('...')
'''
'''
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },

}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info["location"]

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
 '''
'''
people = {
    'alex': {
        'favoritefood': 'Sushi',
        'favoritecolor': 'Green',
        'favoritenumber': 3,
    },
    'tony': {
        'favoritefood': 'Honey Ham',
        'favoritecolor': 'Blue',
        'favoritenumber': 'Unknown',
    },
    'steve': {
        'favoritefood': 'Fajitas',
        'favoritecolor': 'Blue',
        'favoritenumber': 'Unknown'

    },
}

for person, fact in people.items():
    print("\nFor " + person.title() + ", Their favorite food is " + fact['favoritefood'].title()
          + ", they love the color " + fact['favoritecolor'] + " and they their lucky number is " +
          str(fact['favoritenumber']) + ".")
print("\n More Facts to come soon!")
'''
'''
favorite_places = {
    'alex': 'Punta Cana',
    'tony': 'Punta Cana',
    'steve': 'Mexico'
}

for people in favorite_places.keys():
    print(people.title() + "'s favorite place is " + favorite_places[people])
'''

'''
def city_country(city, country):
    cityformated = city.title() + ", " + country.title()
    return cityformated

active = True

while active:
    cityraw = input("Please enter a city: ")
    if cityraw.lower() == "q":
        quit()
    countryraw = input("Please enter a country: ")
    if countryraw.lower() == "q":
        quit()
    print(city_country(cityraw, countryraw))  
'''
'''
active = True


def make_album(partist,palbum,ptotalsong=''):
    # Functions takes parameters and makes a dictionary out of them
    if ptotalsong:
        album = {partist: palbum, 'Tracks': ptotalsong}
        return album
    else:
        album = {partist: palbum}
        return album

promt = "Please Enter an artist followed by and album, When you are finished type quit"
print(promt)


while active:
    # Main loop for function call
    raw_artist = input("Please Enter an artist: ")
    if raw_artist == "quit":
        quit()
    raw_album = input("Please Enter an album: ")
    if raw_album == "quit":
        quit()
    raw_tracks = input("Do you know the number of tracks ?, if not leave empty")
    if raw_tracks:
        songs = make_album(raw_artist,raw_album,raw_tracks)
        print(songs)
    else:
        songs = make_album(raw_artist, raw_album)
        print(songs)

'''

'''
def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = "hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
'''


# Start with some designs that need to printed.


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing. 
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""

    print("\nThe following models have been printed: ")

    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
