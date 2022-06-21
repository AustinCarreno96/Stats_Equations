import math

def main_function():
    table = {'x_values': input("Enter the values of x (separate by space): ").split(),
             'f(x)': input("Enter the values of f(x) (separate by space): ").split()}
    table['x_values'] = [float(x) for x in table['x_values']]
    table['f(x)'] = [float(number) for number in table['f(x)']]

    E_of_X = finding_E_of_X_Squared(table)
    mew = finding_mew(table)
    SDofaRV = finding_SDoaRV(E_of_X, mew)

    print("The Standard Deviation of a Random Variable is: " + str(round(SDofaRV, 2)))

def finding_E_of_X_Squared(table):
    E_of_X = 0.0
    for index in range(len(table['x_values'])):
        E_of_X += (table['x_values'][index] ** 2) * table['f(x)'][index]
    return E_of_X


def finding_mew(table):
    mew = 0.0
    for index in range(len(table['x_values'])):
        mew += table['x_values'][index] * table['f(x)'][index]
    return mew


def finding_SDoaRV(E_of_X, mew):
    SDoaRV = 0.0
    SDoaRV = E_of_X - (mew ** 2)
    SDoaRV = math.sqrt(SDoaRV)
    return SDoaRV