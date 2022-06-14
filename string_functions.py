def cs110_upper(string):	#takes string & makes it uppercase
	big_cap = ""
	da_value= ""
	for i in range(len(string)):
		da_value = ord(string[i])
		if da_value >= 97 and da_value <= 122:
			big_cap = big_cap + (chr(int(da_value) - 32))
		else:
			big_cap = big_cap + str(chr(int(da_value)))
	return big_cap

def cs110_lstrip(string):
	no_space = ""
	da_value= ""
	count = 0
	for i in range(len(string)):
		da_value = ord(string[i])
		if da_value != 32:
			break
		else:
			count += 1
	for c in range(0 + count, len(string)):
		da_value = ord(string[c])
		no_space = no_space + str(chr(da_value))
	return no_space

def cs110_replace (string,char1,char2):
	big_cap = ""
	da_value= ""
	value_1 = ord(char1)
	value_2 = ord(char2)
	for i in range(len(string)):
		da_value = ord(string[i])
		if da_value == value_1:
			big_cap = big_cap + chr(value_2)
		else:
			big_cap = big_cap + chr(da_value)
	return big_cap

def cs110_in(shortString, longString):
	no_space = ""
	da_lvalue= ""
	bungus = 0
	da_svalue = ord(shortString[bungus])
	count = 0
	torf = False
	for i in range(len(longString)):
		da_lvalue = ord(longString[i])
		if da_lvalue == da_svalue:
			break
		else:
			count += 1
	for c in range(0 + count, len(longString)):
		da_lvalue = ord(longString[c])
		da_svalue = ord(shortString[bungus])
		if da_lvalue != da_svalue:
			bungus = 0
			for z in range(len(longString)):
				da_lvalue = ord(longString[z])
				if da_lvalue == da_svalue:
					break
				else:
					count += 1
		elif bungus + 1 == len(shortString):
			torf = True
			break
		elif bungus + 1 > len(shortString):
			break
		else:
			bungus += 1
			count += 1
	return torf

def cs110_title (string):
	big_cap = ""
	da_value= ""
	first_chr = ord(string[0])
	space = False
	if first_chr >= 97 and first_chr <= 122:
		big_cap = big_cap + (chr(int(first_chr) - 32))
	else:
		big_cap = big_cap + str(chr(int(first_chr)))
	for i in range(1, len(string)):
		da_value = ord(string[i])
		if da_value == 32:
			space = True
			big_cap = big_cap + str(chr(int(da_value)))
		elif space:
			space = False
			if da_value >= 97 and da_value <= 122:
				big_cap = big_cap + (chr(int(da_value) - 32))
			else:
				big_cap = big_cap + str(chr(int(da_value)))
		else:
			big_cap = big_cap + str(chr(int(da_value)))
	return big_cap

# EXTRA CREDIT.  Implement this function only if functions 1-10 work properly
# No credit if functions 1-10 do not work properly
def cs110_remove_repeats(string):
	big_cap = ""
	da_value= ""
	prev_chr = ""
	for i in range(len(string)):
		da_value = ord(string[i])
		if da_value != prev_chr:
			big_cap = big_cap + str(chr(int(da_value)))
		prev_chr = da_value
	return big_cap

# Do not add a main() function or any non-function code.
# Add only the code for the above functions.