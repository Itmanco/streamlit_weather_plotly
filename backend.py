import requests

def get_data(city_name, forecast_days = None, kind = None):
    API_KEY = "141710af2113bab9f55ef73e1bcd33d5"


    url = "http://api.openweathermap.org/data/2.5/forecast?" \
          f"q={city_name}&" \
          f"appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8*forecast_days
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    elif kind == "Sky":
        filtered_data = [dict["weather"][0]["id"] for dict in filtered_data]

    return filtered_data


if __name__ == "__main__":
    print(get_data("Tokyo"))