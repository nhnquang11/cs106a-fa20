def percent_in_common(l1, l2):
	"""
	Returns the percentage of the items in common in both lists.
	Assumes that there are no repeated elements in any of the lists.
	"""
	return len([x for x in l1 if x in l2]) / (len(l1) + len(l2))

def calc_score(netflix_history1, netflix_history2, fav_books1, fav_books2):
	"""
	Given the lists of favorite books and netflix history of two users, 
	calculate the compatibility score based on the books and movies
	in common between two users.
	"""
	return percent_in_common(netflix_history1, netflix_history2) +\
			percent_in_common(fav_books1, fav_books2)

def new_friend(name_list, compatibility_scores):
	"""
	Given a list of names of all other users and a list of compatibility scores
	between the chosen user and all other users, returns a list where the first element
	is the name of the user who is the most compatible and the second is element is
	their compatibility score.
	"""
	max_index = get_max_index(compatibility_scores)
	return [name_list[max_index], compatibility_scores[max_index]]

def get_max_index(lst):
	"""
	Returns the index of the max element in the lst.
	"""
	best_index = 0
	best_value = lst[0]

	for index, value in enumerate(lst):
		if value > best_value:
			best_index = index
			best_value = value

	return best_index
	