from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Courses.forms import CreateCourseForm
from Courses.models import Course, Section


# Create your views here.
#pagina principal
def index(request):
    courses = Course.objects.all()[:3]
    return render(request, 'courses/Index.html', {'courses': courses})


#pagina de AllCourse
def AllCourses(request):
    courses = Course.objects.all()
    return render(request, 'courses/AllCourses.html', {'courses': courses})

#detalles de los cursos
def details(request, id):
    course = Course.objects.get(id=id)
    sections = Section.objects.filter(course=course)
    return render(request, 'courses/Details.html', {'course': course, 'sections': sections})

#search function
def searchCourses(request):
    searched = request.POST['searched']
    courses = Course.objects.filter(title__contains=searched)
    return render(request, 'courses/SearchResultCourse.html', {'courses': courses})

@staff_member_required
def CreateCourse(request):
    if request.method == 'POST':
        form = CreateCourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return  redirect('/courses')

    else:
        form = CreateCourseForm()
    return render(request, 'dashboard/CreateCourse.html', {'form': form})



#Detalles de las secciones
@login_required
def sectionDetail(request,pk, id):
    section = Section.objects.get(id=id, course_id=pk)
    allsections = Section.objects.filter(course=pk)
    return render(request, 'courses/Section.html', {'section': section, 'allsections': allsections})