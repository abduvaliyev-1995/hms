import datetime
from hotel.models import Room, Booking


def check_availability(room, check_in, check_out):
    avail_list = []
    booking_list = Booking.objects.filter(room=room)
    for booking in booking_list:
        if booking.check_in > check_out or booking.check_out < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    print(avail_list)
    return all(avail_list)


# bunda booking vaqtiga to'g'ri kelib qolmasligini shartda tekshirilmoqda
# all() funksiyada listning barcha elementlari true bo'lsa true qaytaradi