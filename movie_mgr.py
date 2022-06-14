from movie import Movie

def read_movie_data(file):
	yaga = []

	for line in file:
		line = list(line.split(','))
		booh = line[0]
		yumpo = Movie(line[0], int(line[1]), ",".join(line[2:]))
		yaga.append(yumpo)
		
	return yaga

	# Add code to take already-opened file as parameter,
	#    read movie data from file (1 movie/line),
	#	 create a movie-object for each line of the file,
	#    store the movie-objects in a list,
	#    and return the list

def main():
	print('Welcome to Movie Manager')
	movie_file = open('movie_data.txt', 'r')
	chungus = read_movie_data(movie_file)
	movie_file.close()
	tf = True
	while tf:
		tf2 = True
		foundmovie = False
		search = input('Please enter a movie title: ')
		for z in chungus:
			if search.upper() in z.getdatitle().upper():
				print(z)
				foundmovie = True
			
		if foundmovie == False:
			if search.upper() == "ADD NEW":
				print('Enter data for new movie.')
				newTitle = input('Title: ')
				newYear = input('Year: ')
				newDirector = input('Director: ')
				schwooga = Movie(newTitle, int(newYear), newDirector)
				chungus.append(schwooga)
			else:
				print('Movie not found.\n')

		while tf2:
			again = input('Search for another movie? ("Y", "y", "N", "n") ')
			if again.upper() == 'Y':
				tf2 = False
			elif again.upper() == 'N':
				tf2 = False
				tf = False
			else:
				print('Error! Please enter a valid input')
	print('Goodbye!')

	# Add code to:
	# 1. open provided movie_data file,
	# 2. call read_movie_data() with opened file,
	# 3. close file.
	# 4. Ask user for movie title,
	# 5. Search list of movies for title,
	# 6. If title found, print that movie object,
	#    If title not found, print "Movie not found."
	# 7. Ask user if wants to search for another movie,
	#    Validate response ("Y", "y", "N", "n"); re-ask if necessary,
	# 8. If user responds "Y" or "y", return to step 4 (not step 1)
	#    If user responds "N" or "n", print "Goodbye!" and quit.

main()