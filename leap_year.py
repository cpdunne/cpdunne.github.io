def isLeapYear(year):
	if year % 100 != 0:
		if year % 4 == 0:
			tof = True
		else:
			tof = False
	else:
		if year % 400 == 0:
			tof = True
		else:
			tof = False
	return tof
	# Add your code to calculate if year is a leap year
	# Return True if it is a leap year; return False if it is not a leap year


def main():
	valid = True
	while valid:
		year = int(input("Enter year: "))
		if year > 0:
			valid = False
		else:
			print("Please enter a valid year.")
	leap = isLeapYear(year)
	if leap == True:
		print(f'{year} is a leap year.')
	else:
		print(f'{year} is not a leap year.')


	# Add code to ask the user for a year (any positive integer)
	# Validate that the year is > 0 and if not tell the user and ask again
	# Use your isLeapYear function to test if the year is a leap year
	# If it is, tell the user it is.  If not, tell the user it is not.

main()
