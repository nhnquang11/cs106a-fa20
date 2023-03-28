from random import uniform

NUM_POINTS = 100000
REPEAT_TIMES = 100

def main():
	total_estimated_pi = 0
	for i in range(REPEAT_TIMES):
		estimated_pi = get_estimated_pi()
		print(f"Estimated pi #{i+1} = {estimated_pi}")
		total_estimated_pi += estimated_pi
	average_estimated_pi = total_estimated_pi / REPEAT_TIMES
	print(f"The average of those estimations is: {average_estimated_pi}")
	
def get_estimated_pi():
	num_points_in_circle = 0
	for i in range(NUM_POINTS):
		x = uniform(-1, 1)
		y = uniform(-1, 1)
		if is_in_circle(x, y):
			num_points_in_circle += 1
	estimated_pi = num_points_in_circle / NUM_POINTS * 4
	return estimated_pi

def is_in_circle(x, y):
	return x**2 + y**2 <= 1

if __name__ == "__main__":
	main()
	