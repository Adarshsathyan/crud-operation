from django.shortcuts import render
from .forms import StudentForm
# Create your views here.
def index(request):
    form = StudentForm
    return render(request,'core/reg_form.html',{'form':form})