from django.shortcuts import render,redirect
from .import forms

# Create your views here.
def add_category(request):
    if request.method == 'POST':
        task_form = forms.CategoryForm(request.POST)
        if task_form.is_valid():
            print(task_form.cleaned_data)
            task_form.save()
            return redirect('add_task')
    else:
        task_form = forms.CategoryForm()
    return render(request,'category.html',{'form':task_form})