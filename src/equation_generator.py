import random
import math


     

def generate_equation(exercice):
    while True:
        try:
            a, b, c = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
            discriminant = b**2 - 4*a*c
            if exercice(discriminant):
                user_response = int(input(f"Trouve le discriminant de {a}x^2 + {b}x + {c} ? "))
                if user_response == discriminant:
                    print("Bonne réponse")
                else :
                    print(f"Mauvaise réponse, le discriminant de l'équation est {discriminant}")
                return a, b, c
        except ValueError:
            print("Erreur : veuillez saisir un nombre entier.")



