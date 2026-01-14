## Tailwind CSS in Django

- create project
- goto root folder
- create app
- create virtual env
- activate -> venv\Scripts\activate
- configure settings.py
- update urls.py -> main project's URL
- create url and update views in blog's folder
- pip install django

- 1st way 
- using CDN
- copy CDN link
- <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
- paste it below title tag of template
- then you can directly use it in tag
- <h1 class="bg-sky-200">Welcome to my blog</h1>
- only for development and need internet connection


- 2nd way
- using CLI
- npm install tailwindcss @tailwindcss/cli
- you can see node_modules, package.json installed
- create static/src/input.css inside your blog folder and paste @import "tailwindcss"
- modify package.json 

```python
{
  "scripts": {
    "dev": "npx @tailwindcss/cli -i ./blog/static/src/input.css -o ./blog/static/src/output.css --watch"
  },
  "dependencies": {
    "@tailwindcss/cli": "^4.1.18",
    "tailwindcss": "^4.1.18"
  }
}
```

- then run 
- npm run dev in one terminal
- python server in an another terminal

- then paste it in main template html below title tag
-  <link rel="stylesheet" href="{% static 'src/output.css' %}">