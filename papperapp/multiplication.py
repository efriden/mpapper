import random

def generate_mult_exercises(n):
	result = []
	for i in range(n):
		result.append(generate_mult_triple())
	return result

def generate_mult_triple():
	result = []
	a = random.randint(2,9)
	b = random.randint(2,9)
	for i in range(3):
		result.append(generate_mult(a,b,i)[0])
	return result

def generate_mult_example(a,b):
	result = []
	for i in range(3):
		result.append(generate_mult(a,b,i))
	return result

def generate_mult(a, b, i):
	new_b = round(b*(10**(-i)),i)
	ans = round(a*new_b,i)
	return [str(a) + "\cdot" +  swedify(new_b),
		 swedify(ans)]

def swedify(input):
	return str.replace(str(input),'.',',')
