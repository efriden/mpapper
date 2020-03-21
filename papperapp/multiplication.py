import random

def generate_mult_exercises(n):
	problems = []
	answers = []
	for i in range(n):
		triple_problems = []
		triple_answers = []
		a = random.randint(2,9)
		b = random.randint(2,9)
		for i in range(3):
			res = generate_mult(a,b,i)
			triple_problems.append(res[0])
			triple_answers.append(res[1])
		problems.append(triple_problems)
		answers.append(triple_answers)
	return [problems, answers]

def generate_mult_problems(n):
	problems = []
	answers = []
	for i in range(n):
		triple_problems = []
		triple_answers = []
		for i in range(3):
			a = random.randint(2,9)
			b = random.randint(2,9)
			res = generate_mult(a,b,2)
			triple_problems.append(res[0])
			triple_answers.append(res[1])
		problems.append(triple_problems)
		answers.append(triple_answers)
	return [problems, answers]

def generate_mult_example(a,b):
	result = []
	for i in range(3):
		result.append(generate_mult(a,b,i,False))
	return result

def generate_mult(a, b, i, random_exp = True):
	if (i == 2 and random_exp):
		exp = random.randint(2,4)
	else:
		exp = i
	new_b = round(b*(10**(-exp)),exp)
	ans = round(a*new_b,exp)
	return [str(a) + "\cdot" +  swedify(new_b),
		 swedify(ans)]

def swedify(input):
	return str.replace(str(input),'.',',')
