# Solution to A4

try:
	# Continuously check for input
	while True:
		n = raw_input("Enter Input :\t")
	
		# break if input == -1
		if (int(n) == -1):
			break

		# for each digit i in sequence, calculate the multiplication of all digits except that
		for i in range (0,len(n)):
			count = 1
			for j in range (0,len(n)):
				if (j == i):
					continue

				count = count * int(n[j])

			print count,
		
		# newline just to make it pretty
		print "\n"

# value errors may occur if the input can't be cast to an int
except ValueError:
	print "Please enter a non negative integer only"
	print "-1 for exit"
