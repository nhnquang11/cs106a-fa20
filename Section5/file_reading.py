def find_smallest_int(filename):
	"""
	Returns the smallest unique positive integer in the given file.
	"""
	occurrence = dict()
	with open(filename) as file:
		for line in file:
			num = int(line)
			if num <= 0:
				continue
			if not occurrence.get(num):
				occurrence[num] = 0
			occurrence[num] += 1
			
	for key in sorted(occurrence.keys()):
		if occurrence[key] == 1:
			return key

def main():
	filename = "filename.txt"
	print(find_smallest_int(filename))

if __name__ == '__main__':
	main()