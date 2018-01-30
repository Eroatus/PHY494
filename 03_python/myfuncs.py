# Heasiside Step Function

def heaviside(x):
    """Heaviside Step Function"""

    theta = None
    if x < 0:
        theta = 0.
    elif x == 0:
        theta = 0.5
    else:
        theta = 1.

    return theta

# Temperature Conversion Functions

def convert_FtoK(temp_Fahrenheit):
    """Temperature Conversion from Fahrenheit to Kelvin"""

    temp_Kelvin = (5/9) * (temp_Fahrenheit - 32) + 273.15

    return temp_Kelvin

def convert_KtoC(temp_Kelvin):
    """Temperature Conversion from Kelvin to Celsius"""

    temp_Celsius = temp_Kelvin - 273.15

    return temp_Celsius
