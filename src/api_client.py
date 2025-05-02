import requests


def get_location(ip):
    url = f"https://freeipapi.com/api/json/{ip}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    # import ipdb

    # ipdb.set_trace()
    return {
        "ip": data["ipAddress"],
        "country": data["countryName"],
        "city": data["cityName"],
        "region": data["regionName"],
        "latitude": data["latitude"],
        "longitude": data["longitude"],
        "timezone": data["timeZone"],
    }


if __name__ == "__main__":
    print(get_location("8.8.8.8"))
