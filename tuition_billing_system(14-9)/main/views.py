from django.shortcuts import render, redirect
from .models import Branch, Student
from .forms import BranchForm, StudentForm

def index(request):
    return render(request, 'main/index.html')

def branch_login(request):
    if request.method == 'POST':
        branch_name = request.POST['branch_name']
        password = request.POST['password']
        try:
            branch = Branch.objects.get(name=branch_name, password=password)
            request.session['branch_id'] = branch.id
            return redirect('branch_home')
        except Branch.DoesNotExist:
            # Handle error
            pass
    return render(request, 'main/branch_login.html')

def branch_home(request):
    branch_id = request.session.get('branch_id')
    if not branch_id:
        return redirect('index')
    branch = Branch.objects.get(id=branch_id)
    return render(request, 'main/branch_home.html', {'branch': branch})

def manage_students(request):
    branch_id = request.session.get('branch_id')
    if not branch_id:
        return redirect('index')
    branch = Branch.objects.get(id=branch_id)
    students = Student.objects.filter(branch=branch)
    if 'search' in request.GET:
        search_term = request.GET['search']
        students = students.filter(name__icontains=search_term)
    return render(request, 'main/manage_students.html', {'students': students, 'branch': branch})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            branch_id = request.session.get('branch_id')
            student.branch = Branch.objects.get(id=branch_id)
            student.save()
            return redirect('manage_students')
    else:
        form = StudentForm()
    return render(request, 'main/add_student.html', {'form': form})

def delete_student(request, student_id):
    Student.objects.filter(id=student_id).delete()
    return redirect('manage_students')
from django.shortcuts import render

def landing_page(request):
    return render(request, 'main/landing_page.html')
