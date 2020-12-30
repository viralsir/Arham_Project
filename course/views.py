from django.shortcuts import render
from django import forms

courses_list=[('1','c'),('2','java'),('3','python'),(4,"SQL")]
class AddCourseForm(forms.Form):
    id=forms.IntegerField(label="Course Id")
    name=forms.CharField(max_length=45,label="Course Name :")
    courses=forms.ChoiceField(choices=courses_list)
    fees=forms.IntegerField(min_value=1,max_value=10000)

# Create your views here.
def view_course(request):
    return render(request,"course/viewcourse.html")

def add_course(request):
    return render(request,"course/addcourse.html",{
        "form":AddCourseForm()
    })
