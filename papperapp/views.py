from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
import re
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
import random

from django_tex.shortcuts import render_to_pdf

#######
#VIEWS:
#######
def test(request):
    template_name = 'tex/test.tex'
    context = {'foo': 'Bar'}
    return render_to_pdf(request, template_name, context, filename='test.pdf')

def fractions(request):
	template_name = 'tex/fractions.tex'
	context = {
		'exercise_name': 'BRÅK MED DECIMAL',
		'student_name': 'Elev Testson',
		'numbers': generate_exercises(3),
		}
	for key in context:
		if (type(context[key]) == str):
			context[key] = tex_escape(context[key])
	return render_to_pdf(request, template_name, context, filename='test.pdf')

def mult(request):
	template_name = 'tex/mult.tex'
	context = {
		'exercise_name': 'MULTIPLIKATION MED DECIMAL',
		'student_name': 'Elev Testson',
		'ex': generate_mult_example(3, 2),
		'q': generate_mult_exercises(3),
		}
	for key in context:
		if (type(context[key]) == str):
			context[key] = tex_escape(context[key])
	return render_to_pdf(request, template_name, context, filename='test.pdf')

###########
#FUNCTIONS:
###########
def generate_exercises(n):
	result = []
	for i in range(n):
		result.append(generate_fraction_triple())
	return result

def generate_mult_exercises(n):
	result = []
	for i in range(n):
		result.append(generate_mult_triple())
	return result

def generate_fraction_triple():
	results = []
	for i in range(3):
		results.append(generate_fraction())
	return results

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

def generate_fraction():
	a = random.randint(2,9)
	b = 0.1
	c = int(a/b)
	return [str(a), swedify(b), swedify(c)]

def generate_mult(a, b, i):
	new_b = round(b*(10**(-i)),i)
	ans = round(a*new_b,i)
	return [str(a) + "\cdot" +  swedify(new_b),
		 swedify(ans)]

def swedify(input):
	return str.replace(str(input),'.',',')

def tex_escape(text):
    """
        :param text: a plain text message
        :return: the message escaped to appear correctly in LaTeX
    """
    conv = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\^{}',
        '\\': r'\textbackslash{}',
        '<': r'\textless{}',
        '>': r'\textgreater{}',
		'Å': r'\AA ',
    }
    regex = re.compile('|'.join(re.escape(str(key)) for key in sorted(conv.keys(), key = lambda item: - len(item))))
    return regex.sub(lambda match: conv[match.group()], text)