import logging
import os

from behave import *
import eikon as eik
from eikon.eikonError import EikonError


@step("the daemon is running")
def is_daemon_running(context):
    # TO ADD : mock an http server to simulate that the daemon is running
    pass


@step("the daemon is not running")
def daemon_is_not_running(context):
    pass


APP_KEY = os.environ.get("DESKTOP_APP_KEY")


@step("application ID is set with a valid EPAID")
def set_a_valid_EPAID(context):
    eik.set_app_key(APP_KEY)


@step("application ID is set with an invalid EPAID")
def set_an_invalid_EPAID(context):
    eik.set_app_key("INVALID EPAID")


@step("application key is not set")
def EPAID_not_set(context):
    eik.set_app_key("")


@step("I send JSON request")
def send_a_JSON_request(context):
    payload = (
        '{ "Analysis": [ "OHLCV"], '
        '"EndDate": "2015-10-01T10:00:00","StartDate": "2015-09-01T10:00:00", "Tickers": [ "EUR="]}'
    )
    try:
        context.response = eik.send_json_request("TATimeSeries", payload)
    except EikonError as eik_error:
        context.exception = eik_error


@step("a successful response is received")
def successful_response_received(context):
    assert context.exception is None, f"An Exception was raised: {context.exception}"
    if context.exception is not None:
        assert context.response != "", "Response is empty"


@step('an exception EikonError is raised with text: "{expected_exception_message}"')
def exception_raised(context, expected_exception_message):
    assert (
        context.exception is not None
    ), "No exception raised, but the exception expected."
    assert isinstance(
        context.exception, EikonError
    ), f"Invalid exception type received: {type(context.exception)}"
    assert expected_exception_message in context.exception.message, (
        f"Invalid exception message received: {context.exception.message}, "
        f"expected message: {expected_exception_message}"
    )
