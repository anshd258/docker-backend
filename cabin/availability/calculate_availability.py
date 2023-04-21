from cabin.models.location import Location
from cabin.models.reservation import Reservation
from datetime import datetime
import pytz
def datetimeObject(it):
    print(it)
    return pytz.utc.localize(datetime.strptime(str(it),'%Y-%m-%d %H:%M:%S'))


def CalculateAvailability(location_id, rooms_to_be_booked, checkin, checkout):
    checkin_date = datetimeObject(checkin)
    checkout_date = datetimeObject(checkout)
    location = Location.objects.filter(id=location_id).first()
    no_of_rooms = 0
    for each in Reservation.objects.filter(location_id=location.id).all():
        a =(each.checkin)
        b =(each.checkout)
        print(a,b)
        if (a <= checkout_date <= b) or (a <= checkin_date <= b) or (checkin_date <= a and checkout_date >= b):
            no_of_rooms += each.rooms
    if location.rooms-no_of_rooms >= int(rooms_to_be_booked):
        return 1
    else:
        return 0
