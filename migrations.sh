python manage.py makemigrations
python manage.py makemigrations cabin
python manage.py makemigrations gig
python manage.py makemigrations package
python manage.py migrate
python manage.py shell < tools/create_superuser.py
python manage.py collectstatic --noinput