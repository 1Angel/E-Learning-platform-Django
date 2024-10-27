from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Courses.forms import CreateCourseForm, SectionCommentForm
from Courses.models import Course, Section, SectionComment


# Create your views here.
#pagina principal
def index(request):
    courses = Course.objects.all()[:3]
    return render(request, 'courses/Index.html', {'courses': courses})


#pagina de todos nuestros cursos
def AllCourses(request):
    courses = Course.objects.all()
    return render(request, 'courses/AllCourses.html', {'courses': courses})

#detalles de los cursos
def details(request, id):
    course = Course.objects.get(id=id)
    sections = Section.objects.filter(course=course)
    return render(request, 'courses/Details.html', {'course': course, 'sections': sections})

#funcion de buscar
def searchCourses(request):
    searched = request.POST['searched']
    courses = Course.objects.filter(title__contains=searched)
    return render(request, 'courses/SearchResultCourse.html', {'courses': courses})

#creacion de los cursos - solo admins
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


#Detalles de las videos y para mostrar los comentarios
@login_required
def sectionDetail(request,pk, id):
    section = Section.objects.get(id=id, course_id=pk)
    allsections = Section.objects.filter(course=pk)
    comments = SectionComment.objects.filter(section=id).order_by('-created_at')


    if request.method == 'POST':
        form = SectionCommentForm(request.POST)
        if form.is_valid():
            new_comment =form.save(commit=False)
            new_comment.section = section
            new_comment.user = request.user
            new_comment.save()
            return redirect('section', pk, id)
    else:
        form = SectionCommentForm()
    return render(request, 'courses/Section.html', {'section': section, 'allsections': allsections, 'comments': comments, 'form': form})






