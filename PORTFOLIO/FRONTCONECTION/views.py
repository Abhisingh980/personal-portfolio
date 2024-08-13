from django.shortcuts import render
from . import data_git#
from .models import Project

# Create your views here.
#
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

def projects(request):
    data_git.main()
    projects = Project.objects.all()
    if len(projects) == 0:
        return render(request, 'projects.html')

    return render(request, 'projects.html', {'projects': projects} )

def services(request):
    return render(request, 'service.html')
