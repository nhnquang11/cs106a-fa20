import random

SKILL_SCORE_MINIMUM = 0.90
SKILL_WEIGHT = 0.95
LUCK_WEIGHT = 0.05

def make_applicants(num_applicants):
	"""
	Given the number of applicants, randomly generate 
	skill score and luck score for each applicant. 
	Return the data of all applicants into a list.
	"""
	applicants = []
	for _ in range(num_applicants):
		skill = random.random()
		luck = random.random()
		applicants.append({'skill':skill, 'luck':luck})
	return applicants

def make_first_cut_applicants(applicants):
	"""
	Given the list of initial applicants, eliminate everyone 
	not meeting the requirements (skill score < threshold).
	Returns the list of only skillful ones.
	"""
	return [{'skill':app['skill'], 'luck':app['luck']} 
			for app in applicants if app['skill'] > SKILL_SCORE_MINIMUM]

def calc_combined_score(applicant):
	"""
	Return the combined score of skill and luck scores of the given applicant.
	"""
	return applicant['skill'] * SKILL_WEIGHT + applicant['luck'] * LUCK_WEIGHT

def get_top_astronauts(applicants, num_to_select):
	"""
	Given a list of applicants and the number to select n, 
	return the top n astronauts having the highest combined scores.
	"""
	return sorted(applicants, key=calc_combined_score, reverse=True)[:num_to_select]

def calc_average_score(applicants):
	"""
	Given the list of applicants, return a dictionary including 
	the average skill score and the average luck score.
	"""
	skill_avg = sum([app['skill'] for app in applicants]) / len(applicants)
	luck_avg = sum([app['luck'] for app in applicants]) / len(applicants)
	return {'skill':skill_avg, 'luck':luck_avg}

def find_percent_increase(low, high):
	return round((high - low) / low * 100, 2)

def main():
	num_applicants = int(input("How many applicants are there? "))
	applicants = make_applicants(num_applicants)

	skillful = make_first_cut_applicants(applicants)
	print(f"Out of {num_applicants} applicants, there are {len(skillful)} applicants skillful enough " +
			"to make the first cut.")

	num_to_select = int(input("How many skillful applicants finally being astronauts? "))
	selected = get_top_astronauts(skillful, num_to_select)
	
	skillful_avg = calc_average_score(skillful)
	selected_avg = calc_average_score(selected)

	skill_pct_increase = find_percent_increase(skillful_avg['skill'], selected_avg['skill'])
	luck_pct_increase = find_percent_increase(skillful_avg['luck'], selected_avg['luck'])

	print("------------------------------")
	print("------------------------------")
	print("RESULT")
	print("The selected group is (on average): ")
	print(f"{skill_pct_increase}% more skillful than the {len(skillful)} people that passed the first cut.")
	print(f"{luck_pct_increase}% more skillful than the {len(skillful)} people that passed the first cut.")

if __name__ == '__main__':
	main()










