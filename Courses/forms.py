from django import forms
from django.forms import ModelForm

from Courses.models import Course, SectionComment


#
# class CreateCourseForm(forms.Form):
#     title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
#     image = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))


class CreateCourseForm(ModelForm):

    class Meta:
        model = Course
        fields = ["title", "description", "image"]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control'}),
            "image": forms.FileInput(attrs={'class': 'form-control'}),
        }

class SectionCommentForm(ModelForm):
    class Meta:
        model = SectionComment
        fields = ["description"]

        widgets = {
            "description": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu comentario'}),
        }