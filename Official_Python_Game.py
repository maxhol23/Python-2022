############################
#IMPORTS
############################


############################
#DEFINE ROOMS
############################
Living_Room = Room("You are in the living room, A ripped up art piece lies in the corner of the crispy cold room ")
Library = Room("You are in the library, a books falls cauing a flurry of dust to appear")
Kitchen = Room("You are in the Kitchen, a tub of mayonaise awaits you with on an old, bloodied table top")
Hallway = Room("You are in the Hallway, two wooden doors lie to the left and right of you")
Bedroom_1 = Room("You enter an old looking bedroom and see a a bristleless broom stick pointing to an piece of a painting")
Bedroom_2 = Room("You enter the room with a faint sight of a pair of gloves hiding under a pillow and a glass container holding a sledge hammer, it looks like it needs a key to open it")
Pool = Room("You enter the pool with a glass screw top container bouncing in the corner of the pool surrounded by bubbles")
Art_room = Room("You are in the art room and the walls begin to shrink in front of you, if only you could lodge it.")
Treasure_room = Room("You are in the treasure room and piles of gold surround you with the addition of some mayonaise. Congratulations.")

############################
#DEFINE CONNECTIONS
############################
Living_room.north = Hallway
Hallway.west = Bedroom_1
Hallway.east = Bedroom_2
Living_room.west = Kitchen
Living_room.east = Pool
Pool.east = Art_room
Living_room.south = Library
Living_room.south = Treasure_room

############################
#DEFINE ITEMS
############################
Items.description = ""
rubber_gloves = Item("rubber gloves","gloves",)
rubber_gloves.description = "You look at the rubber gloves"






############################
#DEFINE BAGS
############################


############################
#ADD ITEMS TO BAGS
############################


############################
#DEFINE ANY VARIABLES
############################


############################
#BINDS (eg"@when("look"))
############################


############################
#MAIN FUNCTION
############################
