# You may need to import something here
import random

def print_story(person, place1, place2, plun1, plun2, actv1, actv2, food, adjective1, adjective2, n):
	print(f'''Last year, we went for a holiday with {person} on a trip to
{place1}. The food there is very {adjective1}! Western
{place1} has many {plun1}, and they make {plun2} there.

Many people there also go to the {place2} to {actv1}. The people who live there like to drink {food}. They also
like to {actv2} in the snow and swim in the {n}.

It was a really {adjective2} vacation!''')
	# Add code to print a story from the words given to this function as parameters.
	# This is a void function: it doesn't return anything.

def rn():
	return(random.randint(0, 9))


def main():
	loop = True

	persons = ['your mom', 'Dwayne "The Rock" Johnson', 'Putin', 'Lizzo', 'Frank Ocean', 'my dog', 'my neighbor', 'Rick', 'Jerry Seinfeld', 'Zendaya']
	places = ['San Francisco', 'gym', 'cafeteria', 'Hayes Healy', 'Lone Mountain', 'movie theater', 'Starbucks', 'Gilson', 'closet', 'Golden Gate Bridge']
	plural_n = ['babies', 'appendices', 'dice', 'clones of Dwayne "The Rock" Johnson', 'spoons', 'crabs', 'eyes', 'bugs', 'toes', 'shoes']
	action_v = ['fight', 'eat', 'kiss', 'walk', 'persuade', 'cry', 'dive', 'throw', 'grab', 'smile']
	foods = ['orange juice', 'water', 'Whey protein shakes', 'uncooked eggs in a can', 'Coke', 'syrup', 'vitamin water', 'pina colada', 'carbonated water', 'Sprite']
	adjectives = ['obnoxious', 'disgusted', 'cute', 'combative', 'aggressive', 'confident', 'comfortable', 'purple', 'green', 'cyan']
	noun = ['baby', 'appendice', 'man', 'clone of Dwayne "The Rock" Johnson', 'spoon', 'crab', 'eye', 'bug', 'toe', 'shoe']
	
	while loop:
		print_story(persons[rn()], places[rn()], places[rn()], plural_n[rn()], plural_n[rn()], action_v[rn()], action_v[rn()], foods[rn()], adjectives[rn()], adjectives[rn()], noun[rn()])
		valid = True
		while valid:
			again = input("Do you want to see another version of the story? ")
			if again.lower() == 'yes' or again.lower() == "y":
				valid = False
			elif again.lower() == "no" or again.lower() == "n":
				loop = False
				valid = False
				quit()
			else:
				print("Please answer 'y' or 'yes' or 'n' or 'no'")	
	# Add code to define lists of words,
	#    choose random words from each list,
	#    display the story using the random words,
	#    then ask user if they want to see another story 

main()