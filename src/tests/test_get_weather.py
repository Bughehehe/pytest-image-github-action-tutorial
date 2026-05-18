import pytest_tutorial.main as main

def test_get_weather():
    assert main.get_weather(28) == 'hot', "temp is higher than 20 deg celc"
    assert main.get_weather(10) == 'cold', "temp is lower than 20 deg celc"