from cabin.models.location import Location
from cabin.models.reservation import Reservation


def CalculateAvailability(location_id, rooms_to_be_booked):
    location = Location.objects.filter(id=location_id).first()
    no_of_rooms = 0
    for each in Reservation.objects.filter(location_id=location.id).all():
        no_of_rooms += each.rooms
    if location.rooms - no_of_rooms >= int(rooms_to_be_booked):
        return 1
    else:
        return 0
