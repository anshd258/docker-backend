python manage.py makemigrations # Create migrations for apps
python manage.py makemigrations cabin # Create migrations for apps
python manage.py makemigrations service # Create migrations for apps
python manage.py makemigrations user # Create migrations for apps
python manage.py makemigrations package # Create migrations for apps
python manage.py makemigrations gig # Create migrations for apps
python manage.py migrate # Apply migrations to the database
python manage.py shell < tools/create_superuser.py
python manage.py collectstatic --noinput