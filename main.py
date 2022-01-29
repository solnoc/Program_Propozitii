from entrances import *

inp = '0'
while(inp != '9'):
	clear()
	print("Please select what you want to do:")
	print("Press 0 to enter input mode")
	print("Press 1 to check the strings and propositions currently in storage")
	print("Press 2 to check a cleaned string format and create the abstruct structure")
	print("Press 3 to place paranthases on a relaxed proposition and create the abstruct structure")
	print("Press 4 if you want to create the truth table for a proposition currently in storage")
	print("Press 9 to exit the program")
	inp = input("Select numer: ")
	clear()
	while inp == '0':
		inp = press_0()
	while inp == '1':
		inp = press_1()
	while inp == '2':
		inp = press_2()
	while inp == '3':
		inp = press_3()
	while inp == '4':
		inp = press_4()
			
			
