release: python manage.py migrate
web: gunicorn central_logs.wsgi --max-requests 200
