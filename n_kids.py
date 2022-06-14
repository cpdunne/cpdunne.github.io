def main():
	kidsfile = open("n_kids.txt", "r")
	families = 0
	total = 0
	minimum = 50
	maximum = 0

	for line in kidsfile:
		line = line.rstrip("\n")
		families += 1
		total += int(line)
		if int(line) > maximum:
			maximum = int(line)
		if int(line) < minimum:
			minimum = int(line)
	kidsfile.close()
	
	avg = total / families
	print(f'''Number of families: {families}
Total number of kids: {total}
Average number of kids per family: {"{:.2f}".format(avg)}
Maximum number of kids in a family: {maximum}
Minimum number of kids in a family: {minimum}''')
	writefile = open("results.txt", "w")
	writefile.write(f'''Number of families: {families}
Total number of kids: {total}
Average number of kids per family: {"{:.2f}".format(avg)}
Maximum number of kids in a family: {maximum}
Minimum number of kids in a family: {minimum}''')
	writefile.close()
	# Add code that reads the file n_kids.txt,
	#    computes the total number of kids,
	#    the average #, the minimum #, and the maximum #
	#	 and displays those numbers as specified in the instructions.

main()