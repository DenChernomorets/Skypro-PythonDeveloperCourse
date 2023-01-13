import pytest
from homework_6.validators import check_pin, check_name, check_mail, check_pass
from homework_6.tests.test_data import *


@pytest.mark.parametrize('pin_code, expected_result', get_test_data_pins_evil())
def test_check_pin_evil(pin_code, expected_result):
    """
    Tests with expected result False for validators.check_pin
    """
    assert check_pin(pin_code) == expected_result


@pytest.mark.parametrize('pin_code, expected_result', get_test_data_pins_good())
def test_check_pin_good(pin_code, expected_result):
    """
    Tests with expected result True for validators.check_pin
    """
    assert check_pin(pin_code) == expected_result


@pytest.mark.parametrize('mail, expected_result', get_test_data_mails_good())
def test_check_mail_good(mail, expected_result):
    """
    Tests with expected result True for validators.check_mail
    """
    assert check_mail(mail) == expected_result


@pytest.mark.parametrize('mail, expected_result', get_test_data_mails_evil())
def test_check_mail_evil(mail, expected_result):
    """
    Tests with expected result False for validators.check_mail
    """
    assert check_mail(mail) == expected_result


@pytest.mark.parametrize('name, expected_result', get_test_data_names_evil())
def test_check_name_evil(name, expected_result):
    """
    Tests with expected result False for validators.check_name
    """
    assert check_name(name) == expected_result


@pytest.mark.parametrize('name, expected_result', get_test_data_names_good())
def test_check_name_evil(name, expected_result):
    """
    Tests with expected result True for validators.check_name
    """
    assert check_name(name) == expected_result


@pytest.mark.parametrize('password, expected_result', get_test_data_passwords_evil())
def test_check_pass_evil(password, expected_result):
    """
    Tests with expected result False for validators.check_name
    """
    assert check_pass(password) == expected_result


@pytest.mark.parametrize('password, expected_result', get_test_data_passwords_good())
def test_check_pass_good(password, expected_result):
    """
    Tests with expected result True for validators.check_name
    """
    assert check_pass(password) == expected_result
