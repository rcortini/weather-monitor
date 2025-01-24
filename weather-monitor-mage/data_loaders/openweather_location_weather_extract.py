import io
import os
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    openweather_api_url = 'https://api.openweathermap.org/data/2.5/weather'
    lat = kwargs['lat']
    lon = kwargs['lon']
    OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
    url = f'{openweather_api_url}?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}'
    
    # print(url)
    response = requests.get(url)
    return response.json()


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
