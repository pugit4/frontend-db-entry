from django.shortcuts import render
from .models import students_details

# Create your views here.
def students(request):
    mystudents = students_details.objects.all()
    return render(request, 'high.html', {'mystudents': mystudents})

def add_details(request):
    
    if request.method =='GET':
        return render(request, 'primary.html')
    else:
        students_details(
            firstname = request.POST.get('fname'),
            lastname = request.POST.get('lname'),
            grade = request.POST.get('grade'),
            standard = request.POST.get('standard'),
        ) .save()
        return render(request, 'primary.html')
        
        
        
    