travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country_visited, visits_visited, cities_visited):
    new_country = {"country": country_visited, "visits": visits_visited, "cities": cities_visited}
    return travel_log.append(new_country)


add_new_country("Rassia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
