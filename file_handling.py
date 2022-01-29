def clean_waiting_propositions_write(st):
	try:
		clean_waiting_propositions = open("clean_waiting_propositions.txt",mode = 'a' ,encoding="utf-8")
	except IOError:
		print('"clean_waiting_propositions.txt" file not found...')
		return False
	finally:
		clean_waiting_propositions.write(st)
		clean_waiting_propositions.close()
		return True
		
def clean_waiting_propositions_values():
	try:
		clean_waiting_propositions = open("clean_waiting_propositions.txt",mode='r')
	except IOError:
		print('"clean_waiting_propositions.txt" file not found...')
		return False
	finally:
		clean_props = clean_waiting_propositions.readlines()
		clean_waiting_propositions.close()
		return clean_props
		
def clean_waiting_propositions_remove(i):
	try:
		clean_waiting_propositions = open("clean_waiting_propositions.txt", mode='r')
	except IOError:
		print('"clean_waiting_propositions.txt" file not found...')
		return False
	finally:
		clean_props = clean_waiting_propositions.readlines()
		clean_waiting_propositions.close()
		clean_waiting_propositions = open("clean_waiting_propositions.txt", mode='w')
		clean_waiting_propositions.close()
		clean_waiting_propositions = open("clean_waiting_propositions.txt", mode='a')
		del clean_props[i]
		for x in clean_props:
			clean_waiting_propositions.write(x)
		clean_waiting_propositions.close()
		return True
		
def propositions_write(st):
	try:
		propositions = open("propositions.txt",mode='a',encoding="utf-8")
	except IOError:
		print('"propositions.txt" file not found...')
		return False
	finally:
		st = st.replace(' ','')
		propositions.write(st)
		propositions.close()
		return True
		
def propositions_values():
	try:
		propositions = open("propositions.txt",mode='r')
	except IOError:
		print('"propositions.txt" file not found...')
		return False
	finally:
		props = propositions.readlines()
		propositions.close()
		return props
		
def propositions_remove(i):
	try:
		propositions = open("propositions.txt", mode='r')
	except IOError:
		print('"propositions.txt" file not found...')
		return False
	finally:
		props = propositions.readlines()
		propositions.close()
		propositions = open("propositions.txt", mode='w')
		propositions.close()
		propositions = open("propositions.txt", mode='a')
		del props[i]
		for x in props:
			propositions.write(x)
		propositions.close()
		return True
		
def dummy_file_write(st,fl):
	try:
		dummy_file = open(fl,mode='a',encoding="utf-8")
	except IOError:
		print('"dummy_file.txt" file not found...')
		return False
	finally:
		dummy_file.write(st)
		dummy_file.close()
		return True
		
def dummy_file_values(fl):
	try:
		dummy_file = open(fl,mode='r')
	except IOError:
		print("dummy_file.txt file not found")
	finally:
		files = dummy_file.readlines()
		dummy_file.close()
		return files
