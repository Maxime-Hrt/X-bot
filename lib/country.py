import iso3166


def get_country_name(country_code):
    return iso3166.countries_by_alpha3[country_code].name


def get_country_code(country_name):
    return iso3166.countries_by_name[country_name.upper()].alpha2
