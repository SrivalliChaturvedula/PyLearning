import pytest


@pytest.fixture()
def create_token():
    return "abc"


@pytest.fixture()
def create_booking_id():
    return 1


@pytest.fixture()
def read_excel_file():
    return ("xyz")


def test_consume(create_token, create_booking_id, read_excel_file):
    print(create_token)
    print(create_booking_id)
    print(read_excel_file)


def test_update_req_1(create_token, create_booking_id):
    print("create token ---->", create_token)
    print("Booking id --->", create_booking_id)


def test_update_req_2(create_token, create_booking_id):
    print("create token ---->", create_token)
    print("Booking id --->", create_booking_id)
