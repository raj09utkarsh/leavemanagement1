from django.shortcuts import render, redirect
from .forms import ApplicationForm
from .models import Application, Student
from django.contrib.auth.models import User


def StudentHome(request):
    return render(request, 'student/home.html')

def NewStudentApplication(request):
    if request.method == 'GET':
        form = ApplicationForm()
        print(request.user)
        context = {
            'title': 'Create new application',
            'form': form,
        }
        return render(request, 'student/newApplication.html', context)
    elif request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            newApplication = form.save(commit=False)
            user = User.objects.all().filter(id=request.user.id).first()
            student = Student.objects.all().filter(user=user).first()
            if student:
                newApplication.author = student
                newApplication.save()
                return redirect('StudentHome')
            else:
                print("hooh")
                return redirect("NewApplication")
        else:
            print("hola")
        return redirect('NewApplication')


def PendingApplication(request):
    user = request.user
    student = Student.objects.all().filter(user=user).first()
    application = Application.objects.all().filter(author=student,is_pending=True)
    context = {
        "title":"Pending Applications",
        'applications': application
    }
    return render(request, 'student/pending.html', context)