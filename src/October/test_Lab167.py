# Create booking

import pytest
import allure
import requests

@allure.title("Test GET Request - Restful Booker Project-#1")
@allure.description("TC#1 -> Verify that GET request with ID works")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Srivalli Chaturvedula")
@allure.testcase("TC#1")


@pytest.mark.smoke
def test_get_single_request_by_id_positive():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url)
    assert response_data.status_code == 200

@allure.title("Test GET Request - Restful Booker Project-#1")
@allure.description("TC#2 -> Verify that GET request with Negative ID number")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Srivalli Chaturvedula")
@allure.testcase("TC#2")


@pytest.mark.smoke
def test_get_single_request_by_id_negative_number():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url)
    assert response_data.status_code == 404


@allure.title("Test GET Request - Restful Booker Project-#1")
@allure.description("TC#3 -> Verify that GET request with Invalid id")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Srivalli Chaturvedula")
@allure.testcase("TC#3")


@pytest.mark.smoke
def test_get_single_request_by_id_negative_data():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    response_data = requests.get(url)
    assert response_data.status_code == 404


@allure.title("Test GET Request - Restful Booker Project-#1")
@allure.description("TC#4 -> Verify that GET request with zero id")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Srivalli Chaturvedula")
@allure.testcase("TC#4")


@pytest.mark.smoke
def test_get_single_request_by_id_negative_zero():
    url = "https://restful-booker.herokuapp.com/booking/0"
    response_data = requests.get(url)
    assert response_data.status_code == 404


@allure.title("Test GET Request - Restful Booker Project-#1")
@allure.description("TC#5 -> Verify that GET request with larger number as id")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Srivalli Chaturvedula")
@allure.testcase("TC#5")


@pytest.mark.smoke
def test_get_single_request_by_id_negative_large_number():
    url = "https://restful-booker.herokuapp.com/booking/123456789"
    response_data = requests.get(url)
    assert response_data.status_code == 404


