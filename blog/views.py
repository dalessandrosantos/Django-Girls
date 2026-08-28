from django.shortcuts import render
from .models import Post
from django.utils import timezone # Importa recursos para trabalhar com data e hora

def post_view(request):   
    
    # Busca os posts já publicados (data <= agora), ordenados da mais antiga para a mais recente
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')  

    context = {
        'posts': posts
    }
    return render(request, 'blog/post_list.html', context)