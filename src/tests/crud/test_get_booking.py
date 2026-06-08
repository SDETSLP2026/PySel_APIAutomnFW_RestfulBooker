import allure
import pytest
import requests

from src.modules.wrapper.api_requests_wrapper import post_request
from src.endpoints.api_constants import APIConstants
from src.utils.utils import Utils
from src.modules.payload_manager.payload_manager import payload_create_booking
from src.modules.verification.common_verification import *
import logging


class TestGETBooking:

    @pytest.mark.positive
    @allure.title(
        "Verify that the existing booking, which is booking number 1, exists and it gave you status code 200.")
    @allure.description("")
    def test_verify_existing_booking_bid_01(self):
        pass

    @pytest.mark.negative
    @allure.title("")
    @allure.description("Verify that the booking ID does not exist and it will give you an error.")
    def test_verify_invalid_booking_not_exist(self):
        pass
