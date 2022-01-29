letters = [chr(x) for x in range(ord('A'),ord('Z'))]
allowed = letters[:]
allowed.extend(['neg','con','dis','imp','equ','¬','∨','∧','⇒','⇔','(',')'," "])

i=0
def check_propositional_format(st,d):
	if len(st) > 1 and st[0] != '(':
		return ("String is not a well formed formula because it has more than 1 symbol and it does not start with '('",False)
	reset_i()
	if d == 0:
		return check_p(st)
	elif d == 1:
		print("We are checking: " + st)
		return check_p_steps(st)
	elif d == 2:
		return check_p(st)
	elif d == 3:
		print("We are checking: " + st)
		return check_p_steps(st)
	
def check_p_steps(st):
	global i
	if i >= len(st):
		return ("An overflow has occured",False)
	if st[i] in letters:
		print("We found "+ st[i] + ", witch is a proposition and we will use it further")
		i += 1
		return [st[i-1]]
	elif st[i] != '(':
		return ("Expected '(' or uppercase letter",False)
	elif i+1 >= len(st):
		return ("We found '(', but the string ends right after",False)
	elif st[i+1] == '¬':
		row = ['¬','p']
		print("Sience we found '(' and '¬', we are looking now for a proposition in the next position in the string to put in the position of p in " + str(row))
		i += 2
		row[1] = check_p_steps(st)
		if len(row[1]) == 2 and row[1][1] == False:
			print(row[1][0] + ", so we did not find the proposition we were looking for, the string is not a well formed formula")
			return row[1]
		else:
			print("The proposition found has a good form, this is it: " + str(row[1]))
			if st[i] != ')':
				print(str(row) + " is well formed until here ,but the next charachter is not a ')', so the string is not a well formed formula")
				return (row,False)	
			print("We found ')' and now our formula is complete")
			i += 1
			print(str(row) + "is a well formed formula and we can use it further")
			return row
	else:	
		row = ['s','p1','p2']
		print("Sience we found '(', and the charachter after is not '¬', we are looking now for a proposition in the next position in the string to put in the position of p1 in " + str(row))
		i += 1
		row[1] = check_p_steps(st)
		if len(row[1]) == 2 and row[1][1] == False:
			print(row[1][0] + ", so we did not find the proposition we were looking for, the string is not a well formed formula") 
			return (row[1][0],False)

		print("The proposition found has a good form, this is it: " + str(row[1]))
		print("Now we are looking for a binary logical connective in the next position of the string")
		if i >= len(st):
			print("We have to stop looking because we got to the end of the string and the formula is incomplete, that means the string is not a well formed formula")
			return ("We did not find a binary logical connective because we got to the end of the string",False)
		if not st[i] in ['∨','∧','⇒','⇔']:
			print("The next charachteer in the string is not a bynari logical connective, so the string is not a well formed formula")
			return ("Expected an binary logical conenctive, but we found " + str(st[i]),False)
		row[0] = st[i]
		print("We found " + st[i] + " witch is a bynary logical connective and we plugged it in the position of s, now we are looking for another proposition to put in place of p2 in " + str(row))
		i += 1
		row[2] = check_p_steps(st)
		if len(row[2]) == 2 and row[2][1] == False:
			print(row[2][0] + ", so we did not find the proposition we were looking for, the string is not a well formed formula")
			return (row[2][0], False)
		print("The proposition found has a good form, this is it: " + str(row[2]))
		print("Now we are looking for ')'")
		if i >= len(st):
			print("We have to stop looking because we got to the end of the string and the formula is incomplete, that means the string is not a well formed formula")
			return ("We did not find a ')' because we got to the end of the string",False)
		if st[i] != ')':
			print(str(row) + " is well formed until here ,but the next charachter is not a ')', so the string is not a well formed formula")
			return (row,False)
		print("We found ')' and now our formula is complete")
		i += 1
		print(str(row) + "is a well formed formula and we can use it further")
		return row
def check_p(st):
	global i
	if i >= len(st):
		return ("Error",False)
	if st[i] in letters:
		i += 1
		return [st[i-1]]
	elif st[i] != '(':
		return ("Error",False)
	elif i+1 >= len(st):
		return ("Error",False)
	elif st[i+1] == '¬':
		row = ['¬','p']
		i += 2
		row[1] = check_p(st)
		if len(row[1]) == 2 and row[1][1] == False:
			return ("Error",False)
		else:
			if st[i] != ')':
				return (row,False)	
			i += 1
			return row
	else:	
		row = ['s','p1','p2']
		i += 1
		row[1] = check_p(st)
		if len(row[1]) == 2 and row[1][1] == False:
			return (row[1][0],False)

		if i >= len(st):
			return ("Error",False)
		if not st[i] in ['∨','∧','⇒','⇔']:
			return ("Error",False)
		row[0] = st[i]
		i += 1
		row[2] = check_p(st)
		if len(row[2]) == 2 and row[2][1] == False:
			return ("Error", False)
		if i >= len(st):
			return ("Error",False)
		if st[i] != ')':
			return ("Error",False)
		i += 1
		return row
def reset_i():
	global i
	i = 0
