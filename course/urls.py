from django.urls import path
from .views import view_course,add_course
urlpatterns=[
    path('view/',view_course,name="course_view"),
    path('add/',add_course,name="course_add")
]