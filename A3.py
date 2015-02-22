# Solution to A3

try:
	input = raw_input ("Enter Input: ")
	input_List = input.split()

	if (len(input_List) != 2):
		print "Please enter two and only two strings"
		exit()

	x = input_List[0]
	y = input_List[1]
	count = 0

	for i in range (0, min(len(x),len(y))):
		if (x[i] != y[i]):
			count += 1

	count += abs (len(x) - len(y))

	print count

except valueError:
	print "Input two strings only"
