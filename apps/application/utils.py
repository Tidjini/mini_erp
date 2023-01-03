def meter_to_km(distance):
    km = distance // 1000
    m = distance % 1000
    return (km, m)


def seconds_to_days(seconds):

    minutes = seconds // 60
    hours = minutes // 60
    minutes = minutes % 60
    days = hours // 24
    hours = hours % 24

    return (days, hours, minutes)


def seconds_to_hours(seconds):
    minutes = seconds // 60
    hours = minutes // 60
    minutes = minutes % 60

    return (hours, minutes)
