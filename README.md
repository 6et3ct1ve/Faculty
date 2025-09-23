# Faculty of Natural Sciences

A Django web application for managing faculty information including departments, programs, and teachers.

## Description

This application provides:
- Overview of faculty with general information and contacts
- List of all academic programs with descriptions and coordinators
- Department pages with teaching staff information
- Admin panel for content management

## Installation

1. Clone the repository
```bash
git clone <repository-url>
cd Faculty
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser for admin panel
```bash
python manage.py createsuperuser
```

6. Start the development server
```bash
python manage.py runserver
```

7. Open browser and navigate to
```
http://127.0.0.1:8000/
```

8. Access admin panel at
```
http://127.0.0.1:8000/admin/
```

## Project Structure

```
Faculty/
├── Faculty/          # Project configuration
├── FNS/              # Main application
│   ├── templates/    # HTML templates
│   ├── static/       # CSS files
│   ├── models.py     # Database models
│   ├── views.py      # Request handlers
│   ├── urls.py       # URL routing
│   └── admin.py      # Admin configuration
└── manage.py
```