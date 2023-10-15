"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    aux = EXPECTED_BAKE_TIME - elapsed_bake_time
    return aux



def preparation_time_in_minutes(number_of_layers):
    """
        Calculate the time to prepere the Lasagna layers
        :param number_of_layers : INT
        :return : INT
    """
    return number_of_layers*2



def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
        Calculetes te TOTAL time elapsed - Preparation + bake time
        : param number_of_layers - INT
        : param elapsed_bake_time - INT
        : return  - INT
    """
    return preparation_time_in_minutes(number_of_layers)+elapsed_bake_time