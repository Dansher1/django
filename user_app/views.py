from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
from .forms.myform import Studentform

# Create your views here.

def users(request):
    students =Student.objects.all()
    # return HttpResponse(students)
    return render(request,'users.html',{'students':students})

def create(request):
    if request.method == 'GET':
        form = Studentform()
        return render(request,'form.html',{'form':form})
    else:
        form = Studentform(request.POST,request.FILES)
        if form.is_valid():
            first_name =form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            image=form.cleaned_data['file']
            student =Student(first_name = first_name, last_name = last_name, email = email,image = image)
            student.save()
            return redirect('users')
        else:
            return redirect('create')
        

def update(request,id):
    student =Student.objects.get(pk=id)
    if request.method == 'GET':
        return render(request,'update_form.html',{'student':student})
    else:
        first_name =request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')

        student.first_name = first_name
        student.last_name = last_name
        student.email= email
        student.save()
        return redirect('users')
    
def delete(request,id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('users')











