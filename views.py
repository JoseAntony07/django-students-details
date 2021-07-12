from django.shortcuts import render,redirect
from crudApp.models import Student
from crudApp.forms import StudentForm

def retrieve_view(request):
    student=Student.objects.all()
    return render(request,'index.html',{'student':student})

def create_view(request):
    form=StudentForm()
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/abc')


    return render(request,'create.html',{'form':form})

def delete_view(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('/abc')

def update_view(request,id):
    student=Student.objects.get(id=id)
    if request.method=='POST':
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/abc')
    return render(request,'update.html',{'student':student})




