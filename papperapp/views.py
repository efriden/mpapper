from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.template import RequestContext
import re
import io
from django.http import FileResponse
#from reportlab.pdfgen import canvas
import random
import datetime

from PyPDF2 import PdfFileMerger, PdfFileReader

from django_tex.shortcuts import render_to_pdf, compile_template_to_pdf

import papperapp.multiplication as m

#ToDo: set up jinja template inheritance

#######
#VIEWS:
#######

def mult(request):
	template_name = 'tex/mult.tex'
	student_names = ['Elev Testson1','Elev Testson2','Elev Testson3']
	exercise_name = "MULTIPLIKATION MED DECIMAL"

	pdfs = []
	answers = {}

	for student_name in student_names:
		questions = m.generate_mult_exercises(4)
		problems = m.generate_mult_problems(2)
		answers[student_name] = questions[1] + problems[1]
		context = {
			'exercise_name': exercise_name,
			'student_name': student_name,
            'year': datetime.now().year,
			'ex': m.generate_mult_example(3, 2),
			'q': questions[0],
			'p': problems[0],
			}
		for key in context:
			if (type(context[key]) == str):
				context[key] = tex_escape(context[key])

		buffer = io.BytesIO(compile_template_to_pdf(template_name, context))

		pdfs.append(buffer)

	#answer_context = ""
	#for student_name in answers:
	#	answer_context += "\section*{" + student_name + "} "
	#	answer_context += "\begin{wrapfigure} "
		#todo - make it a list of inputs and iterate with jinja (% for .... %) or whatever




		#for i in range(len(answers[student_name])):
		#	answer_context += str(i+2)
		#	answer_context += ":"

		#	letters = ["a", "b", "c"]
		#	for j in range(3):
		#		answer_context += letters[j]
		#		answer_context += ")"
		#		answer_context += answers[student_name][i][j]
		#		answer_context += " "

		#	answer_context += "\\\\ "

		#answer_context += "\end{wrapfigure}"

	#answer_context = tex_escape(answer_context)



	answer_page = io.BytesIO(compile_template_to_pdf("tex/answers.tex", {"content": answers, "exercise_name": exercise_name}))

	merger = PdfFileMerger()

	for pdf in pdfs:
		merger.append(PdfFileReader(pdf))

	merger.append(PdfFileReader(answer_page))

	output_buffer = io.BytesIO()

	merger.write(output_buffer)

	http_response = HttpResponse(output_buffer.getvalue() , content_type='application/pdf')
	http_response['Content-Disposition'] = 'filename="mattepapper.pdf"'

	return http_response



# def fractions(request):
# 	template_name = 'tex/fractions.tex'
# 	context = {
# 		'exercise_name': 'BRÅK MED DECIMAL',
# 		'student_name': 'Elev Testson',
# 		'numbers': generate_exercises(3),
# 		}
# 	for key in context:
# 		if (type(context[key]) == str):
# 			context[key] = tex_escape(context[key])
# 	return render_to_pdf(request, template_name, context, filename='test.pdf')


###########
#FUNCTIONS:
###########

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
