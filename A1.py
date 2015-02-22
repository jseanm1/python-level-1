# Solution to A1
try:
	# input is a string eg: "1 2 3 4 5 6 7 8"
	input = raw_input ("Enter points: ")
	
	# input_List is a list of strings eg: ["1", "2",...]
	input_List = input.split()

	# have to have 8 and only 8 numbers
	if (len(input_List) != 8):
		print "Input size mismatch!!!"
		exit()

	x = []
	y = []

	# store x and y seperately. convert them to integers 
	for i in range (0,4):
		x = x + [int(input_List[i])]
		y = y + [int(input_List[i+4])]
	
	# check x,y
	print x
	print y

	# have to find a,b,c
	a = y[1] - y[0]
	b = x[0] - x[1]
	c = x[0]*(y[0]-y[1]) + y[0]*(x[1]-x[0])

	print "a = ", a
	print "b = ", b
	print "c = ",c

	coef_p3 = a*x[2]+b*y[2]+c
	coef_p4 = a*x[3]+b*y[3]+c

	print "cp3 = ", coef_p3
	print "cp4 = ", coef_p4

	if ((coef_p3 * coef_p4) > 0):
		print "Output: p3 and p4 are on the same side"
	elif ((coef_p3 * coef_p4) < 0): 
		print "Output: p3 and p4 are on the opposite sides"
	else:
		print "Assumption of p3 and p4 not being in the same line with p1 and p2 false"

except	ValueError:
	print "Please enter integers only. No fractions or other characters allowed"
	


