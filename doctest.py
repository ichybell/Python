import doctest
def func(x):
	"""We will use this function
	to check for doctests arguments.
	The >>> prompt acts like a python interpreter shell
	and next line should be output of function executed above
	if it is not >>>:
	>>> func(3)
	4
	>>> func(4)
	3
	"""
   return x + 1

# invoke the doctest function like this
doctest.testmod(name='func', verbose= True)
