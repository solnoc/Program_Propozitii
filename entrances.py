from input import *
from place_paranthases import *
from give_truth import *
import os
clear = lambda: os.system('clear')

def press_0():
	print("Introduce 'exit' if you want to go back to the menu")
	st = input("Please introduce your proposition: ")
	clear()
	if(st == 'exit'):
		return '-1'
	input_f(st)
	print("")	
	return '0'
	
def press_1():
	print("Introduce 'exit' if you want to go back to the menu")
	print("Introduce 'ls cl' if you want to see all cleaned propositions and their index")
	print("Introduce 'rm cl' followed by the index of the propositions you want to delete from the cleaned propositions")
	print("Introduce 'ls pr' if you want to see all well formed formulas and their index")
	print("Introduce 'rm pr' followed by the index of the propositions you want to delete from the well formed formulas file")
	print("Introduce 'rm dp cl' if you want to delete all duplicates of propositions in the cleaned proposition file")
	print("Introduce 'rm dp pr' if you want to delete all duplicates of propositions in the proposition file")
	st = input("Please introduce: ")
	clear()
	if st == 'exit':
		return '-1'
		
	if st == 'ls cl':
		clean_props = clean_waiting_propositions_values()
		for i in range(len(clean_props)):
			print("[" + str(i) + "]: " + clean_props[i],end='')
		return '1'
		
	if st == 'ls pr':
		abstruct_structures = propositions_values()
		for i in range(len(abstruct_structures)):
			print('[' + str(i) + ']: ' + abstruct_structures[i],end='')
		return '1'
		
	if st[0:5] == 'rm cl':
		if len(st) == 5 or len(st) == 6:
			return '1'
		clean_waiting_propositions_remove(int(st[6:]))
		print("Proposition deleted succesfuly!")
		return '1'
		
	if st[0:5] == 'rm pr':
		if len(st) == 5 or len(st) == 6:
			return '1'
		propositions_remove(int(st[6:]))
		print("Proposition deleted succesfuly!")
		return '1'
	if st == 'rm dp cl':
		props = clean_waiting_propositions_values()
		props = set(props)
		clean_props = open("clean_waiting_propositions.txt",mode='w',encoding="utf-8")
		clean_props.close()
		for i in props:
			clean_waiting_propositions_write(i)
		print("Duplicates removed from the clean_waiting_proposition.txt file")
		return '1'
	if st == 'rm dp pr':
		props = propositions_values()
		props = set(props)
		a_props = open("propositions.txt",mode='w',encoding="utf-8")
		a_props.close()
		for i in props:
			propositions_write(i)
		print("Duplicates removed from the proposition.txt file")
		return '1'
	
def press_2():
	print("Introduce 'ls' if yout want to see all cleaned propositions and their index")
	print("Introduce 'exit' if yout want to go back to the menu")
	print("The commands you can use after you introduce index of string are -l and -g")
	print("-l for listing of steps")
	print("-g for showing graphical construcion of abstract structure")
	st = input("Plese introduce the index of the proposition you want to check: ")
	clear()
	if st == 'exit':
		return '-1';
	if st == 'ls':
		clean_props = clean_waiting_propositions_values()
		clear()
		for i in range(len(clean_props)):
			print("[" + str(i) + "]: " + clean_props[i],end='')
		return press_2()
	st = st.split(" ")
	nr = int(st[0])
	d = 0
	if len(st) == 3 and ((st[1] == '-g' and st[2] == '-l') or (st[1] == '-l' and st[2] == '-g')):	
		d = 3
	elif len(st) == 2:
		if st[1] == '-g':
			d = 2
		elif st[1] == '-l':
			d = 1
	clean_props = clean_waiting_propositions_values()
	rez = check_propositional_format(clean_props[nr][:len(clean_props[nr])-1],d)
	if type(rez) is tuple:
		if d == 1 or d == 3:
			print(rez[0])
		else:
			print("The string is not a well formed formula")
		dlt = input('Do you want to delete the string from the "clean_waiting_propositions.txt" file ?[Y/N]')
		clear()
		if dlt == 'y' or dlt == 'Y':
			clean_waiting_propositions_remove(nr)
			print("String was deleted succesfully")
	else:
		print("String " + clean_props[nr][:len(clean_props[nr])-1] + " is a well formed formula.")
		print("This is the abstruct structure of the formula: " + str(rez))
		propositions_write(str(rez) + '\n')
		print('Abstract structure of proposition was written to "propositions.txt"')
		if(d == 3 or d == 2):
			fi = open("send_cpp.txt", mode='w')
			fi.write(str(rez))
			fi.close()
			os.popen('./run_here.sh')
	return '2'
	
def press_3():
	print("Introduce 'ls' if yout want to see all cleaned propositions and their index")
	print("Introduce 'exit' if yout want to go back to the menu")
	print("The command you can use after you introduce index of string is -l ")
	print("-l for listing of steps")
	st = input("Plese introduce the index of the proposition you want to check: ")
	if st == 'exit':
		return '-1';
	clear()
	clean_props = clean_waiting_propositions_values()
	if st == 'ls':
		for i in range(len(clean_props)):
			print("[" + str(i) + "]: " + clean_props[i],end='')
		return press_3()
	st = st.split(" ")
	nr = int(st[0])
	d = 0
	if len(st) > 1 and st[1] == '-l':
		d = 1
	wff = place_paranthases(clean_props[nr][:len(clean_props[nr])-1],d)
	if not wff:
		print("The string could not be parsed, please review your input...")
		inn = input("Do you want to delete this string from the cleaned propositions file ?[Y/N]")
		if inn == 'y' or st == 'Y':
			clean_waiting_propositions_remove(nr)
			print('String was deleted from "clean_waiting_propositions.txt".')
	else:
		print("This is the parsed ,now well formed formula: " + str(wff))
		abstruct_structure = check_propositional_format(wff,0)
		print("This is the abstruct structure: " + str(abstruct_structure))
		inn = input("Do you want to write the well formed formula to clean_waiting_propositions.txt ?[Y/N]")
		if inn == 'y' or st == 'Y':
			clean_waiting_propositions_write(wff + '\n')
			print('Proposition was written to "clean_waiting_propositions.txt".')
		inn = input("Do you want to write the abstruct structure to propositions.txt ?[Y/N]")
		if inn == 'y' or st == 'Y':
			propositions_write(str(abstruct_structure) + '\n')
			print('Abstruct structures was written to "propositions.txt".')
	return '3'
		
def press_4():
	print("Introduce 'ls' if yout want to see all cleaned propositions and their index")
	print("Introduce 'exit' if yout want to go back to the menu")
	st = input("Plese introduce the index of the proposition you want to create the truth table for: ")
	if st == 'exit':
		return '-1';
	clear()
	props = propositions_values()
	if st == 'ls':
		for i in range(len(props)):
			print("[" + str(i) + "]: " + props[i],end='')
		return press_4()
	nr = int(st)
	tr = ast.literal_eval(props[nr][:len(props[nr])-1])
	make_table(tr)
	os.system("python3 table_format.py")
	os.system("less -S table.txt")
	return '4'
	
	
	
	
		
