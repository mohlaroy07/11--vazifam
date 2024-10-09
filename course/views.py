from django.shortcuts import render, redirect
from .models import Course, Instructor

def add_course(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        duration = request.POST['duration']
        instructor_id = request.POST['instructor_id']
        Course.objects.create(name=name, description=description, duration=duration, instructor_id=instructor_id)
        return redirect('course_list')  
    instructors = Instructor.objects.all()
    return render(request, 'course_form.html', {'instructors': instructors})


def add_instructor(request):
    if request.method == 'POST':
        name = request.POST['name']
        bio = request.POST['bio']
        Instructor.objects.create(name=name, bio=bio)
        return redirect('instructor_list') 
    return render(request, 'instructor_form.html')
