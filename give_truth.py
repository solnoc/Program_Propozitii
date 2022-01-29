from file_handling import *
import ast
def make_table(st):
	table = open("table.txt", mode='w',encoding='utf-8')
	table.close()
	get_table_form(st)
	dummy_file_write('\n',"table.txt")
	set_and_give(st)
	
def set_and_give(st):
	props = get_props(st)
	vals = []
	start = st
	x = 1
	w = 1
	maxx = len(props)
	for i in range(maxx):
		x = x*2
	for i in range(x):
		vals = []
		st = start
		bi = bin(i)
		bi = bi[2:]
		bi = int(bi)
		while bi != 0:
			if bi % 10 == 1:
				vals.append('True')
			else:
				vals.append('False')
			bi = bi // 10
		for i in range(len(vals),maxx):
			vals.append('False')
		st = set_props(st,2,vals)
		print(vals)
		give_truth(st)
		dummy_file_write('\n',"table.txt")
		
letters = [chr(x) for x in range(ord('A'),ord('Z')+1)]
def get_table_form(st):
	if st[0] in letters:
		dummy_file_write(st[0] + ' ',"table.txt")
		return st[0]
	if st[0] == '¬':
		rez = '(¬' + get_table_form(st[1]) + ')'
		dummy_file_write(rez + ' ',"table.txt")
		return rez
	elif st[0] == '∨':
		rez = '(' + get_table_form(st[1]) + "∨" + get_table_form(st[2]) + ')'
		dummy_file_write(rez + ' ',"table.txt")
		return rez
	elif st[0] == '∧':
		rez = '(' + get_table_form(st[1]) + "∧" + get_table_form(st[2]) + ')'
		dummy_file_write(rez + ' ',"table.txt")
		return rez
	elif st[0] == '⇒':
		rez = '(' + get_table_form(st[1]) + "⇒" + get_table_form(st[2]) + ')'
		dummy_file_write(rez + ' ',"table.txt")
		return rez
	elif st[0] == '⇔':
		rez = '(' + get_table_form(st[1]) + "⇔" + get_table_form(st[2]) + ')'
		dummy_file_write(rez +' ',"table.txt")
		return rez
	return "Error"

def give_truth(st):
	if st[0] == 'False' or st[0] == False:
		dummy_file_write('F' + ' ',"table.txt")
		return False
	elif st[0] == 'True' or st[0] == True:
		dummy_file_write('T' + ' ',"table.txt")
		return True	

	if st[0] == '¬':
		tr =  not give_truth(st[1])
		dummy_file_write(('T' if tr else 'F') + ' ',"table.txt")
		return tr
	elif st[0] == '∨':
		tr1 = give_truth(st[1])
		tr2 = give_truth(st[2])
		tr = tr1 or tr2
		dummy_file_write(('T' if tr else 'F') + ' ',"table.txt")
		return tr
	elif st[0] == '∧':
		tr1 = give_truth(st[1])
		tr2 = give_truth(st[2])
		tr = tr1 and tr2
		dummy_file_write(('T' if tr else 'F') + ' ',"table.txt")
		return tr
	elif st[0] == '⇒':
		p1 = give_truth(st[1])
		p2 = give_truth(st[2])
		if p1 and (not p2):
			tr = False
		else:
			tr = True
		dummy_file_write(('T' if tr else 'F') + ' ',"table.txt")
		return tr
	elif st[0] == '⇔':
		p1 = give_truth(st[1])
		p2 = give_truth(st[2])
		if (p1 and p2) or ((not p1) and (not p2)):
			tr = True
		else:
			tr = False
		dummy_file_write(('T' if tr else 'F') + ' ',"table.txt")
		return tr

def get_props(st):
	props = set()
	st = str(st)
	for x in st:
		if x in letters:
			props.add(x)
	return props
	
def set_props(st,d,val=[]):
	props  = set()
	props = get_props(st)
	st = str(st)
	w=0
	for x in props:
		if d == 1:
			print("Introduce value for: " + str(x))
		if d == 0 or d == 1:
			inn = input()
			if inn == 'f' or inn == 'F':
				st = st.replace(x,'False')
			elif inn == 't' or inn == 'T':
				st = st.replace(x,'True')
			else:
				print("Input not correct, value set to True")
		if d == 2:
			st = st.replace(x,val[w])
			w += 1
	st = ast.literal_eval(st)
	return st
		

