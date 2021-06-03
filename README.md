## Learning-Log

### This web application allows users to log the topics they are interested in and to make journal entries as they learn about the topic. 

**The home page** will describe the site and invite users to register/login.
**Once logged in**, an user can create new topic/entries, and read/edit existing entries.

### Setting up Virtual Environment**:
- Desktop\python_projects\learning_log>**python -m venv ll_env**
- Desktop\python_projects\learning_log\ll_env\Scripts>**activate**
- **(ll_env)** Desktop\python_projects\learning_log\ll_env\Scripts>**pip install django**
  -  Installed Django web framework will only be available in when the venv (ll_env environment) is active.
- **(ll_env)** C:\Users\xingy\OneDrive\Desktop\python_projects\learning_log\ll_env\Scripts>**deactivate**

### Setting up project in Django
**Creating the Project:**
- (ll_env) Desktop\python_projects\learning_log\ll_env\Scripts>**django-admin startproject learning_log .**
  - telling Django to set up a new project called learning_log;
  - the dot at the end creates the new project with a directory structure making it easy to deploy app to a server.
- (ll_env) Desktop\python_projects\learning_log\ll_env\Scripts>**dir**
  - dir (Windows; else: ls) shows Django has created the project and a manage.py file.
  - manage.py is a short program taking in the commands and feeds to relevant part of Django to run them.
- (ll_env) Desktop\python_projects\learning_log>dir learning_log
  - **settings.py** controls how Django interacts with my system and manages my project;
  - **urls.py** tells Django which pages to build in response to browser requests;
  - **wsgi.py (web server gateway interface)** helps Django serve the files it creates.

**Creating the Database:**
- (ll_env) Desktop\python_projects\learning_log>**python manage.py migrate**
  - Migrating the database: modifying the database
  - this command tells Django to ensure the database matches the current state of the project.
  - The first time running this command in a new project using SQLite, Django will create a new database.
  - Now running dir would show db.sqlite3 in addition to the project folder and ll_env and manage.py file.

**Viewing the Project:**

![Django development server default page on localhost](https://github.com/Xingyixzhang/Learning-Log/blob/main/learning_log/images/default_page_testing.png)
- (ll_env) Desktop\python_projects\learning_log>**python manage.py runserver**
  - Django starts a server called the development server. When requesting a page by entering a URL in browser, the Django server responds to that request by building the appropriate page and sending it to the browser.
  - Sample output process:
    - Watching for file changes with StatReloader
    - Performing system checks...
    - System check identified no issues (0 silenced).
    - June 01, 2021 - 21:58:49
    - Django version 3.2.3, using settings 'learning_log.settings'
    - Starting development server at http://127.0.0.1:8000/
    - Quit the server with CTRL-BREAK.
  - Starting development server at http://127.0.0.1:8000/ reports the URL where the project is being served.
  - The URL indicates that the project is listening for requests on port 8000 on your computer, which is the localhost.
  - Localhost refers to a server that only processes requests on your system; it does not allow anyone else to see the pages you're developing.

**Start an App:**
- A Django project is organized as a group of individual apps working together to make the project work as a whole.
- (ll_env) Desktop\python_projects\learning_log>**python manage.py startapp learning_logs**
- (ll_env) Desktop\python_projects\learning_log\learning_logs>**dir**

- (ll_env) Desktop\python_projects\learning_log>**python manage.py makemigrations learning_logs**
  - Migrations for 'learning_logs':
    - learning_logs\migrations\0001_initial.py
      - Create model Topic
  - the makemigrations command tells Django to figure out how to modify the DB so it can store the data associated with any new models defined.

- (ll_env) Desktop\python_projects\learning_log>**python manage.py migrate**
  - Operations to perform:
    - Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
  - Running migrations:
    - Applying learning_logs.0001_initial... OK
- This is to apply the migration and have Django modify the DB for us.

**Setting up Admin Site:**
- Only the site's admin use the admin site, no general users.
- Django allows us to create a superuser (a user with all priviledges available on the site).
- To create a super user: (ll_env) Desktop\python_projects\learning_log>**python manage.py createsuperuser**
  - enter **username, email, password** to create the super user.

**Using Django Shell** (just like how we'd use py shell) 
- (ll_env) Desktop\python_projects\learning_log>**python manage.py shell**
- Each time modifying the models, we need to restart the shell to see the effects of those changes.
- Windows: CTRL Z + Enter to exit Shell.

**Making Web Pages with Django:**
- Three Stages: defining URLs + Writing Views + Writing Templates
- URL maps to a view, which often renders the page using a template, which contains the page's overall structure.
