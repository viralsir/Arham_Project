from django.shortcuts import render,redirect
from django import forms

courses=[]

courses_list=[('1','c'),('2','java'),('3','python'),(4,"SQL")]
class AddCourseForm(forms.Form):
    id=forms.IntegerField(label="Course Id")
    name=forms.CharField(max_length=45,label="Course Name :")
    courses=forms.ChoiceField(choices=courses_list)
    fees=forms.IntegerField(min_value=5,max_value=10000)

# Create your views here.
def view_course(request):
    print(courses)
    return render(request,"course/viewcourse.html",{
        "courses":courses
    })

def add_course(request):
    if request.method == 'POST':
        form=AddCourseForm(request.POST)
        if form.is_valid():
            course_dict={}
            course_dict.__setitem__("id",form.cleaned_data["id"])
            course_dict.__setitem__("name",form.cleaned_data["name"])
            course_dict.__setitem__("courses",form.cleaned_data["courses"])
            course_dict.__setitem__("fees",form.cleaned_data["fees"])
            courses.append(course_dict)
            return redirect('course_view')
        else:
            return render(request, "course/addcourse.html", {
                "form": form
            })
    return render(request,"course/addcourse.html",{
        "form":AddCourseForm()
    })
