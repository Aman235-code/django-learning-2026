## Django Signals

- when new user is created a welcome email is sent to that user after firing save button 
- create signals.py inside the app folder
- 2 types of signals presave(before going into the db and postsave(after data inserted to the db)

```python
# signals.py
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
```

- make changes in apps.py

```python
from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        import blog.signals # Import signals to ensure they are registered
```

- then in settins.py installed apps

```python
 'blog.apps.BlogConfig',
```
