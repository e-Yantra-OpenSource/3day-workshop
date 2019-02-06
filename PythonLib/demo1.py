import math
def summ(a, b):
	return a+b;

def sub(a, b):
	return a-b;

def mul(a, b):
	return a*b;

def div(a, b):
	return a/b;

def concat(a, b):
	return str(a+b);

def isPrime(a):
	aroot = int(a**(0.5));
	for i in range(2, math.floor(aroot)+1):
		if(a%i == 0):
			return "No";
	return "Yes";

def greater(a, b):
	if(a > b):
		return True;
	else:
		return False;
		
