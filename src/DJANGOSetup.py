# ============================================================
# 🧱 DJANGO PROJECT STRUCTURE AND SETUP — BEGINNER'S GUIDE
# ============================================================

# ============================================================
# 📘 1️⃣ INTRODUCTION TO DJANGO
# ============================================================
# Django is a high-level Python web framework that allows you to
# build web applications rapidly and with clean, maintainable code.
#
# It follows the MVT pattern:
#   M — Model (Database structure)
#   V — View (Business logic)
#   T — Template (HTML presentation)
#
# Django comes with built-in tools for:
# - Authentication
# - Database handling
# - Admin interface
# - URL routing
# - Template rendering
# and much more.

# ============================================================
# ⚙️ 2️⃣ INSTALLING DJANGO
# ============================================================
# ✅ Step 1: Verify Python and pip are installed
# ------------------------------------------------------------
# > python --version
# > pip --version
#
# ✅ Step 2: Install Django globally
# ------------------------------------------------------------
# > pip install django
#
# ✅ Step 3: Verify Django installation
# ------------------------------------------------------------
# > python -m django --version
# (You should see something like 5.2.x)
#
# NOTE 🧠: You can also install Django inside a virtual environment
# if you want to isolate your project’s dependencies.
#
# Create venv (optional):
# > python -m venv myenv
# Activate it:
# > myenv\Scripts\activate      (on Windows)
# > source myenv/bin/activate   (on macOS/Linux)
# Then install Django inside:
# > pip install django

# ============================================================
# 🧱 3️⃣ CREATING YOUR FIRST DJANGO PROJECT
# ============================================================
# ✅ Step 1: Choose your desired location
# ------------------------------------------------------------
# Example:
# > F:
# > mkdir Django_project
# > cd Django_project
#
# ✅ Step 2: Create a Django project
# ------------------------------------------------------------
# > django-admin startproject myproject .
# (The dot '.' ensures files are created in the current folder)
#
# ✅ Step 3: Verify the folder structure
# ------------------------------------------------------------
# Django will create the following:
#
# myproject/
# ├── manage.py
# └── myproject/
#     ├── __init__.py
#     ├── settings.py
#     ├── urls.py
#     ├── asgi.py
#     └── wsgi.py
#
# ✅ Step 4: Run the Django development server
# ------------------------------------------------------------
# > python manage.py runserver
#
# ✅ Step 5: Open browser and visit
# ------------------------------------------------------------
# http://127.0.0.1:8000/
# You’ll see the Django rocket 🚀 page!

# ============================================================
# 🏗️ 4️⃣ UNDERSTANDING PROJECT STRUCTURE
# ============================================================
# Let’s break down each file/folder created by Django 👇
#
# 1. manage.py
#    → Command-line utility to interact with your project.
#      Examples:
#      > python manage.py runserver
#      > python manage.py startapp myapp
#      > python manage.py migrate
#
# 2. myproject/ (inner folder)
#    → Contains all project configuration files.
#
#    ├── __init__.py
#    │     - Makes this directory a Python package.
#    │
#    ├── settings.py
#    │     - Contains project settings like:
#    │       * Installed apps
#    │       * Database configuration
#    │       * Static file settings
#    │       * Middleware and templates
#    │
#    ├── urls.py
#    │     - URL routing (maps web URLs to Python views)
#    │     Example:
#    │         path('admin/', admin.site.urls)
#    │
#    ├── wsgi.py
#    │     - Web Server Gateway Interface
#    │       Used for deployment on web servers like Apache/Nginx.
#    │
#    └── asgi.py
#          - Asynchronous Server Gateway Interface
#          - Supports async features (e.g., WebSockets).

# ============================================================
# 🧩 5️⃣ CREATING YOUR FIRST DJANGO APP
# ============================================================
# ✅ Step 1: Create an app inside your project
# ------------------------------------------------------------
# > python manage.py startapp myapp
#
# Folder structure created:
# myapp/
# ├── admin.py
# ├── apps.py
# ├── models.py
# ├── tests.py
# ├── views.py
# └── __init__.py
#
# ✅ Step 2: Register your app in settings.py
# ------------------------------------------------------------
# Open settings.py and add:
# INSTALLED_APPS = [
#     ...
#     'myapp',
# ]
#
# ✅ Step 3: Create a simple view
# ------------------------------------------------------------
# In views.py:
#     from django.http import HttpResponse
#
#     def home(request):
#         return HttpResponse("Hello, Django!")
#
# ✅ Step 4: Create a URL for this view
# ------------------------------------------------------------
# Create file: myapp/urls.py
#     from django.urls import path
#     from . import views
#
#     urlpatterns = [
#         path('', views.home),
#     ]
#
# ✅ Step 5: Link your app’s URL to the main project
# ------------------------------------------------------------
# In myproject/urls.py:
#     from django.contrib import admin
#     from django.urls import path, include
#
#     urlpatterns = [
#         path('admin/', admin.site.urls),
#         path('', include('myapp.urls')),
#     ]
#
# ✅ Step 6: Run the server again
# ------------------------------------------------------------
# > python manage.py runserver
#
# Visit: http://127.0.0.1:8000/
# You’ll see: “Hello, Django!”

# ============================================================
# 🧭 6️⃣ OPENING PROJECT IN PYCHARM
# ============================================================
# ✅ Step 1: Open PyCharm → Click "Open" → Choose your folder (e.g., F:\Django_project)
#
# ✅ Step 2: Configure Python Interpreter
# ------------------------------------------------------------
# Choose:
#   - System Interpreter (since you installed Django globally)
#   - Path: C:\Users\Vinay Mishra\AppData\Local\Programs\Python\Python314\python.exe
#
# ✅ Step 3: Verify Django
# ------------------------------------------------------------
# In PyCharm terminal:
# > python -m django --version
# Output: 5.2.7
#
# ✅ Step 4: Run project from PyCharm
# ------------------------------------------------------------
# Run → Edit Configurations → + → Django Server
# Host: 127.0.0.1
# Port: 8000
# Apply → Run

# ============================================================
# 🧠 7️⃣ SUMMARY
# ============================================================
# ✅ Django project = Configuration + Apps
# ✅ Each app = models + views + templates + urls
# ✅ manage.py = Command-line tool for all operations
# ✅ settings.py = Heart of configuration
# ✅ urls.py = Connects routes to logic
# ✅ Run server with: python manage.py runserver
#
# Once this foundation is clear, you can move into:
# - Templates (HTML rendering)
# - Models (Database tables)
# - Admin panel customization
# - Static files & media
# - User authentication
#
# 🏁 Congratulations — you now understand the Django project structure!

# ============================================================
# END OF DOCUMENT
# ============================================================
