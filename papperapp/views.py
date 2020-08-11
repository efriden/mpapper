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
import papperapp.generators.fractions as f

from .forms import NameForm

#ToDo: set up jinja template inheritance

#######
#VIEWS:
#######

def home(request):
    return render(request, 'papperapp/html/index.html')

def mult(request):
    template_name = "papperapp/tex/mult.tex"
    exercise_name = "MULTIPLIKATION MED DECIMAL"
    student_names = ["test"]
    generators = {
        "lvl1": m.generate_lvl1,
        "lvl2": m.generate_lvl2,
        "example": m.generate_example,
    }

    if (request.method == 'POST'):
        student_names = request.POST['student'].split(",")

    http_response = pdf_from_generators(request, generators, template_name, exercise_name, student_names)

    return http_response

def frac(request):
    template_name = "papperapp/tex/mult.tex"
    exercise_name = "DIVISION MED DECIMAL"
    student_names = ["test"]
    generators = {
        "lvl1": f.generate_lvl1,
        "lvl2": f.generate_lvl2,
        "example": f.generate_example,
    }

    if (request.method == 'POST'):
        student_names = request.POST['student'].split(",")

    http_response = pdf_from_generators(request, generators, template_name, exercise_name, student_names)

    return http_response


###########
#FUNCTIONS:
###########

def pdf_from_generators(request, generators, template_name, exercise_name, student_names):
    pdfs = []
    answers = {}

    for student_name in student_names:
        lvl1 = generators["lvl1"](4)
        lvl2 = generators["lvl2"](2)
        answers[student_name] = lvl1[1] + lvl2[1]
        context = {
            'exercise_name': exercise_name,
            'student_name': student_name,
            #'year': datetime.now().year,
            'ex': generators["example"](3, 2),
            'q': lvl1[0],
            'p': lvl2[0],
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

    return render(request, 'papperapp/index.html', {'form': form})
