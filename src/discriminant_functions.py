import math 


def positive_squared_discriminant(discriminant):
    return discriminant > 0 and math.isqrt(discriminant) ** 2 == discriminant

def positive_not_squared_discriminant(discriminant):
    return   0 < discriminant < 100 and math.isqrt(discriminant) ** 2 != discriminant

def negative_discriminant(discriminant):
    return discriminant < 0