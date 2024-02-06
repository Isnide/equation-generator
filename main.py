from src.equation_generator import generate_equation
from src.discriminant_functions import positive_squared_discriminant, positive_not_squared_discriminant, negative_discriminant


def main():
    generate_equation(positive_squared_discriminant)
    generate_equation(positive_not_squared_discriminant)
    generate_equation(negative_discriminant)

if __name__ == "__main__":
    main()