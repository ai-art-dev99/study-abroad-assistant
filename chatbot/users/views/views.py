from django.http import HttpResponse, FileResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from users.models import Program, EducationDetails, WorkExperience, JobDetails
from django.conf import settings

import os
import json
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from openai import OpenAI
import fitz
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_KEY", None) 
client = OpenAI(api_key=api_key)

def programs(request):
  data = Program.objects.all()
  object_list = list(data.values())
  return render(request, 'programs.html', {'data':object_list})

def program_details(request, id=None):
  program = None
  if id is not None:
    program = Program.objects.get(id=id)
  return render(request, 'program_detail.html', {'program': program})

def program_suggestion(request):
  data = Program.objects.all()
  object_list = list(data.values())
  chatbot_response = ''
  prompt = f'Suggest some programs to the user with field computer science, these are the programs the user can intend {object_list}'
  if api_key is not None:
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    ) 

    for chunk in stream:
      if chunk.choices[0].delta.content is not None:
          chatbot_response += chunk.choices[0].delta.content

  context = {
    'response': chatbot_response
  }

  return render(request, 'program_suggest.html', context)


def jobs(request):
  data = JobDetails.objects.all()
  object_list = list(data.values())
  return render(request, 'jobs.html', {'data': object_list})

def job_details(request, id=None):
  job = None
  if id is not None:
    job = JobDetails.objects.get(id=id)
  return render(request, 'job_detail.html', {'job': job})

def job_suggestion(request):
  data = JobDetails.objects.all()
  object_list = list(data.values())
  chatbot_response = ''
  prompt = f'Suggest some jobs to the user with field computer science, these are the programs the user can intend {object_list}'
  if api_key is not None:
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    ) 

    for chunk in stream:
      if chunk.choices[0].delta.content is not None:
          chatbot_response += chunk.choices[0].delta.content

  context = {
    'response': chatbot_response
  }

  return render(request, 'job_suggest.html', context)

def visa(request):
  context = {
     'checklist': 'imm5483e',
     'forms': ['imm1294e', 'imm5257_1e']
  }
  return render(request, 'visa_page.html', context)

def display_pdf(request, pdfname):
    if pdfname is not None:
      file_path = os.path.join(settings.STATICFILES_DIRS[0], 'visa_files', f'{pdfname}.pdf')
      return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    return redirect('visa_information')

def generate_pdf(request):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    text_data = "Hello, this is a PDF created with ReportLab!"
    p.drawString(100, 750, text_data)
    
    p.showPage()
    p.save()
    
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')

def medical_test(request):
   pass

def submit_and_pay(request):
   pass

def houses(request):
  pass

def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    document = fitz.open(pdf_path)
    text = ""
    
    # Iterate through each page
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text

def split_text(text, max_length=2000):
    while len(text) > max_length:
        split_index = text.rfind('.', 0, max_length)
        if split_index == -1:
            split_index = max_length
        yield text[:split_index + 1]
        text = text[split_index + 1:]
    yield text

def get_feedback_from_gpt4(text):
    feedback = ""
    
    # Split the text into manageable chunks
    for chunk in split_text(text):
        prompt = "You are a helpful assistant. Provide detailed feedback on this text from a PDF document:\n\n" + chunk
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Assuming GPT-4 model name is "text-davinci-004"
            messages=[{"role":"user", "content":prompt}],
            max_tokens=2000,  # Increase if needed for GPT-4
            stream=True
        )
        for chunk in response:
          if chunk.choices[0].delta.content is not None:
              feedback += chunk.choices[0].delta.content
    
    return feedback

def pdf_feedback(request):
  context = {}
  base_url = settings.BASE_DIR
  feedback = ''
  if request.user.is_authenticated:
    user_workexperience = WorkExperience.objects.get(user__id=request.user.id)
    user_educationdetails = EducationDetails.objects.get(user__id=request.user.id)
    if user_workexperience.jobcv:
      context['jobcv'] = user_workexperience.jobcv.url
    
    if user_educationdetails.cv:
      context['cv'] = user_educationdetails.cv.url

    if user_educationdetails.sop:
      context['sop'] = user_educationdetails.sop.url

    if request.method == 'POST':
      filename = request.POST.get('filename').replace('/', '\\')
      pdf_path = str(base_url) + filename
      pdf_text = extract_text_from_pdf(pdf_path)
      feedback = get_feedback_from_gpt4(pdf_text)
      return render(request, 'pdfcheck.html', {'pdfs':context, 'feedback':feedback})
      
  return render(request, 'pdfcheck.html', {'pdfs': context, 'feedback': feedback})

def chat(request):
  chatbot_response = ''
  if api_key is not None and request.method == 'POST':
    user_input = request.POST.get('user_input', None)
    prompt = user_input

    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        stream=True
    ) 

    for chunk in stream:
      if chunk.choices[0].delta.content is not None:
          chatbot_response += chunk.choices[0].delta.content

  context = {
    'response': chatbot_response
  }

  template = loader.get_template('chat.html')
  return HttpResponse(template.render(context=context, request=request))
