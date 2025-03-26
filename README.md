# Django Task Management System

## Description
This is a Task Management System made using Django and Bootstrap.
<br>

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/SumanGautam1/task_management.git

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt

3. Create a ```.env``` file in your root directory and configure your SECRET KEY.
    You can generate a secure key using:
    ```bash
    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

4. Run migrations:
    ```bash
    python manage.py migrate

5. Create superuser for easier handling of data.
    ```bash
    python manage.py createsuperuser

6. Run migrations again:
    ```bash
    python manage.py makemigrations
    python manage.py migrate

7. Start the development server:
    ```bash
    python manage.py runserver

## UI Screenshots

### Dashboard Page
![Dashboard](assets/dashboard.png?raw=true "Dashboard")

### Manage Tasks Page
![Manage Task](assets/manage.png?raw=true "Manage Task")

## Task List Page
![Task List](assets/tasklist.png?raw=true "Task List")