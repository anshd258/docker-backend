# Basic Requirements
- Docker:  https://www.docker.com/products/docker-desktop

# STEPS OF INSTALLATION

-Clone the repo: git clone https://github.com/brisphere/django-backend.git
-Change the current directory: cd django-backend
-Build the docker containers: docker-compose build 
-Run the docker containers: docker-compose up 

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