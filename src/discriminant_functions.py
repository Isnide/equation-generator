import math 


def find_positive_squared_discriminant(discriminant):
    return discriminant > 0 and math.isqrt(discriminant) ** 2 == discriminant

def find_positive_not_squared_discriminant(discriminant):
    return   0 < discriminant < 100 and math.isqrt(discriminant) ** 2 != discriminant

def find_negative_discriminant(discriminant):
    return discriminant < 0