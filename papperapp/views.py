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

import papperapp.generators.multiplication as m

from .forms import NameForm

#ToDo: set up jinja template inheritance

#######
#VIEWS:
#######

def home(request):
    return render(request, 'html/index.html');

def mult(request):
	template_name = 'tex/mult.tex'
    student_names = []
	exercise_name = "MULTIPLIKATION MED DECIMAL"

    if request.method == 'POST'
        student_names.append(request.POST['student'])

	pdfs = []
	answers = {}

	for student_name in student_names:
		questions = m.generate_lvl1(4)
		problems = m.generate_lvl2(2)
		answers[student_name] = questions[1] + problems[1]
		context = {
			'exercise_name': exercise_name,
			'student_name': student_name,
            #'year': datetime.now().year,
			'ex': m.generate_example(3, 2),
			'q': questions[0],
			'p': problems[0],
			}
		for key in context:
			if (type(context[key]) == str):
				context[key] = tex_escape(context[key])

		buffer = io.BytesIO(compile_template_to_pdf(template_name, context))

		pdfs.append(buffer)

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


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'index.html', {'form': form})
