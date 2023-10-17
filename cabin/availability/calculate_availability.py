from cabin.models.property import Property
from cabin.models.payment_status import PaymentStatus
from cabin.models.reservation import Reservation
from datetime import datetime
import pytz

from cabin.models.room import Room
def datetimeObject(it):
    return pytz.utc.localize(datetime.strptime(str(it),'%Y-%m-%d %H:%M:%S.%f'))


def CalculateAvailability(location_id, rooms_to_be_booked, checkin, checkout):
    checkin_date = checkin
    checkout_date = checkout
    location = Property.objects.filter(id=location_id).first()
    no_of_rooms = 0
    res_list=Reservation.objects.filter(property=location.id).all()
    fin=[]
    for each in res_list:
        payments=PaymentStatus.objects.filter(reservation_id=each.id)
        for i in payments:
            print(i.status)
            if i.status==True:
                fin.append(each)
                break
    for each in fin:
        a =(each.checkin)
        b =(each.checkout)
        print(a,b)
        if (a <= checkout_date <= b) or (a <= checkin_date <= b) or (checkin_date <= a and checkout_date >= b):
            no_of_rooms += each.roomsbooked
    print(location.rooms)  
    if location.rooms-no_of_rooms >= int(rooms_to_be_booked):
        return 1
    else:
        return 0


def CalculateAvailability_fromRoom(roomid, rooms_to_be_booked, checkin, checkout):
    checkin_date = checkin
    checkout_date = checkout
    room = Room.objects.filter(id=roomid).first()
    no_of_rooms = 0
    res_list=Reservation.objects.filter(room=room).all()
    fin=[]
    for each in res_list:
        payments=PaymentStatus.objects.filter(reservation_id=each.id)
        for i in payments:
            print(i.status)
            if i.status==True:
                fin.append(each)
                break
    for each in fin:
        a =(each.checkin)
        b =(each.checkout)
        print(a,b)
        if (a <= checkout_date <= b) or (a <= checkin_date <= b) or (checkin_date <= a and checkout_date >= b):
            no_of_rooms += each.roomsbooked
    if room.available-no_of_rooms >= int(rooms_to_be_booked):
        return 1
    else:
        return 0