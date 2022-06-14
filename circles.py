import math  # Need so global variable math.pi is defined

def circumference(r):
	return 2 * math.pi * r
	# Write code to take the radius r and
	# compute and return the circumference

def area(r):
	return r ** 2 * math.pi
	# Write code to take the radius r and
	# compute and return the area
	
def main():
	bingus = True
	while bingus:
		r = float(input("Enter radius of a circle: "))
		if r == 0:
			print("Goodbye!")
			bingus = False
			quit()
		elif r < 0:
			print("Invalid radius!")
		elif r > 0:
			print(f'A circle of radius {r} has circumference {circumference(r)} and area {area(r)}.')


	# Write code to ask user for radius,
	# then use the above two functions to
	# compute the area and circumference.
	# Perform input validation: don't accept negative radius.
	# Zero (0) is the sentinel value that ends the program;
	# otherwise keep asking user for new radius.

main()