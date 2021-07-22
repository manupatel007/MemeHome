from django.shortcuts import render
from .models import TaskType
# Create your views here.

def hierarchy_view(request):
    data = TaskType.objects.all()
    return render(request, 'result.html', {'data':data})
    #print(data.values())
    #what i tried..
    '''size = len(data)

    dict1 = {}

    for j in range(1,size+1):
        dict1[j] = []
    
    for dat in data:
        if(dat.parent_id):
            dict1[dat.parent_id.si_no].append({'name': dat.title})
        else:
            dict1[dat.si_no].append({'name': dat.title})

    to_be_deleted = []

    for key in dict1:
        if(len(dict1[key])==0):
            to_be_deleted.append(key)

    for elem in to_be_deleted:
        del dict1[elem]
    
    print(dict1)
    
    return render(request, 'result.html', {'data':dict1})'''
