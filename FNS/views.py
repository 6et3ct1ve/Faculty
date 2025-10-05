from django.shortcuts import render, redirect
from .models import Department, Program, Teacher, HomePage


def index(request):
    homepage = HomePage.objects.first()
    context = {"homepage": homepage}
    return render(request, "FNS/index.html", context)


def programs_list(request):
    programs = Program.objects.all()
    context = {"programs": programs}
    return render(request, "FNS/programs_list.html", context)


def program_detail(request, program_id):
    try:
        program = Program.objects.get(pk=program_id)
    except Program.DoesNotExist:
        return redirect("FNS:programs_list")

    context = {"program": program}
    return render(request, "FNS/program_detail.html", context)


def departments_list(request):
    departments = Department.objects.all()
    context = {"departments": departments}
    return render(request, "FNS/departments_list.html", context)


def department_detail(request, department_id):
    try:
        department = Department.objects.get(pk=department_id)
    except Department.DoesNotExist:
        return redirect("FNS:departments_list")

    teachers = department.teachers.all()
    context = {"department": department, "teachers": teachers}
    return render(request, "FNS/department_detail.html", context)
