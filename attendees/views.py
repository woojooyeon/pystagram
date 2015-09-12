from django.shortcuts import render
from attendees.models import Attendees

#Create your views here.

def index(request):
    student_list = Attendees.objects.all()
    return render(request, 'attendees/index.html', {
            'student_list': student_list,
        })