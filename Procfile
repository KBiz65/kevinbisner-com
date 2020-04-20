web: gunicorn kbsite.wsgi:application --access-logfile=- --timeout 10
release: python manage.py migrate --no-input