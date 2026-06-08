import allure
import pytest
import requests

from src.modules.verification.common_verification import *
from src.modules.wrapper.api_requests_wrapper import post_request
from src.endpoints.api_constants import APIConstants
from src.utils.utils import Utils
from src.modules.payload_manager.payload_manager import payload_create_booking, payload_create_token


@pytest.fixture
def setup():
    print("Step is started!")
    yield # No need to write separate teardown method
    print("End the Testcases") # When all the test cases are completed then this code will be executed.


# All the common codes which I want to execute here.


@pytest.fixture
def db_connection():
    print("Connect DB")
    yield "DB"
    print("Disconnect DB")


# @pytest.fixture
# def browser():
#     driver = launch_browser()
#     yield driver
#     driver.quit()


# create_token()
# booking_id()


def verify_json_key_for_not_null_token(param):
    pass


@pytest.fixture(scope="session")
def create_token():
    response = post_request(
        url=APIConstants().url_create_token(),
        headers=Utils().common_headers_json(),
        auth=None,
        payload=payload_create_token(),
        in_json=False
    )
    verify_http_status_code(response_data_status=response.status_code, expected_data=200)
    verify_json_key_for_not_null_token(response.json()["token"])
    return response.json()["token"]


@pytest.fixture(scope="session")
def get_booking_id():
    response = post_request(
        url=APIConstants().url_create_booking(),
        auth=None,
        headers=Utils().common_headers_json(),
        payload=payload_create_booking(),
        in_json=False

    )
    booking_id = response.json()["bookingid"]
    verify_http_status_code(response_data_status=response.status_code, expected_data=200)
    verify_json_key_for_not_null(booking_id)
    return booking_id
