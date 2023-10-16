def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <=0:
        raise ValueError("Classification is only possible for positive integers.")
    divisor = []
    for x in range(1, int(number/2)+1):
        if number % x == 0:
            divisor.append(x)
    
    if sum(divisor) == number:
        return "perfect"
    if sum(divisor) < number:
        return "deficient"
    return "abundant"
