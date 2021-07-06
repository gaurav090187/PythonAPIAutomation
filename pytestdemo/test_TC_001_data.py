import pytest


@pytest.mark.smoke
def test_tc_registration_valid_data():
    print('Registration with valid data')


@pytest.mark.sanity
def test_tc_registration_invalid_data():
    print('Registration with invalid data')


@pytest.mark.smoke
def test_tc_invalid_data():
    print('Invalid data')