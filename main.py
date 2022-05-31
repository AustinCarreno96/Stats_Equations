import Basic_Equations
import Probability
import Factorial_Math


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
        case "1":
            basic_equations(basic_eq)
        case "2": factorial_equations(factorial_math)
        case "3": prob.place_holder(prob)



    # create_histogram(data_set)
def basic_equations(basic_eq):
    data_set = input("Enter the points in the data set: ").split()
    data_set = [float(point) for point in data_set]

    sample_mean = basic_eq.find_sample_mean(basic_eq, data_set)
    sample_variance = basic_eq.find_sample_variance(basic_eq, data_set)
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


main()
