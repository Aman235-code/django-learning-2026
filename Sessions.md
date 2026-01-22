## Django Sessions 

- first run migrations 
- djsngo_session -> in this db data will be stored
- used to save secure data in server side

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def set_session(request):
    request.session['username'] = 'aman'
    request.session['course'] = 'Django full course'
    return HttpResponse("Session data saved successfully")

def get_session(request):
    username = request.session.get('username', 'Guest')
    course = request.session.get('course', 'Not enrolled')
    return HttpResponse(f"Welcome : {username} You are learning : {course}")

def delete_session(request):
    # try:
    #     del request.session['username']
    #     del request.session['course']
    # except KeyError:
    #     pass
    # return HttpResponse("Session data deleted successfully")

    request.session.flush() # delete all session data
    return HttpResponse("All session data deleted successfully.")
```

## Django Cookies

- stores small info in browser's side
- not much secure
- data stored in key-value pairs (limited size 4kb)

```python
def set_cookie(request):
    response = HttpResponse("Cookie Set Successfully")
    response.set_cookie('username', 'Aman', max_age=60*60*24*7) # 7 days
    response.set_cookie('course', 'Django full Course', max_age=60*60*24) # 1 day
    return response

def get_cookie(request):
    username = request.COOKIES.get('username', 'Guest')
    course = request.COOKIES.get('course', 'No Course Selected')
    # return HttpResponse(f"Username: {username}, Course : {course}")
    if 'username' in request.COOKIES:
        return HttpResponse(f"Username: {username}, Course : {course}")
    else:
        return HttpResponse("No Cookies Found")
    
def delete_cookie(request):
    response = HttpResponse("Cookie Deleted Successfully")
    response.delete_cookie('username')
    response.delete_cookie('course')
    return response
```
