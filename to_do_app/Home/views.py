from django.shortcuts import render,redirect
from .models import Tasks



def Home(request):

    if request.method == "POST":


        task_title = request.POST['title']
        task_date = request.POST['date']
        new_task = Tasks.objects.create(title = task_title, date_created = task_date)
        new_task.save()
        return redirect('/')


    task = Tasks.objects.all()
    return render(request,'home.html',{'tasks':task})

def Delete(request,task_id):

    task = Tasks.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect("/")


    return render(request,'delete.html')


def Update(request,task_id):


    task = Tasks.objects.get(id = task_id) 




    if request.method == "POST":
        up_title = request.POST['title']
        date = request.POST['date']

        Tasks.objects.filter(id=task_id).update(title = up_title, date_created = date)

        
        return redirect('/')
        
    return render(request, 'update.html',{'task':task})
