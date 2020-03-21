import random

def generate_exercises(n):
	result = []
	for i in range(n):
		result.append(generate_fraction_triple())
	return result



def generate_fraction_triple():
	results = []
	for i in range(3):
		results.append(generate_fraction())
	return results



def generate_fraction():
	a = random.randint(2,9)
	b = 0.1
	c = int(a/b)
	return [str(a), swedify(b), swedify(c)]
