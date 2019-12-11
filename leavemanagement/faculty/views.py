from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Faculty
from student.models import Application, Student


def FacultyHome(request):
    return render(request, 'faculty/home.html')

def PendingApplications(request):
    user = request.user
    faculty = Faculty.objects.all().filter(user=user).first()
    applications = Application.objects.all().filter(faculty=faculty, is_pending=True)
    context = {
        'applications': applications,
    }

    return render(request, 'faculty/pending.html', context)

def AcceptApplication(request, app_id):
    application = Application.objects.all().filter(id=app_id).first()
    faculty = application.faculty
    # if faculty.is_hod:
    #     application.accepted = True
    #     application.is_pending = False
    #     application.save()
    # else:
    #     department = faculty.department
    #     HOD = Faculty.objects.all().filter(department=department, is_hod=True).first()
    #     application.faculty = HOD
    #     application.save()
    # return redirect("FacultyPendingApplications")
    pass

def RejectApplication(request, app_id):
    pass