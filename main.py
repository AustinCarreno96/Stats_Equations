import Basic_Equations
import Probability
import Probability_Distribution_of_X
import Joint_Probability_Distribution as JPD
import Standard_Deviation_of_a_Random_Variable as SRofaRV
import Set_Arithmetic as SA
import Binomial_Experiment as BE
import Multinomial_Experiment as ME
import Hypergeometric_Probability as HP


def main():
    basic_eq = Basic_Equations.Basic_Equations
    prob = Probability.Probability
    prob_dist_of_X = Probability_Distribution_of_X
    user_choice = input("Pick The Type of Problem Needed To Be Solved:"
                        "\n1. Mean/Median/Trimmed Mean/Standard Deviation/Sample Variance"
                        "\n2. Probability Distribution of X"
                        "\n3. Joint Probability Distribution"
                        "\n4. Standard Deviation of a Random Variable X"
                        "\n5. Set Arithmetic"
                        "\n6. Binomial Experiment"
                        "\n7. Multinomial Experiment"
                        "\n8. Hypergeometric Probability"
                        "\nChoice: ")

    match user_choice:
        case "1": basic_equations(basic_eq)
        case "2": factorial_equations(prob_dist_of_X)
        case "3": JPD.joint_prob_distribution()
        case "4": SRofaRV.main()
        case "5": SA.main()
        case "6": BE.main()
        case "7": ME.main()
        case "8": HP.main()


def print_statement_without_trimmed_mean(sample_mean, median, sample_range, sample_variance, standard_derivation):
    print("\nThe Sample Mean is: " + str(round(sample_mean, 3)) +
          "\nThe Median is: " + str(round(median, 3)) +
          "\nThe Sample Range is: " + str(round(sample_range, 3)) +
          "\nThe Sample Variance is: " + str(round(sample_variance, 4)) +
          "\nThe Standard Derivation is: " + str(round(standard_derivation, 4)))

def print_statement_with_trimmed_mean(sample_mean, median, sample_range,
                                      sample_variance, standard_derivation, trimmed_mean):
    print("\nThe Sample Mean is: " + str(round(sample_mean, 3)) +
          "\nThe Median is: " + str(round(median, 3)) +
          "\nThe Sample Range is: " + str(sample_range) +
          "\nThe Trimmed Mean is: " + str(round(trimmed_mean, 3)) +
          "\nThe Sample Variance is: " + str(round(sample_variance, 4)) +
          "\nThe Standard Derivation is: " + str(round(standard_derivation, 4)))

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
        print_statement_without_trimmed_mean(sample_mean, median, sample_range, sample_variance, standard_derivation)
    else:
        print_statement_with_trimmed_mean(sample_mean, median, sample_range,
                                          sample_variance, standard_derivation, trimmed_mean)

def factorial_equations(prob_dist_of_X):
    prob_dist_of_X.probability_distribution_of_X()


def placeholder():
    print("placeholder")
main()
