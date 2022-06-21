from Probability_Distribution_of_X import factorial_equation as FE


def main_function():
    variable_dict = get_variables()
    x = variable_dict['x']
    k = variable_dict['k']
    p = variable_dict['p']
    q = variable_dict['q']
    probability = math(x, k, p, q)
    print_statement(x, k, p, probability)

def get_variables():
    variable_dict = {
        'x': int(input("Enter the value for x: ")),
        'p': float(input("Enter the probability, p: ")),
        'k': int(input("Enter the value for k: "))
    }

    variable_dict['q'] = 1 - variable_dict['p']

    return variable_dict

def math(x, k, p, q):
    first = FE((x - 1), (k - 1))
    second = p ** k
    third = q ** (x - k)

    return first * second * third

def print_statement(x, k, p, probability):
    print("b^*(" + str(x) + "; " + str(k) + ", " + str(p) + ") = " + str(round(probability, 4)))


main_function()