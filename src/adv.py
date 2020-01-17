from cave import Cave
from player import Player

# Declare all the rooms
cave = {
    'outside':  Cave("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Cave("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Cave("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Cave("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Cave("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together
cave['outside'].north_to = cave['foyer']
cave['foyer'].south_to = cave['outside']
cave['foyer'].north_to = cave['overlook']
cave['foyer'].east_to = cave['narrow']
cave['overlook'].south_to = cave['foyer']
cave['narrow'].west_to = cave['foyer']
cave['narrow'].north_to = cave['treasure']
cave['treasure'].south_to = cave['narrow']

#
# Main
#
# Player starts outside of cave entrance
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Player name input
player = Player(input("What's your name? "), cave["outside"])
print(player.current_room)

# Possible directions
directions = ["north", "south", "east", "west"]

# This is a basic REPL loop
while True:
    # input to lowercase, prepended with >>>
    cmd = input(") input command >>> ").lower()
    if cmd in directions:
        player.travel(cmd)
    elif cmd == "q":        # q quits the game
        print("Thanks for playing!")
        exit()
    else:
        print("Please input north, south, east, west, or q")
