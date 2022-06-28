# Basic Requirements
- Python and MySQL to be installed in system.

# STEPS OF INSTALLATION

- Create a database using MySQL with name "backenddb"
- Change the username and password accordingly by going to backend>settings.py>DATABASE.
- Create a virtual environment and activate the environment.
- Run "pip install -r requirements.txt" to install all the dependencies
- Makemigrations using command "python manage.py makemigrations" and then run those migrations using "python manage migrate"
- Run "python manage.py runserver" to run the server.
- Create one superuser to access the admin panel using command "python manage.py createsuperuser"
- Go to admin pannel and add a few entries to each model to check the APIs.


## URLS
- localhost:8000/admin/
- localhost:8000/cabin/get-room-availability/?id=<cabin_location.id>&rooms=<number_of_rooms_required>&checkin=<checkin_date>&checkout=<checkout_date>
- localhost:8000/cabin/payment-status/?id=<paymentStatus.id>
- localhost:8000/cabin/get-booking/?id=<user.id>
- localhost:8000/cabin/create-booking/
- localhost:8000/cabin/post-testing/
- localhost:8000/package/create-package/?id=<duration>&guests=<guests>&preferences=<a_string_containing_coma_separated_ids_of_package_preferences>

###### One example of create-package url is
###### http://localhost:8000/package/create-package/?duration=6&guests=2&preferences=8,6


#### NOTE: All date formats in "YYYY-MM-DD"