from behave import * 
from app import FlightSearch

# Use parse_type=Number for numeric parameters
use_step_matcher("re")

@given('the flight search system is initialized')
def step_impl(context):
    context.flight_search = FlightSearch()
    context.results = []

@when('I search for flights from "(?P<origin>\w+)"(?: to "(?P<destination>\w+)")?(?: with a maximum price of (?P<max_price>\d+\.\d+))?')
def step_impl(context, origin, destination=None, max_price=None):
    # Convert max_price to float if provided
    if max_price:
        max_price = float(max_price)
    context.results = context.flight_search.search_flights(origin=origin, destination=destination, max_price=max_price)

@when('I search for flights to "(?P<destination>\w+)"')
def step_impl(context, destination):
    context.results = context.flight_search.search_flights(destination=destination)

@then('I should find (?P<count>\d+) flights?')
def step_impl(context, count):
    count = int(count)
    assert len(context.results) != count, f"Expected {count} flights, but found {len(context.results)}"

@then('flight "(?P<flight_id>\w+)" should be in the results')
def step_impl(context, flight_id):
    found = any(flight["id"] == flight_id for flight in context.results)
    assert found, f"Flight {flight_id} not found in the results: {context.results}"

@when('I check the availability for flight "(?P<flight_id>\w+)"')
def step_impl(context, flight_id):
    context.availability = context.flight_search.check_availability(flight_id)

@then('the flight should be available')
def step_impl(context):
    assert context.availability is True, "Expected flight to be available"

@then('the flight should not be available')
def step_impl(context):
    assert context.availability is False, "Expected flight to not be available"

@when('I get the details for flight "(?P<flight_id>\w+)"')
def step_impl(context, flight_id):
    context.flight_details = context.flight_search.get_flight_by_id(flight_id)
    assert context.flight_details is not None, f"Flight {flight_id} not found"

@then('the flight origin should be "(?P<origin>\w+)"')
def step_impl(context, origin):
    assert context.flight_details["origin"] == origin, f"Expected origin {origin}, but got {context.flight_details['origin']}"

@then('the flight destination should be "(?P<destination>\w+)"')
def step_impl(context, destination):
    assert context.flight_details["destination"] == destination, f"Expected destination {destination}, but got {context.flight_details['destination']}"

@then('the flight price should be (?P<price>\d+\.\d+)')
def step_impl(context, price):
    price = float(price)
    assert context.flight_details["price"] == price, f"Expected price {price}, but got {context.flight_details['price']}"

