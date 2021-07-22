from django.shortcuts import render
from .forms import UserForm, TasksForm
from .models import Tasks
from django.http import JsonResponse

# Create your views here.
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
            return render(request, 'createtask.html', 'form':form)

def view_task(request):
    tasks_data = Tasks.objects.all()
    return render(request, 'viewtask.html', {'data':task_data})