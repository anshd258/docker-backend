from cabin.models.location import Location
from cabin.models.reservation import Reservation
from datetime import datetime


def datetimeObject(it):
    return datetime.strptime(str(it), '%Y-%m-%d')


def CalculateAvailability(location_id, rooms_to_be_booked, checkin, checkout):
    checkin_date = datetimeObject(checkin)
    checkout_date = datetimeObject(checkout)
    location = Location.objects.filter(id=location_id).first()
    no_of_rooms = 0
    for each in Reservation.objects.filter(location_id=location.id).all():
        if datetimeObject(each.checkout) < checkin_date or datetimeObject(each.checkin) > checkout_date:
            no_of_rooms += each.rooms
    if no_of_rooms >= int(rooms_to_be_booked):
        return 1
    else:
        return 0
