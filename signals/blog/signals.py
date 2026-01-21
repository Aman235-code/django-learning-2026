from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Blog

# Trigger before saving a blog
@receiver(pre_save, sender=Blog)
def before_blog_save(sender, instance, **kwargs):
    print(f"About to save blog[Pre-Save]: {instance.title}")

# Trigger after saving a blog
@receiver(post_save, sender=Blog)
def after_blog_save(sender, instance, created, **kwargs):
    if created:
        print(f"New Blog Created[Post-Save]: {instance.title}")
    else:
        print(f"Blog Updated[Post-Save]: {instance.title}")