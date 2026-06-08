import allure
import pytest
from src.modules.wrapper.api_requests_wrapper import post_request
from src.endpoints.api_constants import APIConstants
from src.utils.utils import Utils
from src.modules.payload_manager.payload_manager import payload_create_booking
from src.modules.verfication.common_verification import *
import logging


class TestPUTBooking:

    @pytest.mark.positive
    @allure.title("Verify that the existing booking ID with existing token update is happening")
    @allure.description("")
    def test_verify_existing_booking_update_put(self):
        bookingId = 1
        token = "ox232m3m23kl"
        pass

    @pytest.mark.negative
    @allure.title("Verify that if you try to update without the token, you get an error.")
    @allure.description("")
    def test_verify_existing_booking_update_put_without_auth(self):
        bookingId = 1
        tokne = "ox232m3m23kl"
        pass
