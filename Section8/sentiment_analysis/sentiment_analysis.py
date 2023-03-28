EMOTION = 'anger'

def make_emotion_dict(filename):
	emotion_dict = {}
	for line in open(filename):
		splits = line.split()
		
		if splits[1] == EMOTION:
			curr_word = splits[0]
			value = int(splits[2])
			
			emotion_dict[curr_word] = value
	
	return emotion_dict

def read_file(filename, emotion_dict, stoplist):
	top_tweet = ""
	top_score = -1
	for line in open(filename):
		splits = line.split()
		shortened_tweet = remove_stop_words(splits, stoplist)
		score = sum_tweet(shortened_tweet, emotion_dict)
		if score >= top_score:
			top_score = score
			top_tweet = line.strip()


	return top_tweet, top_score

def remove_stop_words(line, stoplist):
	updated_tweet = []
	for word in line: 
		if word.lower() not in stoplist:
			updated_tweet.append(word)
	return updated_tweet


def sum_tweet(tweet, emotion_dict):
	"""
	>>> emotion_dict = {'happy':1, 'birthday':1}
    >>> sum_tweet(['Happy', 'Birthday', 'Brahm!'], emotion_dict)
    2
    """
	score = 0
	for word in tweet:
		if word.lower() in emotion_dict:
			score += emotion_dict[word.lower()]
	return score

def build_stop_list():
	stoplist = []
	fp = open("english.stop")
	stoplist = fp.read()
	fp.close()
	return stoplist

def main():
	#creates a list of all words that you want to remove from each tweet 
	stoplist = build_stop_list()

	emotion_dict = make_emotion_dict('emotion-lexicon.txt')

	top_tweet, top_score = read_file('brahms_puns.txt', emotion_dict, stoplist)
	print(top_score, top_tweet)

if __name__ == "__main__":
	main()