
from django.shortcuts import render,HttpResponse,redirect
from .models import Department,Role,Employee
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,"home.html")


def All_employee(request):
    emps=Employee.objects.all()
    context={'emps':emps}
    print(context)
    return render(request,"all_emp.html",context)



def ADD_employee(request):
    if request.method == 'POST':
        emp_id=request.POST["emp_id"]
        first_name=request.POST['first_name']
        last_name=request.POST["last_name"]
        email=request.POST['email_id']
        salary=int(request.POST["salary"])
        bonus=int(request.POST["bonus"])
        dept=int(request.POST["dept"])
        role=int(request.POST["role"])
        new_emp=Employee(emp_id=emp_id,first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,dept_id=dept,role_id=role,email=email)
        new_emp.save()
        return HttpResponse("successfully added in employee details...")
        
    elif request.method == "GET":
        return render(request,"add_emp.html")
    else:
        return HttpResponse("Exception is occured...")
    


def Remove_employee(request,emp_id=0):
    if emp_id:
        try:
            emp_remove=Employee.objects.get(id=emp_id)
            emp_remove.delete()
            return HttpResponse("<h1>Employee successfully removed...</h1>")
        except:
            return HttpResponse("Please enter a valid ..")
    emps=Employee.objects.all()
    context={'emps':emps}
    return render(request,"remove.html",context)

def filter_employee(request):
    if request.method == 'POST':
        name=request.POST['name']
        dept_id=request.POST['dept']
        role_id=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept_id:
            emps=emps.filter(dept__name=dept_id)
        if role_id:
            emps=emps.filter(role__name=role_id)
            
        context={'emps':emps}

        return render(request,"all_emp.html",context)

    elif request.method =="GET":
        return render(request,"filter.html")
    else:
        return HttpResponse("<h1>An Exception is occured <h1>")




