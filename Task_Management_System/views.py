from django.shortcuts import render
from category.models import Category
# Create your views here.

def show_task(request):
    data = Category.objects.all() 
    return render(request, 'show_task.html',{'data':data})