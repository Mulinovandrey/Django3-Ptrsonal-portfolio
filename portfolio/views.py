from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def home(request):
    projects = Project.objects.all() #Таким образом Джанго импортирует все данные из базы данных, конвертирует их в .py и добавляет в список
    return render(request, 'portfolio/home.html', {'projects':projects}) #переключение (взятие) файла home.html из папки info

#request - запрос
