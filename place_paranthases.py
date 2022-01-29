from check_propositional_format import *

letters = [chr(x) for x in range(ord('A'), ord('Z'))]
def place_paranthases(st,d):
	if type(st) != list:
		st = list(st)
	if '(' in st:
		end = -1
		start = -1
		i = 0
		while i < len(st):
			if st[i] == '(':
				start = i
			if st[i] == ')' and end == -1 and start != -1:
				end = i
				if not return_wff(st,start,end):
					return False
				i = -1
				end = -1
				start = -1
			elif st[i] == ')' and end == -1:
				if d == 1:
					print("Paranthases do not mach, please review your input...")
				return False
				
			i += 1
	
	dis = False
	con = False
	for i in range(len(st)-1,-1,-1):
		if st[i] == '∨':
			dis = True
		elif st[i] == '∧':
			con = True	
		elif st[i] == '⇒' or st[i] == '⇔':
			dis = False
			con = False
			
		if dis and con:
			if d==1:
				print("An ambiguity has been found , please review your input...")
			return False
			
	for i in range(len(st)):
		if st[i] in letters:
			st[i] = [st[i]]

	for i in range(len(st)-1,-1,-1):
		if st[i] == '¬':
			if not add_sym('¬',st,i):
				return False
			if d == 1:
				print(print_string(st))
			
	i = len(st)-1
	while i>=0:
		if st[i] == '∨':
			if not add_sym('∨',st,i):
				return False
			if d == 1:
				print(print_string(st))
			i -= 1
		i -= 1

	i = len(st)-1
	while i>=0:
		if st[i] == '∧':
			if not add_sym('∧',st,i):
				return False
			if d == 1:
				print(print_string(st))
			i -= 1
		i -= 1
	i = len(st)-1
	while i>=0:
		if st[i] == '⇒':
			if not add_sym('⇒',st,i):
				return False
			if d == 1:
				print(print_string(st))
			i -= 1
		i -= 1
		
	i = len(st)-1
	while i>=0:
		if st[i] == '⇔':
			if not add_sym('⇔',st,i):
				return False
			if d == 1:
				print(print_string(st))
			i -= 1
		i -= 1
	if d == 2:
		return st
	
	return print_string(st)

def add_sym(sym,st,i):
	if i == len(st)-1:
		print(str(sym) + " is at the end of the string...")
		return False
	if sym == '¬':
		if type(st[i+1]) == list and (i == 0 or not type(st[i-1]) == list):
			st[i] = ['¬',st[i+1][:]]
			st.pop(i+1)
			return True
		elif not type(st[i+1]) == list:
			print("String can't be parsed because the symbol after negation is " + str(st[i+1]))
			return False
		else:
			print("String can't be parsed because before the negation there is this proposition: " + str(st[i-1]))
	else:
		if type(st[i-1]) == list and type(st[i+1]) == list:
			st[i-1] = [st[i-1][:],sym,st[i+1][:]]
			st.pop(i)
			st.pop(i)
			return True
		elif type(st[i-1]) != list:
			print("String can't be parsed because before the implication symbol there is " + str(st[i-1]))
			return False
		elif type(st[i+1]) != list:
			print("String can't be parsed because after the implication symbol there is " + str(st[i+1]))
			return False
	
def return_wff(st,start,end):
	new_st = []
	for i in range(start+1,end):
		new_st.append(st[i])
	wff = place_paranthases(new_st,2)
	if not wff:
		return False
	st[start] = wff[0]
	for i in range(start,end):
		st.pop(start+1)
	return True

def print_string(st):
	
	x = str(st)
	x = x[:len(x)-1]
	x = x[1:]
	x = x.replace("[","(")
	x = x.replace("]",")")
	x = x.replace("'",'')
	x = x.replace(",",'')
	x = x.replace(" ",'')
	i = 0
	while i<len(x):
		if x[i] in letters:
			x = x[:i-1] + x[i:]
			x = x[:i] + x[i+1:]
			i -= 1
		i += 1
	return x
	
