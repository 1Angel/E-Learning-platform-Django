from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='course-images/')
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


#videos de curso
class Section(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    video =models.FileField(upload_to='videos/', blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CourseComment(models.Model):
    description = models.TextField(max_length=500)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

class SectionComment(models.Model):
    description = models.TextField(max_length=500)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description