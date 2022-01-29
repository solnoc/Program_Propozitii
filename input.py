from file_handling import *
from check_propositional_format import *
def input_f(st):
	il_chr = False
	jumps = 0
	for i in range(len(st)):
		if jumps > 0:
			jumps -= 1
			continue
		if not st[i] in allowed:
			if i+2 < len(st) and st[i:i+3] in allowed:
				jumps = 2
			else:
				print("Element " + st[i] + " is not valid, please try to review your input...")
				il_chr = True
	if not il_chr:
		st = format(st)
		clean_waiting_propositions_write(st)
		print('String was formated as ' + st, end='')
		print('String was written to "clean_waiting_propositions.txt" sucessfuly.')

def format(st):
	st = st.replace(" ","")
	st = st.replace("neg","¬")
	st = st.replace("dis","∨")
	st = st.replace("con","∧")
	st = st.replace("imp","⇒")
	st = st.replace("equ","⇔")
	st = st + "\n"
	return st
