from django.shortcuts import render, get_object_or_404 #функция get_object_or_404 позволяет найти нужное значение или вывести 404
from .models import Blog # импорт Блога

def all_blogs(request):
    blogs = Blog.objects.order_by('-date') #через order_by задаются парамерты отображения ('-date' - отображение по дате публикации, [:5] - отображаются 5 последних публикаций)
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id) #pk - термин из БД, означает первичный ключ
    return render(request, 'blog/detail.html', {'blog':blog})
