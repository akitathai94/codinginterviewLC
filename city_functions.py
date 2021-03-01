def getCityCountry(city, country, population=''):
    city = city.title()
    country = country.title()
    if population:
        full_string = f"{city}, {country} - population {population}"
    else:
        full_string = f"{city}, {country}"
    return full_string