from django.contrib import admin
from crudApp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list=['sRollNo','sname','sclass','sDateofbirth']

admin.site.register(Student,StudentAdmin)


