# Solution to A2
while True:
	
	try:
		# get n
		n = int(raw_input("Enter n\t: "))
		
		# if n = 0 exit
		if (n == 0):
			print "Program terminated"
			break
		
		# if n < 0 continue
		if (n < 0):
			print "Please enter non negative integers only"
			continue

		# list to store binary 1's and 0's
		bin = []
		
		# find modulo, add to the FRONT of list, divide by 2 for next iteration
		while (n > 0):
			bit = n % 2
			bin = [bit] + bin
			n = n / 2

		print "Output\t: ",
		
		# print binary representation of n
		for b in bin:
			print b,

		print "=",
	
		for i in range (0,len(bin)):
			bit = bin[-1-i]
			print str(bit) + "*2^" + str(i),
			
			if (i < (len(bin)-1)):
				print "+",
			else:
				print ""
	except ValueError: 
		print "Please enter non negative integers only"
