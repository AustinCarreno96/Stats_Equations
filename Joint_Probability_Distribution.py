import Probability_Distribution_of_X
import pandas
from fractions import Fraction

def joint_prob_distribution():
    first_multiplier_list = []
    second_multiplier_list = []
    third_multiplier_list = []
    denominator_list = []
    x_index = 0
    y_index = 0
    print('apples, oranges, bananas')
    X = input("Which fruit is the X: ")
    Y = input("Which fruit is the Y: ")
    data_frame = pandas.DataFrame(columns=['0', '1', '2', '3', '4'], index=['0', '1', '2', '3', '4'])

    amount_of_a = input("How many apples are there: ")
    first_multiplier_list.append(int(amount_of_a))

    amount_of_b = input("How many bananas are there: ")
    second_multiplier_list.append(int(amount_of_b))

    amount_of_o = input("How many oranges are there: ")
    third_multiplier_list.append(int(amount_of_o))

    sample_fruit = input("How many sample fruit are there: ")
    denominator_list.append(int(amount_of_a) + int(amount_of_b) + int(amount_of_o))
    denominator_list.append(int(sample_fruit))

    X = X_and_Y_match_stmt(X, amount_of_a, amount_of_b, amount_of_o)
    Y = X_and_Y_match_stmt(Y, amount_of_a, amount_of_b, amount_of_o)

    for x_index in range(int(sample_fruit) + 1):
        first_multiplier_list.append(x_index)
        for y_index in range(int(sample_fruit) + 1):
            if (x_index + y_index + int(amount_of_o)) < int(sample_fruit):
                data_frame.loc[data_frame.index == str(y_index), str(x_index)] = 0
            elif x_index > int(X):
                data_frame.loc[data_frame.index == str(y_index), str(x_index)] = 0
            elif y_index > int(Y):
                data_frame.loc[data_frame.index == str(y_index), str(x_index)] = 0

            else:
                if int(sample_fruit) - x_index - y_index < 0:
                    data_frame.loc[data_frame.index == str(y_index), str(x_index)] = 0
                else:
                    # first_multiplier_list.append(x_index)
                    second_multiplier_list.append(y_index)


                    third_multiplier_list.append((int(sample_fruit) - x_index) - y_index)

                    first_multiplier = Probability_Distribution_of_X.factorial_equation(first_multiplier_list[0], first_multiplier_list[1])
                    second_multiplier = Probability_Distribution_of_X.factorial_equation(second_multiplier_list[0], second_multiplier_list[1])
                    third_multiplier = Probability_Distribution_of_X.factorial_equation(third_multiplier_list[0], third_multiplier_list)

                    denominator = Probability_Distribution_of_X.factorial_equation(denominator_list[0], denominator_list[1])
                    numerator = first_multiplier * second_multiplier * third_multiplier

                    data_frame.loc[data_frame.index == str(y_index),str(x_index)]=Fraction(int(numerator),int(denominator))

                    second_multiplier_list.remove(second_multiplier_list[1])
                    third_multiplier_list.remove(third_multiplier_list[1])
        first_multiplier_list.remove(first_multiplier_list[1])
    print("\n")
    print(data_frame)


def X_and_Y_match_stmt(variable, amount_of_a, amount_of_b, amount_of_o):
    match variable:
        case 'apples': variable = amount_of_a
        case 'bananas': variable = amount_of_b
        case 'oranges': variable = amount_of_o

    return variable
