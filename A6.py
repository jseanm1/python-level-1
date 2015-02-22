# Solution to A5

try:
	# get input, cast to int, may get ValueError, handled
	N = int(raw_input("Enter N (size of matrix) : "))
	
	# this program does not expect to compute matrices larger than 10x10
	if (N > 10):
		print "N should be less than 10"
		exit()

	matrix = []
	transpose = []

	# get the matrix input
	for i in range (0,N):
		raw = raw_input("Enter row " + str(i+1) + ": ")
		raw_list = raw.split()
		matrix = matrix + [raw_list]

	# get each column as a temp row and store it as a row in transpose matrix
	for i in range (0,N):
		temp_raw = []

		for j in range (0,N):
			temp_raw = temp_raw + [matrix[j][i]]

		transpose = transpose + [temp_raw]			

	print "Transpose of the input matrix is:"

	# ideally each of the elements should be right aligned as shown in the example execution 2.  
	for i in range (0,N):
		for j in range (0,N):
			print transpose[i][j] + "\t",

		print ""

# Value error may occur when non numeric input is given
except ValueError:
	print "Input should consist only of numeric values"
