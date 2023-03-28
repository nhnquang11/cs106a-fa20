def exclaim(s): 
	"""
	Given a string s, look for the first exclamation mark. 
	If there is a substring of 1 or more alphabetic characters 
	immediately to the left of the exclamation mark, 
	return this substring including the exclamation mark. 
	Otherwise, return the empty string.
	>>> exclaim('xx Hello! yy')
	'Hello!'
	>>> exclaim('!Hello')
	''
	"""
	mark = s.find('!') 
	if mark == -1:
		return False

	result = '!'
	for i in reversed(range(mark)):
		if not s[i].isalpha():
			break
		result = s[i] + result

	if len(result) > 1:
		return result
	return ''

def vowels(s):
	"""
	Given a string s, look for the first colon. 
	If there is a substring of 1 or more vowels immediately to the right of the colon, 
	return this substring without the colon. Otherwise, return the empty string.
	>>> vowels('xy:aieee?')
	'aieee'
	"""
	mark = s.find(':')
	if mark == -1:
		return ''

	result = ''
	for i in range(mark + 1, len(s)):
		if s[i].lower() in 'aeiouy':
			result += s[i]
	return result
