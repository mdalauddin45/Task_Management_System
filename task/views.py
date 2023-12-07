from django.shortcuts import render,redirect
from .import forms
from .import models

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            print(task_form.cleaned_data)
            task_form.save()
            return redirect('add_task')
    else:
        task_form = forms.TaskForm()
    return render(request, 'task.html',{'form':task_form})