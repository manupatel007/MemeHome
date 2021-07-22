from django.shortcuts import render
from .forms import UserForm, TasksForm
from .models import Tasks
from django.http import JsonResponse
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def sign_up(request):
    if(request.method=='GET'):
        context = {'form':UserForm}
        return render(request, 'signup.html', context)
    else:
        form = UserForm(request.POST)
        if(form.is_valid()):
            v = form.save()
            response_data = {'message':'Submitted Sucessfully'}
            return JsonResponse(response_data, status=201)
        else:
            return render(request, 'signup.html',{'form':form}) #This form will have error text

def create_task(request):
    if(request.method=="GET"):
        context = {'form':TasksForm}
        return render(request, 'createtask.html', context)
    else:
        form = TasksForm(request.POST)
        if(form.is_valid()):
            v = form.save()
            response_data = {'message':'Submitted Sucessfully'}
            return JsonResponse(response_data, status=201)
        else:
            return render(request, 'createtask.html', {'form':form})

def view_task(request):
    tasks_data = Tasks.objects.all()
    paginator = Paginator(tasks_data, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'viewtask.html', {'page_obj': page_obj})