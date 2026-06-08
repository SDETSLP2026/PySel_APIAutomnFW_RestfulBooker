# Common verification
# HTTP Status Code
# Headers
# Data Verification
# JSON Schema

# As we are verifying actual vs expected, we need to assert the statements.

def verify_http_status_code(response_data_status, expected_data):
    assert response_data_status == expected_data, "Status code mismatch."


def verify_response_key(key, expected_data):
    assert key == expected_data, "Response key mismatch."


def verify_json_key_for_not_null(key):
    assert key != 0, "Failed. The key is not empty." + key
    assert key > 0, "Failed. The key is greater than zero."


def verify_json_key_for_null_token(key):
    assert key != 0, "Failed. The key is not empty." + key


def verify_response_delete(response):
    assert "Created" in response
