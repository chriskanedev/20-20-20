def convert_minutes_seconds(value, convert_to):
    value = int(value)
    if convert_to == "minutes":
        new_value = value / 60
    elif convert_to == "seconds":
        new_value = value * 60
    else:
        print("An error occurred: You have not specified whether to convert to minutes or seconds. Please check arguments.")
        new_value = None

    return new_value

