# API Constants - A class which contains all the endpoints
# -----------------------------------------------------------------------------------
# RestfulBooker - List of all the endpoints
# HealthCheck_Ping - https://restful-booker.herokuapp.com/ping
# Auth_Create Token - https://restful-booker.herokuapp.com/auth
# Booking_GetAllBookings - https://restful-booker.herokuapp.com/booking
# Booking_GetSingleBooking - https://restful-booker.herokuapp.com/booking/:id (BookingID is required)
# Booking_CreateBooking - https://restful-booker.herokuapp.com/booking
# Booking_UpdateBooking - https://restful-booker.herokuapp.com/booking/:id (BookingID is required)
# Booking_PartialUpdateBooking - https://restful-booker.herokuapp.com/booking/:id (BookingID is required)
# Booking_DeleteBooking - https://restful-booker.herokuapp.com/booking/:id (BookingID is required)
# -----------------------------------------------------------------------------------

class APIConstants:

    # Create a function which will create an application's base URL
    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def url_healthcheck(self):
        return "https://restful-booker.herokuapp.com/ping"

    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_patch_put_delete(self, booking_id):
        return "https://restful-booker.herokuapp.com/booking" + str(booking_id)

