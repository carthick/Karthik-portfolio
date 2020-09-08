from django.shortcuts import render
from projects.models import Projects


# Create your views here.

def all_projects(request):
    all_projects = Projects.objects.all()
    return render(request, 'projects/all_projects.html', {'all_projects':all_projects})
