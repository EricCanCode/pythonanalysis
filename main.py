""" This app allows the user to process several mathematical
functions on a csv file """

import csv
import os
import sys

import matplotlib.pyplot as plt
from pandas import read_csv

print('***************** Welcome to the Python Data Analysis App ********** ')
print('What type of data would you like to analyze')
while True:
    try:
        data_type = int(input('1. Population Data \n'
                              '2. Housing Data \n'
                              '3. Exit the Program \n'))


        def line_count(read):
            """This method counts the lines read in the csv file and displays the count"""
            count = str(read.line_num - 1)
            return 'Count equals: ' + count


        if data_type == 1:
            with open(os.path.join(sys.path[0] + '\\' + 'popchange.csv'), 'r') as pop_data:
                reader = csv.DictReader(pop_data)
                st = read_csv('popchange.csv')

                result_a = []
                result_b = []
                result_c = []

                for row in reader:
                    a = int(row['Pop Apr 1'])
                    b = int(row['Pop Jul 1'])
                    c = int(row['Change Pop'])

                    result_a.append(a)
                    result_b.append(b)
                    result_c.append(c)


            def process_pop(pop, title, bins, mean_std, min_max):
                """This method processes the population data and returns the
                count of items, mean, standard deviations, min, max and a histogram"""
                print(line_count(reader))
                print('Mean equals: ' + str(st.mean(axis=0)[mean_std]))
                print('Standard Deviation equals: ' + str(st.std(axis=0)[mean_std]))
                print('Min equals: ' + str(st.min(axis=0)[min_max]))
                print('Max equals: ' + str(st.max(axis=0)[min_max]))
                print('Here is a histogram of the data you selected')
                plt.hist(pop, bins=bins, edgecolor='black')
                plt.title(title)
                plt.xlabel('Population')
                plt.ylabel('Total number of properties April 1')
                return plt.show()


            print('You have entered Population Data.')
            column_select = input('Select which column you would like to analyze: \n'
                                  'A. Pop Apr 1 \n'
                                  'B. Pop Jul 1 \n'
                                  'C. Change Pop \n'
                                  'D. Exit Column \n')

            if not column_select:
                print('You entered an invalid entry, reenter your selection.')

            while column_select:
                if column_select.upper() == 'A':
                    a_pop = process_pop([result_a], 'April 1 Population',
                                        [10000, 30000, 50000, 70000, 90000,
                                         110000, 130000, 150000], 1, 4)
                    break

                if column_select.upper() == 'B':
                    b_pop = process_pop(result_b, 'July 1 Population',
                                        [10000, 30000, 50000, 70000, 90000,
                                         110000, 130000, 150000], 2, 5)
                    break

                if column_select.upper() == 'C':
                    c_pop = process_pop(result_c, 'Change in Population (April - July)',
                                        [-10500, -9000, -7500, -6000, -4500, -3000, -1500,
                                         0, 1500, 3000, 4500, 6000, 7500, 9000, 10500], 3, 6)
                    break

                if column_select.upper() == 'D':
                    input('Press any key to return to the main menu')
                    break

                print('You entered an invalid entry, reenter your selection.')
                break

        if data_type == 2:
            with open(os.path.join(sys.path[0] + '\\' + 'housing.csv'), 'r') as house_data:
                reader2 = csv.DictReader(house_data)
                sd = read_csv('housing.csv')

                result_f = []
                result_g = []
                result_h = []
                result_i = []
                result_j = []
                result_m = []
                result_n = []

                for row in reader2:
                    f = int(row['AGE'])
                    g = int(row['BEDRMS'])
                    h = int(row['BUILT'])
                    i = int(row['ROOMS'])
                    j = float(row['UTILITY'])
                    m = (row['NUNITS'])
                    n = (row['WEIGHT'])

                    result_f.append(f)
                    result_g.append(g)
                    result_h.append(h)
                    result_i.append(i)
                    result_j.append(j)
                    result_m.append(m)
                    result_n.append(n)


                    def process_house(house, ticks, xlabel, mean_std, min_max):
                        """This method processes the house data and returns the
                        count of items, mean, standard deviations, min, max and a histogram"""
                        print(line_count(reader2))
                        print('Mean equals: ' + str(sd.mean(axis=0)[mean_std]))
                        print('Standard Deviation equals: ' + str(sd.std(axis=0)[mean_std]))
                        print('Min equals: ' + str(sd.min(axis=0)[min_max]))
                        print('Max equals: ' + str(sd.max(axis=0)[min_max]))
                        print('Here is a histogram of the data you selected')
                        plt.hist(house, bins=ticks, edgecolor='black')
                        plt.ylabel('Number of Homes')
                        plt.xlabel(xlabel)
                        return plt.show()

            print('Here is the housing data')
            param_select = input('Select which housing parameter you would like to analyze: \n'
                                 'A. Age \n'
                                 'B. Bedrooms \n'
                                 'C. Built \n'
                                 'D. Rooms \n'
                                 'E. Utility \n'
                                 'F. Exit Column \n')

            if not param_select:
                print('You entered an invalid entry, reenter your selection.')

            while param_select:
                if param_select.upper() == 'A':
                    process_house(result_f,
                                  [-10, 0, 10, 20, 30, 40, 50, 60, 70], 'Age', 0, 0)
                    break

                if param_select.upper() == 'B':
                    process_house(result_g,
                                  [0, 1, 2, 3, 4, 5, 6, 7, 8], 'Bedrooms', 1, 1)
                    break

                if param_select.upper() == 'C':
                    process_house(result_h,
                                  [1919, 1929, 1939, 1949, 1959, 1969, 1979,
                                   1989, 1999, 2009, 2019], 'Year Built', 2, 2)
                    break

                if param_select.upper() == 'D':
                    process_house(result_i, [0, 3, 6, 9, 12, 15], 'Rooms', 4, 4)
                    break

                if param_select.upper() == 'E':
                    process_house(result_j, [0, 300, 600, 900, 1200, 1500], 'Utility', 6, 6)
                    break

                if param_select.upper() == 'F':
                    input('Press any key to return to the main menu')
                    break

                print('Invalid input, please reenter your selection')
                break

        if data_type == 3:
            print('Thank you for using the Python Data Analysis App')
            sys.exit()

    except ValueError:
        print('You entered an invalid entry, please select one of the listed options')
