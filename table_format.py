from file_handling import *
table = dummy_file_values("table.txt")
tabel = open("table.txt", mode='w')
tabel.close()
w = 1
for i in range(1,len(table)):
	table[i] = table[i].replace(" ","")
	table[i] = list(table[i])
	
dummy_file_write(table[0],"table.txt")
word = 0
for i in range(2,len(table[0])):
	if table[0][i] != ' ':
		for j in range(1,len(table)):
			table[j].insert(w,"?")
		word += 1
	else:
		if word > 2:
			for q in range(word//2):
				for j in range(1,len(table)):
					#if w-(word//2) < len(table[])
					table[j].pop(w-(word//2))
					table[j].insert(w,"?")
		word = 0 
	w += 1
		
		
# P B (¬B) (¬(¬B)) (¬(¬(¬B))) (¬(¬(¬(¬B)))) (¬(¬(¬(¬(¬B))))) (P⇒(¬(¬(¬(¬(¬B)))))) Q S (Q∧S) ((P⇒(¬(¬(¬(¬(¬B))))))⇔(Q∧S)) 
# F F    T       F T F T F F F F T 

	
for i in range(1,len(table)):
	table[i] = str(table[i])
	table[i] = table[i].replace("[","")
	table[i] = table[i].replace("]","")
	table[i] = table[i].replace(",","")
	table[i] = table[i].replace("'","")
	table[i] = table[i].replace(" ","")
	table[i] = table[i].replace("?"," ")
       #table[i] = table[i].replace("\\","")
	table[i] = table[i].replace("\\n","")
	dummy_file_write(str(table[i]) + '\n',"table.txt")


