# API Request - HTTP Request

import allure
import pytest
import requests


@allure.title("TC#1- Create Booking CRUD Positive")
@allure.description("TC#1 - Verify create booking")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    # To make request: URL, method - POST, Headers, Body, Auth(NO)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    url = base_url + base_path
    headers = {"Content-type": "Application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url, headers=headers, json=payload)
    # status code
    assert response.status_code == 200

    responseData = response.json()

    # Response body verification
    booking_id = responseData["bookingid"]
    assert booking_id is not None
    assert booking_id > 0
    assert type(booking_id) == int

    firstname = responseData["booking"]["firstname"]
    lastname = responseData["booking"]["lastname"]
    totalprice = responseData["booking"]["totalprice"]
    depositpaid = responseData["booking"]["depositpaid"]

    assert firstname == "Jim"
    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == True

    checkin = responseData["booking"]["bookingdates"]["checkin"]
    checkout = responseData["booking"]["bookingdates"]["checkout"]

    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"

@allure.title("TC#2- Create Booking CRUD Negative")
@allure.description("TC#2 - Verify create booking")
@pytest.mark.crud
def test_create_booking_negative_tc2():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    url = base_url + base_path
    headers = {"Content-type": "Application/json"}
    json_payload = {}
    response = requests.post(url, headers=headers, json=json_payload)
    assert response.status_code == 500



@allure.title("TC#3- Create Booking CRUD Negative")
@allure.description("TC#3 - Verify create booking by giving negative totalprice")
@pytest.mark.crud
def test_create_booking_negative_tc3(): # bug status code is wrong
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    url = base_url + base_path
    headers = {"Content-type": "Application/json"}
    json_payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": -111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url, headers=headers, json=json_payload)
    assert response.status_code == 200


