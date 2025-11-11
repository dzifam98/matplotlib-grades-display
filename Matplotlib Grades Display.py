#This program displays class details out of values you input.
#There are 7 classes: math, history, physics, chemistry, recreation, english.
#There are 3 ways to put in grade information: file input, manual input, random list
import random as rand
import statistics as stats
import matplotlib.pyplot as plt
import numpy as np
def student_count():
    try:
        amount = int(input("How many students? "))
        return amount
    except ValueError:
        print("Not an integer. Please try again.")
        j = student_count()
        #recursive functions have saved my sanity ;w;
        return j
    
    
    
def choose_random():
    choice = input("Would you like a random list? ")
    if choice.lower() == "yes" or choice.lower() == "y":
        # this is what you do if there's a random list
        digits_lower = int(input("Choose your lowest value possibility. "))
        digits_higher = int(input("Choose your highest value possibility. "))
        listy = [rand.randrange(digits_lower, digits_higher) for i in range(amount)]
        print("Successfully inserted.")
        #makes a random list of "j" number of students
        return listy
    elif choice.lower() == "no" or choice.lower() == "n":
        manuals = input("Manual or File Input? (m/f) ")
        if manuals.lower() == "manual" or manuals.lower() == "m":
            listy = []
            for i in range(amount):
                a = int(input("Enter a grade. "))
                listy.append(a)
                print(f"Successfully inserted. {i+1} value(s) complete.")
            return listy
        elif manuals.lower() == "file input" or manuals.lower() == "f":
            to_open = input("What is your file name? (case sensitive) ")
            try:
                with open(to_open, "r") as file:
                    l = file.read()
                    string_list = l.strip().split()
                    listy = []
                    for i in string_list:
                        listy.append(int(i))
                        
                    print(listy)
                    if len(listy) == amount:
                        print("Successfully inserted.")
                        return listy
                    else:
                        print("Invalid amount. Please revise your file.")
                        m = choose_random()
                        return m
            except FileNotFoundError:
                print("File not found!")
                m = choose_random()
                return m        
        else:
            print("Invalid value.")
            m = choose_random()
            return m
    else:
        print("Invalid value.")
        m = choose_random()
        return m

def show_stats(group):
    maxes = {}
    mins = {}
    averages = {}
    medians = {}
    stdevs = {}
    for listj in group:
        maxes[str(listj)] = max(listj)
        mins[str(listj)] = min(listj)
        averages[str(listj)] = stats.mean(listj)
        medians[str(listj)] = stats.median(listj)
        stdevs[str(listj)] = stats.stdev(listj)
    print(f'Maxes: {list(maxes.values())}')
    #dict.values() will clean up the clutter of the original list, which will reprint all of the data in the class lists
    print(f'Mins: {list(mins.values())}')
    print(f'Averages/Means: {list(averages.values())}')
    print(f'Medians: {list(medians.values())}')
    print(f'Standard Deviations: {list(stdevs.values())}')
        
def boxplot(stat):
    #The following code is from the Matplotlib website but I have tweaked it to work for me
    fig, ax = plt.subplots()
    VP = ax.boxplot(stat, positions=[0,2,4,6,8,10], widths=1.5, patch_artist=True,
            #There are 6 positions to match the 6 classes in the "stat" parameter.
                showmeans=False, showfliers=False,
                medianprops={"color": "white", "linewidth": 0.5},
                boxprops={"facecolor": "C0", "edgecolor": "white",
                          "linewidth": 0.5},
                whiskerprops={"color": "C0", "linewidth": 1.5},
                capprops={"color": "C0", "linewidth": 1.5})

    plt.show()
    
    
def histogram(stat):
    #This is also from the Matplotlib website
    x = np.array(stat)
    
    plt.style.use('_mpl-gallery')
    fig, ax = plt.subplots()

    ax.hist(x, bins=6, linewidth=1.5, color="green")
    #One can add more or less bins to the graph, but a lower number like 6 is adequate.

    plt.show()

if __name__ == "__main__":
    amount = student_count()
    print("##############################################")
    math = choose_random()
    print(f"Math grades: {math}")
    print("**********")
    
    history = choose_random()
    print(f"History grades: {history}")
    print("**********")
    
    physics = choose_random()
    print(f"Physics grades: {physics}")
    print("**********")
    
    chem = choose_random()
    print(f"Chemistry grades: {chem}")
    print("**********")
    
    rec = choose_random()
    print(f"Recreation grades: {rec}")
    print("**********")
    
    english = choose_random()
    print(f"English grades: {english}")
    
    print("##############################################")
    
    classes = []
    
    show_stats(classes)
    
    print("##############################################")
    
    boxplot(classes)
    
    histogram(math)