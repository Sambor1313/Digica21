data = {
    "Tokyo": {
        "weather": ["sunny", "cloudy"],
        "roads": "dry"},
    "Dakar":
        {"weather": ["foggy", "windy"],
         "roads": "sandy"},
    "Warsaw":
        {"weather": ["windy", "sunny"],
         "roads": "dry"},
    "New York":
        {"weather": ["rainy"],
         "roads": "wet"}
}


def main():
    weather_list = {}
    for city in data:
        for weather in data[city].get('weather'):
            weather_list.setdefault(weather, []).append(city)

    print(weather_list)


if __name__ == "__main__":
    main()
