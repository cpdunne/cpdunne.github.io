from movie import Movie

# Create instance
m = Movie(title="Battlefield Earth",
         release_year=2000,
         director='Roger Christian')

m.add_rating(2)
m.add_rating(4)
m.add_rating(5)
m.add_rating(4)

m.calc_average_rating()

# Check attributes are defined
expected_attributes = {'_Movie__director', '_Movie__ratings', '_Movie__release_year', '_Movie__title', '_Movie__average_rating', 'add_rating', 'calc_average_rating', 'getRatings'}
#print(m.__dir__())
actual_attributes = set(attribute for attribute in m.__dir__() if not attribute.startswith('__'))
assert actual_attributes >= expected_attributes 

# Check that __str__ has been implemented
assert not m.__str__().startswith('<__main__.')

# Check that ratings can be added and calculated 
assert m.getRatings() == [2, 4, 5, 4]
assert m.getAverageRating() == 3.75

print("All tests pass 🙂")
