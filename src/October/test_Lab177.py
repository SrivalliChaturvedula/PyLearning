import pytest
import allure
import requests

# from src.October.conftest import create_booking, create_token


class Test_request(object):
    def test_put_request(self, create_token, create_booking):
        base_url = "https://restful-booker.herokuapp.com"
        base_path = "/booking/" + str(create_booking)
        put_url = base_url + base_path
        cookie = "token=" + create_token
        headers = {
            "Content-Type": "application/json",
            "Cookie": cookie
        }
        json_payload = {
            "firstname": "Shaanu",
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

        assert data['firstname'] == "Shaanu"
        assert data['lastname'] == "Marti"

    def test_patch_request(self, create_token, create_booking):
        base_url = "https://restful-booker.herokuapp.com"
        base_path = "/booking/" + str(create_booking)
        put_url = base_url + base_path
        cookie = "token=" + create_token
        headers = {
            "Content-Type": "application/json",
            "Cookie": cookie
        }
        json_payload = {
            "firstname": "Divya",
            "lastname": "Mallina"
        }
        response = requests.patch(url=put_url, headers=headers, json=json_payload)
        assert response.status_code == 200
        data = response.json()
        print(data)

        assert data['firstname'] == "Divya"
        assert data['lastname'] == "Mallina"

