from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
# Create your views here.
def index(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request,'core/reg_form.html',{'form':form})
def details(request):
    details = Student.objects.all()
    return render(request,'core/reg_details.html',{'details':details})