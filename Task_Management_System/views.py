from django.shortcuts import render

# Create your views here.

def show_task(request):
    return render(request, 'show_task.html')