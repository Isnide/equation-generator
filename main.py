from src.equation_generator import generate_equation
from src.discriminant_functions import find_positive_squared_discriminant, find_positive_not_squared_discriminant, find_negative_discriminant


def main():
    generate_equation(find_positive_squared_discriminant)
    generate_equation(find_positive_not_squared_discriminant)
    generate_equation(find_negative_discriminant)

if __name__ == "__main__":
    main()