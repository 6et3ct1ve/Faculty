from django.contrib import admin
from .models import Department, Program, Teacher, HomePage


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "head"]
    search_fields = ["name"]


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ["code", "name", "department", "coordinator_name"]
    list_filter = ["department"]
    search_fields = ["name", "code"]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["name", "position", "degree", "department"]
    list_filter = ["department", "position"]
    search_fields = ["name"]


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ["title"]
