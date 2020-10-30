import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

exponents = []
coefficients = []

i = 1

#Evaluates the polynomial function specified by the user
def polynomial_func(coefficients, exponents, xval):
	funcval = 0
	for i in range(len(coefficients)):
		funcval += coefficients[i]*(xval**exponents[i])

	return funcval

#This is a very lazy way of taking input. Not 100% bulletproof or efficient.
while(True):
	
	#Ask user for coefficients of the terms in the polynomial function
	coefficient = input("Enter the coefficient of term " + str(i) + " in the polynomial function or type done to stop: ")
	
	#Stop taking input if the user is done specifying a function
	if(coefficient == "done"):
		break
	
	#Attempt to read the user input. If it is not a number, yell at the user.
	try:
		float(coefficient)
		coefficients.append(float(coefficient))
		exponent = input ("Enter the exponent of term " + str(i) + " in the polynomial function: ")

		try:
			float(exponent)
			exponents.append(float(exponent))
			i += 1

		#Yell at the user if the input exponent is not an integer
		except:
			print("You did not enter a number. Try again.")	

	except:
		print("You did not enter a number. Try again.")	


#Similar to above, but now reading the lower/upper bounds on x (the domain)
while(True):

	ldomain = input("Enter the beginning of your domain: ")

	try:
		float(ldomain)
		ldomain = float(ldomain)

		udomain = input("Enter the end of your domain: ")

		try:

			float(udomain)
			udomain = float(udomain)
			break	
		except:
			print("You did not enter a number. Try again.")

	except:
	
		print("You did not enter a number. Try again.")


while(True):

	nintervals = input("Enter the number of subintervals (INTEGER): ")

	try:
		int(nintervals)
		nintervals = int(nintervals)
		break

	except:

		print("You did not enter an integer. Try again.")	


right = False
left = False

#Ask the user whether they want to evaluate a left or right sum
while(True):

	sum_type = input("Type left for left Riemann sum or right for right Riemann sum: ")

	if (sum_type == "left" or sum_type == "right"):

		if (sum_type == "left"):
			left = True

		elif (sum_type == "right"):
			right = True

		break

	else:

		print("Please choose either left or right")
	
#Calculating the Riemann sum
dx = (udomain - ldomain)/nintervals


area = 0

xvals = []
yvals = []
if (left == True):

	for i in range (0, nintervals):
		function_value = polynomial_func(coefficients, exponents, ldomain + i*dx)
		xvals.append(ldomain + i*dx)
		yvals.append(function_value)
		area += dx*(function_value)

	print("The integral is approximately " + str(area))

elif (right == True):

	for i in range (1, nintervals + 1):
		function_value = polynomial_func(coefficients, exponents, ldomain + i*dx)
		#ldomain + i*dx - dx to account for shifted index (i starts at 1)
		xvals.append(ldomain + i*dx - dx)
		yvals.append(function_value) 
		area += dx*(function_value)
	print("The integral is approximately " + str(area))


#This is a poor choice of variable name(s)
#Real x/yvals used for plotting a smooth version of the input function
real_xvals = np.arange(ldomain, udomain, 0.00001).tolist()
real_yvals = []
for i in range (len(real_xvals)):
	real_yvals.append(polynomial_func(coefficients, exponents, real_xvals[i]))

#Code for plotting
fig, ax = plt.subplots(1)

#Draws rectangles
for i in range(len(xvals)):

	ax.add_patch(patches.Rectangle((xvals[i],0),dx,yvals[i],linewidth=1,edgecolor='black',facecolor='red', alpha = 0.6))

plt.plot(real_xvals, real_yvals)
plt.scatter(xvals, yvals, color = 'lime', s = 20)
plt.title("Integral"+ r'$\approx$' +str(area) + "   " + "(n=" + str(nintervals) +")")
plt.show()
