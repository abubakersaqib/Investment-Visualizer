# Import standard Python functions needed to support this module.
from random import randint, choice, seed, shuffle
from turtle import textinput
from re import sub

# A global variable used to ensure that the student doesn't call
# function "data_set" or "raw_data" in their code
already_called = False

#
#--------------------------------------------------------------------#



#-----Test Cases-----------------------------------------------------#
#
# Developing code when the underlying data set changes randomly can
# be difficult.  To help you develop your code you can temporarily
# provide the call to the data generation function at the bottom of
# the assignment template file with a "seed" value which will force
# it to produce a known data set.  Of course, having completed your
# solution, your program must work for any list that can be returned
# by calling the data generation function with no argument.
#
# You can use also enter seed values or test numbers by activating
# the "pop-up tester" below.  The markers will use this facility to
# test your solution efficiently.
#

# Test no. / Seed / Description, including the total result for the
# full year
test_cases = [
    # Some typical data sets (complete sets of reports and data fits within grid)
    [0, 17868, "A good year with no negative reports (Total: 17)"],
    [-1, 96218, "A very ordinary year, mainly average reports (Total: 0)"],
    [-2, 44303, "Good start to the year but a downturn at the end (Total: 9)"],
    [-3, 64211, "Year starts and ends even but otherwise is good (Total: 16)"],
    [-4, 54270, "A very volatile year with a slightly negative outcome (Total: -1)"],
    [-5, 61168, "Good start to the year but major downturn in August (Total: -2)"],
    [-6, 72785, "A very poor year, but average at the end (Total: -17)"],
    [-7, 42800, "Year starts and ends badly, but good results in third quarter (Total: -8)"],
    [-8, 50181, "A generally bad year, with a big upturn at Christmas (Total: -12)"],
    [-9, 60354, "Year starts well but goes bad in May (Total: -15)"],
    # Data sets that go outside the grid
    [-10, 99962, "A very good year with July off the chart (Total: 22)"],
    [-11, 50478, "Results off the top of the chart starting in May (Total: 40)"],
    [-12, 41924, "Results go outside bottom of the chart starting in August (Total: -47)"],
    [-13, 85360, "Results go outside bottom of the chart starting in May (Total: -48)"],
    [-14, 30377, "All good news and off the chart in April (Total: 29)"],
    [-15, 38318, "Nothing but bad news! (Total: -68)"],
    [-16, 50790, "All good news! (Total: 45)"],
    # Data sets with missing reports
    [-17, 92737, "A good year but no report received for July (Total: 7)"],
    [-18, 50867, "No reports received for June and November (Total: 13)"],
    [-19, 99628, "A volatile year with no report for January (Total: 4)"],
    [-20, 91962, "No reports for February or March (Total: -2)"],
    [-21, 15593, "Four reports missing: June, Aug, Sept & Nov! (Total: 8)"],
    # Data sets with missing reports and results outside the grid
    [-22, 66738, "No report for January and May-July off top of chart (Total: 27)"],
    [-23, 55364, "No report in May and December off the bottom of the chart (Total: -3)"]
    ]
test_cases2 = [
    # Balanced data sets with a mix of positive, zero, and negative reports
    [-24, 81238, "A balanced year with ups and downs (Total: 0)"],
    [-25, 32458, "A year with a steady rise and fall, ending even (Total: 0)"],
    [-26, 94827, "A year starting badly, improving later (Total: 5)"],
    
    # Data sets with extreme outliers
    [-27, 78623, "A year with one month's result significantly higher (Total: 30)"],
    [-28, 48930, "A year with an extreme low point in the middle (Total: -25)"],
    
    # Data sets with frequent negative reports
    [-29, 67342, "A challenging year with many setbacks (Total: -20)"],
    [-30, 56547, "A tough year with a few bright spots (Total: -10)"],
    
    # Data sets with all reports being positive
    [-31, 23478, "An outstanding year with all positive results (Total: 36)"],
    
    # Data sets with constant results
    [-32, 67891, "A consistent year with no changes (Total: 0)"],
    
    # Data sets with alternating results
    [-33, 12435, "A year of alternating good and bad results (Total: 0)"],
    
    # Data sets with a gradual improvement
    [-34, 11121, "A year starting poorly, but gradually improving (Total: 15)"],
    
    # Data sets with a gradual decline
    [-35, 22232, "A year starting strong, but gradually declining (Total: -15)"],
    
    # Data sets with missing reports spread throughout the year
    [-36, 33343, "An unpredictable year with several missing reports (Total: 5)"],
    [-37, 44454, "A year with significant data gaps (Total: -5)"],
    
    # Additional mixed data sets
    [-38, 55565, "A mixed year with a strong finish (Total: 10)"],
    [-39, 66676, "A mixed year with a weak finish (Total: -10)"],
    [-40, 77787, "An unpredictable year with a very strong start and end (Total: 20)"],
    [-41, 88898, "A year of two halves, starting poorly but recovering well (Total: 15)"]
]


# For markers (or interested students): Set the following constant
# to True to enable the pop-up seed/test no. prompt.  Positive
# values entered are interpreted as seeds for the random number
# generator.  Zero or negative numbers are interpreted as one of the
# test cases listed above.  Any other values entered are ignored and
# a random seed is used instead.
pop_up_tester = True
           
#
#--------------------------------------------------------------------#



# Define the months of the year when reports are made
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

def raw_data(given_seed):

    # Confirm that this is the first time functions "data_set" or
    # "raw_data" have been called, otherwise abort the program
    global already_called
    assert not already_called, "Program attempts to create a second data set - Aborting!"
    already_called = True

    # Decide which seed to use
    if pop_up_tester:
        # Get the seed number from the user
        markers_choice = textinput('Seed or test case selection',
                                   'Enter seed or test case number')
        try:
            number_entered = int(markers_choice)
            if number_entered > 0:
                # Use the number entered as the seed
                chosen_seed = number_entered
                description = 'Manually-entered seed'
            else:
                # Get the seed from the list of test cases
                chosen_seed = test_cases[abs(number_entered)][1]
                description = test_cases[abs(number_entered)][2]
        except:
            # User's input is not a number or is not in the
            # range of test cases, so ignore it
            print('Invalid seed or test number ignored ...\n')
            chosen_seed = given_seed
            description = 'Randomly-chosen seed'            
    else:
        # Use the argument given to raw_data
        chosen_seed = given_seed
        description = 'Argument to function data_set'
    # Set the random number seed and inform the user
    print(f'Using seed {chosen_seed}\n({description}) ...\n')
    seed(chosen_seed)

    # Define an initial value (which could be interpreted as that
    # for December in the previous year) biased towards the middle
    # of the range
    current_level = choice([-2, -1, -1, -1,
                            0, 0, 0, 0, 0, 0,
                            1, 1, 1, 1, 2])
    # Initialise the data set
    reports = []

    # Create the monthly reports
    for month in months:
        # Choose which way to change the level, biased towards
        # staying about the same
        change = choice([-2, -1, -1, -1, -1,
                         0, 0, 0, 0, 0, 0, 0,
                         1, 1, 1, 1, 2])
        # Update the current level
        current_level = current_level + change
        # Sometimes reports get lost in the mail (about
        # once every three years on average)
        missing = (randint(1, 36) == 1)
        # Add this month's report to the data set (provided it
        # wasn't lost)
        if not missing:
            reports.append([month, current_level])
    # Unfortunately the reports arrive in an unpredictable order
    shuffle(reports)

    # Print the whole data set to the shell window, laid out
    # one month per line
    print("The monthly reports to be visualised are:\n")
    print(str(reports).replace(' [', '\n [') + '\n')
    # Return the data set to the caller
    return reports

#
#--------------------------------------------------------------------#

