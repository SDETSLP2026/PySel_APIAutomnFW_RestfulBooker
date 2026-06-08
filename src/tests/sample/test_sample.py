import pytest
import allure

@allure.title("To verify that the framework is working. Pass ✅")
@allure.step("Step - 1")
def test_sample_pass():
    assert True == True

@allure.title("To verify that the framework is not working. Failed ❌")
@allure.step("Step - 2")
def test_sample_fail():
    assert True == False