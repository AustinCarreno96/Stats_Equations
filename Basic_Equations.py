import math

class Basic_Equations:


    def find_frequency(self, data_set, data_df):
        for point in data_set:
            if 1.5 < point < 1.9:
                data_df.frequency[0] += 1
            elif 2.0 < point < 2.4:
                data_df.frequency[1] += 1
            elif 2.5 < point < 2.9:
                data_df.frequency[2] += 1
            elif 3.0 < point < 3.4:
                data_df.frequency[3] += 1
            elif 3.5 < point < 3.9:
                data_df.frequency[4] += 1
        row_count = data_df.count()[0]

        for index in range(row_count):
            data_df.relative_freq[index] = float(data_df.frequency[index] / len(data_set))

    # Finding the sample_mean
    def find_sample_mean(self, data_set):
        sum = 0.0
        for point in data_set:
            sum += point

        sample_mean = sum / float(len(data_set))
        return sample_mean

    def find_median(self, data_set):
        data_set.sort()
        print(data_set)
        median = 0.0

        if len(data_set) % 2 != 0:
            median = data_set[(len(data_set) + 1) / 2]
        else:
            median = 0.5 * (data_set[int(len(data_set) / 2) - 1] + data_set[int((len(data_set) / 2) + 1) - 1])
        return median

    def find_trimmed_mean(self, data_set):
        choice = input("Do we need to find the trimmed mean?: ")
        if choice == 'yes':
            percent = input("What % should be trimmed? ")
            percent = float(percent) / 100
            number_of_points_to_knock_off = int(float(percent) * len(data_set))
            count = 0

            while count < number_of_points_to_knock_off:
                data_set.remove(data_set[0])
                data_set.remove(data_set[len(data_set) - 1])
                count += 1

            return self.find_sample_mean(self, data_set)

        else:
            return

    def find_sample_variance(self, data_set):
        numerator = 0
        mean = self.find_sample_mean(self, data_set)

        for point in data_set:
            numerator += (point - mean) ** 2
        sample_variance = numerator / (len(data_set) - 1)

        return sample_variance

    def find_standard_derivation(self, sample_variance):
        return math.sqrt(sample_variance)

    def find_sample_range(self, data_set):
        return data_set[len(data_set) - 1] - data_set[0]


