import math
from fractions import Fraction as fract

import Basic_Equations
import Probability
import Factorial_Math

data_set = [3.78, 2.71, 2.84, 2.83, 3.01, 1.87,
            2.44, 3.21, 2.54, 2.13, 2.68, 2.68,
            2.77, 2.71, 3.54, 3.84, 3.24, 2.05,
            2.90, 2.78, 3.12, 2.54, 2.11, 3.64,
            3.25, 3.70, 2.4, 2.71, 3.61, 3.30]

# This will solve simple equations in stats for me by taking an array of numbers and applying simple math.
def main():
    basic_eq = Basic_Equations.Basic_Equations
    prob = Probability.Probability
    factorial_math = Factorial_Math
    user_choice = input("Pick The Type of Problem Needed To Be Solved:"
                        "\n1. Mean/Median/Trimmed Mean/Standard Deviation/Sample Variance"
                        "\n2. Factorial Math"
                        "\nChoice: ")

    match user_choice:
        case "1": basic_equations(basic_eq, data_set)
        case "2": factorial_equations(factorial_math)
        case "3": prob.place_holder(prob)



    # create_histogram(data_set)
def basic_equations(basic_eq, data_set):
    sample_mean = basic_eq.find_sample_mean(basic_eq, data_set)
    sample_variance = basic_eq.find_sample_variance(basic_eq,data_set)
    standard_derivation = basic_eq.find_standard_derivation(basic_eq, sample_variance)
    median = basic_eq.find_median(basic_eq, data_set)
    sample_range = basic_eq.find_sample_range(basic_eq, data_set)
    trimmed_mean = basic_eq.find_trimmed_mean(basic_eq, data_set)

    if trimmed_mean == 0:
        print("\nThe Sample Mean is: " + str(round(sample_mean, 3)) +
              "\nThe Median is: " + str(round(median, 3)) +
              "\nThe Sample Range is: " + str(round(sample_range, 3)) +
              "\nThe Sample Variance is: " + str(round(sample_variance, 4)) +
              "\nThe Standard Derivation is: " + str(round(standard_derivation, 4)))
    else:
        print("\nThe Sample Mean is: " + str(round(sample_mean, 3)) +
              "\nThe Median is: " + str(round(median, 3)) +
              "\nThe Sample Range is: " + str(sample_range) +
              "\nThe Trimmed Mean is: " + str(round(trimmed_mean, 3)) +
              "\nThe Sample Variance is: " + str(round(sample_variance, 4)) +
              "\nThe Standard Derivation is: " + str(round(standard_derivation, 4)))

def factorial_equations(factorial_math):
    factorial_math.factorial_math_class.factorial_math(factorial_math.factorial_math_class)
# def factorial_math():
#     first_multiplier_list = []
#     second_multiplier_list = []
#     denominator_list = []
#     index = 0
#
#     full_amount = input("Type how many items are there: ")
#     denominator_list.append(int(full_amount))
#
#     amount_faulty = input("Type how many items are faulty: ")
#     denominator_list.append(int(amount_faulty))
#
#     amount_purchased = input("Type how many were purchased: ")
#     first_multiplier_list.append(int(amount_purchased))
#
#     not_sold = int(full_amount) - int(amount_purchased)
#     second_multiplier_list.append(not_sold)
#
#     while index <= int(amount_faulty):
#         first_multiplier_list.append(index)
#         second_multiplier_list.append(int(amount_faulty) - index)
#
#         first_multiplier = factorial_equation(first_multiplier_list)
#         second_multiplier = factorial_equation(second_multiplier_list)
#
#         numerator = first_multiplier * second_multiplier
#         denominator = factorial_equation(denominator_list)
#
#         first_multiplier_list.remove(first_multiplier_list[1])
#         second_multiplier_list.remove(second_multiplier_list[1])
#         print("f(" + str(index) + "): " + str(fract(int(numerator), int(denominator))))
#         index += 1
#
#
#
#
# def factorial_equation(list):
#     numerator = math.factorial(int(list[0]))
#     denominator = math.factorial(int(list[1])) * math.factorial(int(list[0]) - int(list[1]))
#     return numerator / denominator
main()
