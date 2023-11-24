from django.shortcuts import render

from core.models import Job, Project

from datetime import datetime

def index(request):
    jobs = Job.objects.all()
    projects = Project.objects.all()
    currentYear = datetime.now().year
    return render(request, 'core/index.html', {
        'jobs': jobs,
        'projects': projects,
        'year': currentYear,
    })