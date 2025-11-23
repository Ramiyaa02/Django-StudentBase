from django.shortcuts import render, redirect,get_object_or_404
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Student

def home(request):

    search = request.GET.get("search")
    dept_filter = request.GET.get("dept")
    grade_filter = request.GET.get("grade")
    min_marks = request.GET.get("min_marks")
    max_marks = request.GET.get("max_marks")
    sort_by = request.GET.get("sort", "id")  # default sort

    students = Student.objects.all()

    # Text search
    if search:
        students = students.filter(
            Q(name__icontains=search) |
            Q(dept__icontains=search)
        )

    # Department filter
    if dept_filter and dept_filter != "":
        students = students.filter(dept=dept_filter)

    # Grade filter
    if grade_filter and grade_filter != "":
        students = students.filter(grade=grade_filter)

    # Marks range filter
    if min_marks:
        students = students.filter(marks__gte=min_marks)

    if max_marks:
        students = students.filter(marks__lte=max_marks)

    # Sorting
    students = students.order_by(sort_by)

    return render(request, 'studentapp/home.html', {
        "students": students,
    })


def add_student(request):
    if request.method == "POST":
        student_id = request.POST.get("student_id")
        name = request.POST.get("name")
        dept = request.POST.get("dept")
        marks = request.POST.get("marks")
        grade = request.POST.get("grade")

        Student.objects.create(
            student_id=student_id,
            name=name,
            dept=dept,
            marks=marks,
            grade=grade
        )
        return redirect('home')

    return render(request, 'studentapp/add.html')


def eligible_students(request):
    eligible = Student.objects.filter(grade__in=['A', 'A+'])
    return render(request, 'studentapp/eligible.html', {'eligible': eligible})
    
    
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'studentapp/edit.html', {"student": student})


def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.student_id = request.POST.get("student_id")
        student.name = request.POST.get("name")
        student.dept = request.POST.get("dept")
        student.marks = request.POST.get("marks")
        student.grade = request.POST.get("grade")
        student.save()
        return redirect('home')

    return render(request, 'studentapp/edit.html', {"student": student})
  
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('/')
    
def student_details(request):
    students = Student.objects.all()
    return render(request, 'studentapp/student_details.html', {"students": students})
    

def student_profile(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'studentapp/student_profile.html', {"student": student})

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "studentapp/login.html")


def logout_user(request):
    logout(request)
    return redirect('login')
   
    
    
    
