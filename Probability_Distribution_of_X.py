import math
from fractions import Fraction as fract

def probability_distribution_of_X():
    first_multiplier_list = []
    second_multiplier_list = []
    denominator_list = []
    index = 0

    full_amount = input("Type how many items are there: ")
    denominator_list.append(int(full_amount))

    amount_faulty = input("Type how many items are faulty: ")
    denominator_list.append(int(amount_faulty))

    amount_purchased = input("Type how many were purchased: ")
    first_multiplier_list.append(int(amount_purchased))

    not_sold = int(full_amount) - int(amount_purchased)
    second_multiplier_list.append(not_sold)

    while index <= int(amount_faulty):
        first_multiplier_list.append(index)
        second_multiplier_list.append(int(amount_faulty) - index)

        first_multiplier = factorial_equation(first_multiplier_list[0], first_multiplier_list[1])
        second_multiplier = factorial_equation(second_multiplier_list[0], second_multiplier_list[1])

        numerator = first_multiplier * second_multiplier
        denominator = factorial_equation(denominator_list[0], denominator_list[1])

        first_multiplier_list.remove(first_multiplier_list[1])
        second_multiplier_list.remove(second_multiplier_list[1])
        print("f(" + str(index) + "): " + str(fract(int(numerator), int(denominator))))
        index += 1

def factorial_equation(top_number, bottom_number):
    numerator = math.factorial(int(top_number))
    denominator = math.factorial(int(bottom_number)) * math.factorial(int(top_number) - int(bottom_number))
    return numerator / denominator