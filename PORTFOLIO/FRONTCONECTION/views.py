from django.shortcuts import render, redirect
from . import data_git
from .models import Project, Contact
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

# Create your views here.
#
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    # emplement the mail sending function here to send the mail to the admin
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        position = request.POST['position']
        phone_number = request.POST['phone']
        message = request.POST['message']

        contact = Contact(name=name,
            email=email,
            subject=subject,
            position=position,
            phone_number=phone_number,
            message=message)
        # contct save in models the display the message to the user in page


        if len(name) < 2 or len(email) < 3 or len(subject) < 4 or len(message) < 4:
            messages.error(request, 'Please fill the form correctly')
            return redirect('contact')

        else:
            contact.save()


            # send mail to the conected persone to send the who is the fill the form
            try:
                message = f'''Name: {name}\nEmail: {email}\nSubject: {subject}\nPosition: {position}\nPhone: {phone_number}\nMessage: {message}
                 Thank you for contacting us. We will get back to you as soon as possible.
                '''
                send_mail(
                    subject='Response auto genrated from the website',
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email,],
                    fail_silently=False
                )
                messages.success(request, 'Your message has been sent successfully')
                return redirect('contact')
            except Exception as e:
                print(e)
                messages.error(request, 'Mail sending failed')
                return redirect('contact')
    return render(request, 'contact.html')

def projects(request):
    data_git.main()
    projects = Project.objects.all()
    if len(projects) == 0:
        return render(request, 'projects.html')

    return render(request, 'projects.html', {'projects': projects} )

def services(request):
    return render(request, 'service.html')
