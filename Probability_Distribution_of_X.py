import math
from fractions import Fraction as fract

# class probability_distribution_class:
#     def probability_distribution_of_X(self):
#         first_multiplier_list = []
#         second_multiplier_list = []
#         denominator_list = []
#         index = 0
#
#         full_amount = input("Type how many items are there: ")
#         denominator_list.append(int(full_amount))
#
#         amount_faulty = input("Type how many items are faulty: ")
#         denominator_list.append(int(amount_faulty))
#
#         amount_purchased = input("Type how many were purchased: ")
#         first_multiplier_list.append(int(amount_purchased))
#
#         not_sold = int(full_amount) - int(amount_purchased)
#         second_multiplier_list.append(not_sold)
#
#         while index <= int(amount_faulty):
#             first_multiplier_list.append(index)
#             second_multiplier_list.append(int(amount_faulty) - index)
#
#             first_multiplier = self.factorial_equation(self, first_multiplier_list)
#             second_multiplier = self.factorial_equation(self, second_multiplier_list)
#
#             numerator = first_multiplier * second_multiplier
#             denominator = self.factorial_equation(self, denominator_list)
#
#             first_multiplier_list.remove(first_multiplier_list[1])
#             second_multiplier_list.remove(second_multiplier_list[1])
#             print("f(" + str(index) + "): " + str(fract(int(numerator), int(denominator))))
#             index += 1
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

        first_multiplier = factorial_equation(first_multiplier_list)
        second_multiplier = factorial_equation(second_multiplier_list)

        numerator = first_multiplier * second_multiplier
        denominator = factorial_equation(denominator_list)

        first_multiplier_list.remove(first_multiplier_list[1])
        second_multiplier_list.remove(second_multiplier_list[1])
        print("f(" + str(index) + "): " + str(fract(int(numerator), int(denominator))))
        index += 1

    # def factorial_equation(self, list):
    #     numerator = math.factorial(int(list[0]))
    #     denominator = math.factorial(int(list[1])) * math.factorial(int(list[0]) - int(list[1]))
    #     return numerator / denominator

def factorial_equation(list):
    numerator = math.factorial(int(list[0]))
    denominator = math.factorial(int(list[1])) * math.factorial(int(list[0]) - int(list[1]))
    return numerator / denominator