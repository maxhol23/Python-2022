############################
#IMPORTS
############################
from adventurelib import  *
import time
############################
#DEFINE ROOMS
############################
Room.items = Bag()

living_room = Room("You are in the living room, A ripped up art piece lies in the corner of the crispy cold room ")
library = Room("You are in the library, a books falls cauing a flurry of dust to appear")
kitchen = Room("You are in the Kitchen, a tub of mayonaise awaits you with on an old, bloodied table top")
hallway = Room("You are in the Hallway, two wooden doors lie to the left and right of you")
bedroom_1 = Room("You enter an old looking bedroom and see a a bristleless broom stick pointing to an piece of a painting")
bedroom_2 = Room("You enter the room with a faint sight of a pair of gloves hiding under a pillow and a locked glass container holding a sledge hammer, it looks like it needs a key to open it")
pool = Room("You enter the pool with a glass screw top container bouncing in the corner of the pool surrounded by bubbles")
art_room = Room("You are in the art room and the walls begin to shrink in front of you, if only you could lodge it.")
treasure_room = Room("You are in the treasure room and piles of gold surround you with the addition of some mayonaise. Congratulations.")
hallway = Room("You stand in the hallway with 2 unknown doors to your left and right")
############################
#DEFINE CONNECTIONS
############################
living_room.north = hallway
hallway.west = bedroom_1
hallway.east = bedroom_2
living_room.west = kitchen
living_room.east = pool
pool.east = art_room
living_room.south = library
living_room.south = treasure_room

############################
#DEFINE ITEMS
############################
Item.description = ""
rubber_gloves = Item("rubber gloves","gloves",)
rubber_gloves.description = "You look at the rubber gloves that contain some red stains"
art_piece_1 = Item("ripped up art piece","art piece","ripped up piece of art","art","piece of art","ripped up art")
art_piece_2 = Item("ripped up art piece","art piece","ripped up piece of art","art","piece of art","ripped up art")
art_piece_3 = Item("ripped up art piece","art piece","ripped up piece of art","art","piece of art","ripped up art")
art_piece_4 = Item("ripped up art piece","art piece","ripped up piece of art","art","piece of art","ripped up art")
art_piece_1.description = "You look at the ripped up art piece."
art_piece_2.description = "You look at the ripped up art piece."
art_piece_3.description = "You look at the ripped up art piece."
art_piece_4.description = "You look at the ripped up art piece."
sledge_hammer = Item("sledge hammer","hammer")
sledge_hammer.description = "You look at the sledge_hammer."
glass_table = Item("glass table","table","glass")
glass_table.description = "You look at the glass table and it looks like you can put some art on it."
broomstick = Item("broom stick","broom","bristleless broomstick","bristleless broom")
broomstick.description = "You look at the broomstick"
mayonaise_tub = Item("mayonaise","mayonaise tub","tub of mayonaise","mayo","mayo tub","tub of mayo")
mayonaise_tub.description = "You look at the tub of mayonaise and you notice a small piece of paper hanging from under the tub"
book = Item("book","book on the ground")
book.description = "You look at the book on the ground and notice that there is shiny metallic objet lying within it"
sledge_hammer_key = Item("key","key in book","key in the book")
sledge_hammer_key.description = "You look at the key"
acid_key = Item("key","key in water","key in acid water","key in acid")
acid_key.description = "You look at the container and notice a key inside of it"

############################
#DEFINE BAGS
############################
inventory = Bag()
Room.items = Bag()

############################
#ADD ITEMS TO BAGS
############################


kitchen.items.add(mayonaise_tub)
living_room.items.add(art_piece_1)
bedroom_1.items.add(broomstick)
bedroom_1.items.add(art_piece_2)
bedroom_2.items.add(rubber_gloves)
bedroom_2.items.add(sledge_hammer)
library.items.add(sledge_hammer_key)
pool.items.add(acid_key)
art_room.items.add(art_piece_4)
library.items.add(art_piece_3)

############################
#DEFINE ANY VARIABLES
############################
game_start = True
current_room = living_room




############################
#BINDS (eg"@when("look"))
############################
if game_start == True:
	print("You wakeup with a letter in your pocket. It states that somewhere amongst the house is millions of dollars. A piece of art\nlies in the corner, you will need four of these too get the code to ultimately unlock the room to get all of the moolah.")
	game_start = False

@when("look")
def look():
	global current_room
	print(current_room)
	exits_amount = int(len(current_room.exits()))
	if exits_amount == 1:
		#grammatically correct way of saying there is one exit
		print(f"You can see exits to the {', '.join(current_room.exits())}")
	elif exits_amount > 1:
			#grammatically correct way of saying there is more than one exit
		print(f"You can see exits to the {', '.join(current_room.exits()[:-1]) + ' and ' + current_room.exits()[-1]}")
	else:
		print("You can't see any exits")
    

@when("DIRECTION")
@when("go DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f'You go {direction}.')
		print(current_room)
	else:
		print("You cannot go that way")


@when("inventory")
@when("show inventory")
@when("what is in my pocket")
def player_inventory():
	print("you are carrying")
	for item in inventory:
		print(item)



############################
#BINDS FOR ITEMS
############################
@when("get ITEM")
@when("take ITEM")
def get_item(item):
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the item")
	else:
		print(f"You don't see a {item}")

@when("look at ITEM")
def look_at (item):
	if item in inventory:
		t = inventory.find(item)
		print(t.description)
	else:
		print(f"You aren't carrying a {item}")




############################
#MAIN FUNCTION
############################

def main():
	start()
	#Start the main loop
main()