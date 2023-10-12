# Links Page Backend
Welcome to the Django Portfolio Linktree Clone! This project provides a quick and efficient way to set up a personal portfolio with multiple links, similar to the popular Linktree service. Built with Django and the Django Rest Framework, it's designed to be easily deployable, customizable, and extendable.

## Features:
User Registration & Authentication: Securely register and login to manage your links.
CRUD Operations: Add, modify, delete, and view links directly via the Django admin panel or through API endpoints.
Responsive Design: Looks great on both desktop and mobile devices.
Customizable Appearance: Personalize your portfolio's colors, fonts, and more.
API-First Design: Easily integrate with other systems or expand functionality using the provided API endpoints.

## Prerequisites:
Python (>= 3.7)
Django (>= 3.2)
Django Rest Framework

## Installation & Setup:
### Clone the Repository:
```
git clone https://github.com/your-github-username/django-portfolio-linktree-clone.git
cd django-portfolio-linktree-clone
```

### Set Up a Virtual Environment:
```
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### Install Dependencies:
```
pip install -r requirements.txt
```

### Set Up the Database:
```
python manage.py makemigrations
python manage.py migrate
```

### Run the Development Server:
```
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to view your site! Access the admin panel at http://127.0.0.1:8000/admin/.
