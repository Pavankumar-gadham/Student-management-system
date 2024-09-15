from django.shortcuts import render
from .models import Student
from .forms import StudentInfoForm
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q

def list_student(request):
    #student = Student.objects.all() # it will fetch entire data from database and it will place in object student
    student = Student.objects.all().values
    return render(request, "crud/list_student.html", {"student": student})

def update_student(request, id): # when we click on submit the method will be post, first it is getting the data from db then it will take the data from the form and it chesks the data is valid or not, if valid saves in the db then it will take you to the homepage 
    if request.method == "POST":
        student = Student.objects.get(pk = id)
        fm = StudentInfoForm(request.POST, instance=student)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
        
    else:
        student = Student.objects.get(pk = id)
        fm = StudentInfoForm(instance=student)
    return render(request, "crud/update_student.html", {"form": fm})

def delete_student(request, id):
    if request.method == "POST":
        student = Student.objects.get(pk = id)
        student.delete()
        return HttpResponseRedirect("/")
    
def add_student(request):
    if request.method == "POST":
        fm = StudentInfoForm(request.POST) #taking the data of the form 
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/") #comes back to the home page if data valid
        
    else:
        fm = StudentInfoForm() #when its a get method it will call the add.html page
    return render(request, "crud/add.html", {"form":fm})

def search_student(request):
    if request.method =="POST":
        search = request.POST.get("output") # get the data which is there in the field output
        student = Student.objects.all() #accessing all the data from the db
        std=None # if nothing in search box matches it shows error as none
        if search:
            std = student.filter(
                Q(fname__icontains=search)| #icontains means caseinsensitive p=P
                 Q(lname__icontains=search)| #"|" is "or" operator make use of Q operator if we use | or and operator
                  Q(email__icontains=search)|
                   Q(branch__icontains=search)) 
        return render(request, "crud/list_student.html", {"student":std})
            
    
    else:
        return HttpResponse("An error occurred!")


    
    
    
