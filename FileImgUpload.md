## File & Image Uploads

- you have to install this package that helps in uploading of the image

```python
pip install pillow
```

- in settings.py at the end

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

- in main project's urls.py

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- create a model with image field

```python
from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profiles/')

    def __str__(self):
        return self.name
```

- create a profile form so that we can use this form directly 

```python
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['name', 'image']
```

- in views.py 

```python
def upload_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Picture Uploaded successfully')
            return redirect('view_profile')
        else:
            messages.error(request, "Error Uploading profile picture")
    else:
        form = ProfileForm()
    return render(request, 'accounts/upload_profile.html', {'form':form})

def view_profile(request):
    profile = Profile.objects.all()
    return render(request, 'accounts/view_profile.html', {'profiles':profile})
```

- we can upload and view the profile in templates using

```python
{% extends "accounts/base.html" %}

{% block content %}

<h2>Upload Profile Picture</h2>
<form method="POST" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Upload</button>
</form>
{% endblock %}




{% extends "accounts/base.html" %}

{% block content %}

<h2>View Profile Picture</h2>
<ul>
    {% for profile in profiles %}
    <li>
        {{profile.name}}<br/>
        <img src="{{profile.image.url}}" width="200"/>
    </li>
    {% endfor %}
</ul>

{% endblock %}
```
