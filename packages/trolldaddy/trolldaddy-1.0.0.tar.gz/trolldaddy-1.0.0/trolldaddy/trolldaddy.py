import geocoder
import random
import math
from datetime import datetime
from pytz import timezone
import requests

def get_random_useless_fact():
    """
    Get a random useless fact.
    """
    useless_facts = [
        "The average person takes about 23,040 breaths per day.",
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
        "The shortest war in history was between Britain and Zanzibar in 1896. It lasted only 38 minutes.",
        "Ketchup was originally sold as medicine in the 1830s.",
        "The national animal of Scotland is the unicorn.",
        "The average person spends about six months of their life waiting for red lights to turn green.",
        "There are more possible iterations of a game of chess than there are atoms in the known universe.",
        "The word 'set' has the most definitions of any word in the English language.",
        "The top six foods that people are allergic to are milk, eggs, peanuts, tree nuts, soy, and wheat.",
        "Cows have best friends and can become stressed when separated from them.",
        "The oldest known sample of the smallpox virus was found in the teeth of a 17th-century child buried in Lithuania.",
        "The average person walks the equivalent of three times around the world in a lifetime.",
        "Hippopotomonstrosesquippedaliophobia is the fear of long words.",
        "A single strand of spaghetti is called a 'spaghetto.'",
        "Coca-Cola originally contained cocaine when it was first introduced in 1886.",
        "Humans share about 50% of their DNA with bananas.",
        "The average person spends about two weeks of their life kissing.",
        "Elephants can recognize themselves in mirrors, a trait shared only with humans, apes, and dolphins.",
        "The Hawaiian alphabet has only 13 letters.",
        "The average person blinks about 15-20 times per minute.",
    ]
    return random.choice(useless_facts)


def get_latitude_longitude():
    """
    Get the latitude and longitude of the current location.
    """
    g = geocoder.ip('me')
    if g.ok:
        return g.latlng
    else:
        return 'Error: Unable to retrieve latitude and longitude.'


def get_distance(latitude1, longitude1, latitude2, longitude2):
    """
    Calculate the distance between two sets of latitude and longitude coordinates using the Haversine formula.
    """
    # Convert degrees to radians
    lat1 = math.radians(latitude1)
    lon1 = math.radians(longitude1)
    lat2 = math.radians(latitude2)
    lon2 = math.radians(longitude2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = 6371 * c  # Radius of the Earth in kilometers

    return distance


def get_time_to_magnetic_north(walking_speed):
    """
    Get the estimated time to reach Magnetic North at an average walking speed.
    """
    latitude_longitude = get_latitude_longitude()
    if isinstance(latitude_longitude, list):
        latitude, longitude = latitude_longitude
        magnetic_north_latitude = 82.52  # Latitude of Magnetic North
        magnetic_north_longitude = -114.05  # Longitude of Magnetic North

        distance = get_distance(latitude, longitude, magnetic_north_latitude, magnetic_north_longitude)
        average_walking_speed_kph = walking_speed  # Average walking speed in kilometers per hour

        estimated_time = distance / average_walking_speed_kph
        hours = int(estimated_time)
        minutes = int((estimated_time - hours) * 60)

        return f"Estimated time to reach Magnetic North at an average walking speed of {walking_speed} km/h: {hours} hours {minutes} minutes"
    else:
        return latitude_longitude


def get_time_at_south_pole():
    """
    Get the current time at the South Pole.
    """
    south_pole_timezone = timezone('Antarctica/South_Pole')
    current_time = datetime.now(south_pole_timezone)
    time_format = "%Y-%m-%d %H:%M:%S %Z%z"
    return current_time.strftime(time_format)


def get_opposite_weather():
    """
    Get the current weather at the exact opposite side of the globe from the PC's position.
    """
    latitude_longitude = get_latitude_longitude()
    if isinstance(latitude_longitude, list):
        latitude, longitude = latitude_longitude
        opposite_latitude = -latitude
        if longitude < 0:
            opposite_longitude = longitude + 180
        else:
            opposite_longitude = longitude - 180

        url = f"https://api.meteomatics.com/now?lat={opposite_latitude}&lon={opposite_longitude}&model=mix"
        response = requests.get(url)

        if response.status_code == 200:
            weather_data = response.json()
            weather_info = weather_data['data']['time'][0]['parameter']

            temperature = weather_info['air_temperature_2m']['value']
            humidity = weather_info['relative_humidity_2m']['value']
            wind_speed = weather_info['wind_speed_10m']['value']

            return {
                'temperature': temperature,
                'humidity': humidity,
                'wind_speed': wind_speed
            }
        else:
            return 'Error: Unable to retrieve weather information.'
    else:
        return latitude_longitude