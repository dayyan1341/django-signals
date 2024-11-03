from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import Post
import time
import threading

@receiver(post_save, sender=Post)
def post_saved(sender, instance, created, **kwargs):
    if created:
        time.sleep(2)

        if instance.title.lower() == 'exception':
            raise Exception('This is an exception')
        thread_name = threading.current_thread().name
        print(f"Signal received in thread: {thread_name} - Instance created: {instance.title}")
        print(f'Printed after signal completion for post: {instance.title}')
    else:
        print(f'Post updated: {instance.title}')