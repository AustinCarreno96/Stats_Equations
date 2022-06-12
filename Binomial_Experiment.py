import Probability_Distribution_of_X as PDoX
from Basic_Equations import convert_string_to_float as CSTF

def main():
    variable_list = grab_variables()

    n = variable_list[0]
    x_list = variable_list[3]
    p = variable_list[1]
    q = variable_list[2]

    b = binomial_distribution(n, x_list, p, q)

    for x_value in x_list:
        print("P(X = " + str(x_value) + ") = " + str(round(b[int(x_value)], 3)))

    print("\nP(X <= " + str(len(x_list) - 1) + ") = " + str(round(sum(b), 3)))
    print("μ = " + str(find_mean_of_binomial_distribution(n, p)))
    print("σ^2 = " + str(find_variance_fo_binomial_distribution(n, p, q)))


def grab_variables():
    x_list = []

    variable_list = input("Enter in the numeric values for each variable (n, p): ").split()
    highest_x = input("What is the highest value of x: ")

    # Getting all values of x where X >= highest_x
    for index_1 in range(int(highest_x) + 1):
        x_list.append(float(index_1))

    # Turning string values to float
    variable_list = CSTF(variable_list)

    variable_list.append(1.0 - variable_list[len(variable_list) - 1])
    variable_list.append(x_list)
    return variable_list

def binomial_distribution(n, x_list, p, q):
    b_list = []

    for x_value in x_list:
        b = 1
        x = x_value
        for index in range(4 - 1):
            match index:
                case 0: temp = PDoX.factorial_equation(n, x)
                case 1: temp = p ** x
                case 2: temp = q ** (n - x)
            b *= temp
        b_list.append(b)
    return b_list

def find_mean_of_binomial_distribution(n, p):
    return round(n * p, 2)

def find_variance_fo_binomial_distribution(n, p, q):
    return round(n * p * q, 2)


main()