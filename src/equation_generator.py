import random
import math


def generate_three_values():
    a, b ,c = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
    return a, b, c 

def calculate_discriminant(a, b, c):
    discriminant = b**2 - 4*a*c
    return discriminant

def get_user_response(a, b, c):
    while True:
        try:
            user_input = input(f"Trouve le discriminant de {a}x^2 + {b}x + {c} ? ")
            user_response = int(user_input)
            return user_response
        except ValueError:
            print("Erreur : veuillez saisir un nombre entier.")

def send_response(user_response,discriminant):
    if user_response == discriminant:
        print('bonne réponse')
    else:
        print(f'mauvaise réponse, la bonne réponse était {discriminant}')


def generate_equation(case):
    while True:
        a,b,c = generate_three_values()
        discriminant = calculate_discriminant(a, b, c)
        if case(discriminant):
            user_response = get_user_response(a, b, c)
            send_response(user_response,discriminant)
            break

