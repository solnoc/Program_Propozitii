from give_truth import *
def give_interpretation(st):
	if len(st) <= 1:
		return '('+get_table_form(st[0])+')';
	rez = 'Ɓ'
	if st[0] == '¬':
		rez += st[0]
		rez += '(Vi'
		return rez + give_interpretation(st[1]) + ')'
	else:
		rez += st[0]
		rez += '(Vi'
		i1 = give_interpretation(st[1])
		i2 = give_interpretation(st[2])
		return str(rez) + i1 + ',Vi' + i2 + ')'
		
v = propositions_values()
s = v[0][0:len(v[0])-1]
s = ast.literal_eval(s)

ww=0
	
def pprint():
	ww = str(row)
	ww = ww.replace('[','(')
	ww = ww.replace(']',')')
	ww = ww.replace(' ','')
	ww = ww.replace("'", "")
	ww = ww.replace(",","")
	ww = ww.replace(")(","),(")
	ww = ww.replace(")Vi","),Vi")
	ww += '='
	print(ww)
	pp = 0
	for i in range(len(ww)):
		if ww[i] == '(':
			pp += 1
		elif ww[i]==')':
			pp -= 1

def give_int(st,rro):
	if st[0] == '¬':
		rro[0] = 'Ɓ¬'
		if st[1][0] in letters:
			rro[1] = ['Vi(' + st[1][0] + ')']
			pprint()
		else:
			rro[1] = ['Vi' + get_table_form(st[1])]
			pprint()
			rro[1] = ['',[]]
			give_int(st[1],rro[1])
	else:
		rro[0] = 'Ɓ' + st[0]
		if st[1][0] in letters:
			rro[1] = ['Vi(' + st[1][0] + ')']
			if st[2][0] in letters:
				rro[1].append('Vi(' + st[2][0] + ')')
				pprint()
			else:
				rro[1].append('Vi' + get_table_form(st[2]))
				pprint()
				rro[1] = [rro[1][0],['',[]]]
				give_int(st[2],rro[1][1])
		else:
			rro[1] = ['Vi' + get_table_form(st[1])]
			if st[2][0] in letters:
				rro[1].append('Vi(' + st[2][0] + ')')
				pprint()
				rro[1] = [['',[]],rro[1][1]]
				give_int(st[1],rro[1][0])
			else:
				rro[1].append('Vi' + get_table_form(st[2]))
				pprint()
				rro[1] = [['',[]],rro[1][1]]
				give_int(st[1],rro[1][0])
				rro[1] = [rro[1][0],['',[]]]
				give_int(st[2],rro[1][1])
				
		
	
	
w = s
for ite in v:
	s = ite[0:len(ite)-1]
	s = ast.literal_eval(s)
	w=s
	row = ['',[]]
	print(w)
	give_int(w,row)
	print('\n\n\n')
give_int(s,0)
print(s)

def get_form(st):
	if st[0] in letters:
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
	

def give_iasdasdasdasnt(st,pp,ro):
	if st[0][0] in letters:
		st[0] = "Vi(" + st[0][0] + ')'
	elif st[0] == '¬':
		st[0] = 'Ɓ¬'
		c1 = st[1]
		if c1[0] in letters:
			st[1] = "Vi(" + c1[0] + ')'
			pp=0
			pprint()
		else:
			st[1] = "Vi" + get_table_form(st[1])
			pprint()
			st[1] = c1
			give_int(st[1],pp)
		
	else:
		st[0] = 'Ɓ' + st[0]
		c1 = st[1]
		c2 = st[2]
		if c1[0] in letters:
			st[1] = "Vi(" + c1[0] + ')'
			if c2[0] in letters:
				st[2] = "Vi(" + c2[0] + ')'
				pp=0
				pprint()
			else:
				st[2] = "Vi" + get_table_form(c2)
				pprint()
				st[2] = c2
				give_int(st[2],pp+1)
		else:
			st[1] = "Vi" + get_table_form(c1)
			if c2[0] in letters:
				st[2] = "Vi(" + c2[0] + ')'
				pp=0
				pprint()
				st[1] = c1
				give_int(st[1],pp)
			else:
				st[2] = "Vi" + get_table_form(c2)
				pprint()
				st[1] = c1
				give_int(st[1],pp)
				st[2] = c2
				give_int(st[2],pp+1)
