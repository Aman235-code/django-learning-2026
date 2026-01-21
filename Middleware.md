## Django Middleware

<!-- req -> middleware -> view.py -->

- used for Authentication check
- req/res logging
- IP blocking
- language / session namagement
- performance timing

### 2 types -> Built In & Custom 

### Custom Middleware

- create a middleware.py inside the app folder
- MiddlewareMixin -> backward compatibility, less code, more facility

```python
import datetime
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class SimpleLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f"[{datetime.datetime.now()}] Request URL : {request.path}")

    def process_response(self, request, response):
        print(f"[{datetime.datetime.now()}] response Status Code : {response.status_code}")
        return response

# when you run the server your website is blocked and shows this message
class BlockIpMiddleware(MiddlewareMixin):
    BLOCKED_IPS = [
        '127.0.0.1'
    ]

    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if ip in self.BLOCKED_IPS:
            return HttpResponse("Your IP is blocked", status=403)
```

- after wrting the middleware you have to register it in settings.py MIDDLEWARE

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'blog.middleware.SimpleLogMiddleware',
    'blog.middleware.BlockIpMiddleware'
]
```