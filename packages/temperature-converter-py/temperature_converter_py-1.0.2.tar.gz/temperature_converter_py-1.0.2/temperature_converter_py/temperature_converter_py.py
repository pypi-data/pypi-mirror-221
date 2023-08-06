def celsius_to_fahrenheit(temp_in_celsius):
    """
    Converts temperature from Celsius to Fahrenheit.

    Args:
        temp_in_celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    """
    temp_in_fahrenheit = 1.8 * temp_in_celsius + 32
    return temp_in_fahrenheit


def fahrenheit_to_celsius(temp_in_fahrenheit):
    """
    Converts temperature from Fahrenheit to Celsius.

    Args:
        temp_in_fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.
    """
    temp_in_celsius = (temp_in_fahrenheit - 32) / 1.8
    return temp_in_celsius


def celsius_to_kelvin(temp_in_celsius):
    """
    Converts temperature from Celsius to Kelvin.

    Args:
        temp_in_celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Kelvin.
    """
    temp_in_kelvin = temp_in_celsius + 273.15
    return temp_in_kelvin


def kelvin_to_celsius(temp_in_kelvin):
    """
    Converts temperature from Kelvin to Celsius.

    Args:
        temp_in_kelvin (float): Temperature in Kelvin.

    Returns:
        float: Temperature in Celsius.
    """
    temp_in_celsius = temp_in_kelvin - 273.15
    return temp_in_celsius


def fahrenheit_to_kelvin(temp_in_fahrenheit):
    """
    Converts temperature from Fahrenheit to Kelvin.

    Args:
        temp_in_fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Kelvin.
    """
    temp_in_celsius = (temp_in_fahrenheit - 32) / 1.8
    temp_in_kelvin = celsius_to_kelvin(temp_in_celsius)
    return temp_in_kelvin


def kelvin_to_fahrenheit(temp_in_kelvin):
    """
    Converts temperature from Kelvin to Fahrenheit.

    Args:
        temp_in_kelvin (float): Temperature in Kelvin.

    Returns:
        float: Temperature in Fahrenheit.
    """
    temp_in_celsius = temp_in_kelvin - 273.15
    temp_in_fahrenheit = celsius_to_fahrenheit(temp_in_celsius)
    return temp_in_fahrenheit


# if __name__ == '__main__':
#     print('{} ºF'.format(celsius_to_fahrenheit(10)))
#     print('{} ºC'.format(fahrenheit_to_celsius(212)))
