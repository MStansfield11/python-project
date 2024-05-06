import requests
import textwrap

api_key = 'ddbb72c1853f934bbf1bc4304948d720'

user_input = input("Enter a city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.status_code == 200:
    weather = weather_data.json()['weather'][0]['main']
    temp = weather_data.json()['main']['temp']

    # Format weather and temperature
    weather_info = f"Weather: {weather}\nTemperature: {temp}°F"

    # Format into a 2x2 box
    box_width = 20
    formatted_box = '+' + '-' * (box_width - 2) + '+\n'
    lines = textwrap.wrap(weather_info, width=box_width - 4)
    for line in lines:
        formatted_box += '| ' + line.center(box_width - 4) + ' |\n'
    formatted_box += '+' + '-' * (box_width - 2) + '+'

    print(formatted_box)
else:
    print("City not found or API request failed.")
