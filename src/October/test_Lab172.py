import allure
import pytest
import requests


def test_update_req_1(create_token, create_booking):
    print(create_token)
    print(create_booking)
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(create_booking)
    put_url = base_url + base_path
    cookie = "token=" + create_token
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    json_payload = {
        "firstname": "Shanvitha",
        "lastname": "Marti",
        "totalprice": 403,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(url=put_url, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["firstname"] == "Shanvitha"
    assert data["lastname"] == "Marti"
