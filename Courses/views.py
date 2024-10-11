from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from Courses.models import Course, Section


# Create your views here.
def index(request):
    courses = Course.objects.all()[:3]
    return render(request, 'courses/Index.html', {'courses': courses})

@login_required
def details(request, id):
    course = Course.objects.get(id=id)
    sections = Section.objects.filter(course=course)
    return render(request, 'courses/Details.html', {'course': course, 'sections': sections})

@login_required
def sectionDetail(request,pk, id):
    section = Section.objects.get(id=id, course_id=pk)
    allsections = Section.objects.filter(course=pk)
    return render(request, 'courses/Section.html', {'section': section, 'allsections': allsections})