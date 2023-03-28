def only_one_first_char(s):
	"""
	Removes all occurences of the first character of s except the first character itself.
	>>> only_one_first_char('recurrence')
	'recuence'
	"""
	res = s[0]
	for char in s:
		if char != s[0]:
			res += char
	return res

def make_gerund(s):
	"""
	Adds 'ing' to the end of the given word.
	If the given word already ends in 'ing', adds 'ly' to the end of the given word.
	>>> make_gerund('interesting')
	'interestingly'
	>>> make_gerund('start')
	'starting'
	"""
	if len(s) >= 3 and s[-3:] == "ing":
		return s + 'ly'
	return s + 'ing'

def put_in_middle(outer, inner):
	"""
	Returns a new string where inner has been put into the middle of outer.
	>>> put_in_middle('starting', 'bob')
	'starbobting'
	>>> put_in_middle('total', 'part')
	'toparttal'
	"""
	mid_index = len(outer) // 2
	return outer[:mid_index] + inner + outer[mid_index:]
