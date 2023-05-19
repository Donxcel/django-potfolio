# importing the main libraries from django needed for the view.py
from django.shortcuts import render, redirect
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from django.contrib import messages
from .models import Project,Info


# creating or rendering projects in our index.html 


def homepage(request):
      # getting the data from our database for the various projects
    project = Project.objects.all()
    info = Info.objects.all()
    content = {'projects':project,'info':info}

    return render(request,'index.html',content)

def contact_view(request):


    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            # we use the django default built in function to send the mail
            subject = 'Message from  portfolio website'
            form_data = {
                'name':name,
                'email': email,
                'message': message
            }
            message = '''
            From:\n\t\t{}\n
            Email:\n\t\t{}\n
            Message:\n\t\t{}\n
            '''.format(form_data['name'], form_data['email'], form_data['message'])
            EmailMessage(
                subject,
                message,
               f'{name} <{email}',
                [f'{name} < {settings.DEFAULT_FROM_EMAIL}']
            ).send()
        # rendering the results on a template
        messages.success(request, 'Your message has been sent')
        return render(request,'myapp/success.html')
    
        return render(request,'index.html')

# Create your views here.
