from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Post
import time
import threading
from django.db import transaction

def print_all():
    all_posts = Post.objects.all()
    for post in all_posts:
        print("Title : ", post.title)

def create_post(request):
    post_created = False
    post = None

    if request.method == "POST":
        
        # Retrieve title and content from form data
        title = request.POST.get("title")
        content = request.POST.get("content")
        
        if title.lower() == 'exception':
            try :
                with transaction.atomic():
                    p = Post.objects.create(title=title, content=content)
            except Exception as e:
                print_all()
                print("Exception raised in transaction")
            return redirect('create_post')
        print(f"Instance created in thread: {threading.current_thread().name}")
       
        post = Post.objects.create(title=title, content=content)
        
       
        print("This will only be printed after the signal code is Finished")
        
        post_created = True  


    

    latest_post = Post.objects.latest('id') if Post.objects.exists() else None
    return render(request, 'demo1/create_post.html', {'post_created': False})


