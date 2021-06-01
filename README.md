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
