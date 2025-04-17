# Simulation of  rolling a sixsided die multiple times (at least 20 times)
# and printing the results in a table format.
import random
# import pandas as pd
# import seaborn as sns
# import numpy as np
# import matplotlib.pyplot as plt

# random.seed(42)
# result = []

# for _ in range(20):
#     value = random.randint(1, 6)
#     result.append(value)


    
# df = pd.DataFrame(result, columns=["Die Value"])
# count = df["Die Value"].value_counts().sort_index()

# sns.barplot(x=count.index, y=count.values)

# plt.title("Die Roll Simulation")
# plt.xlabel("Die Value")
# plt.ylabel("Count")

# plt.show()

# count_6 = 0
# count_1 = 0
# double_count_6 = 0
# prev_roll = None

# for _ in range(20):
#     roll = random.randint(1, 6)
    
#     if roll == 6:
#         count_6 += 1
#     if roll == 1:
#         count_1 += 1
#     if roll == 6 and prev_roll == 6:
#         double_count_6 += 1
#     prev_roll = roll
    
# print(f"Statistics of the die rolls:")
# print(f"Count of 6: {count_6}")
# print(f"Count of 1: {count_1}")
# print(f"Count of double 6: {double_count_6}")


# Workout routine (completion of 100 jumping jacks.)
import time
print("You are to perform 100 jumping Jacks but you have to perform 10 jumps at a time")

for i in range(1,101):
    print(f"You are jumping jack {i}")
    time.sleep(1)
    if i == 100:
        print("Congratulations! You completed the workout!!!")
        break
    if i % 10 == 0:
        tired_value = input("Are you tired?\n").lower().strip()
        
        if tired_value == "yes" or tired_value == "y":
            skip_steps = input("Do you want to skip the remaining steps?.").lower().strip()
            
            if skip_steps == "yes" or tired_value == "y":
                print(f"You completed a total of {i} jumping jacks")
                break
            else:
                print("Success is not for the weak!!!. Continue jumping!.")
        elif tired_value == "no" or tired_value == "n":
            print(f"Push harder!!!. {100 - i} jumping jacks remaining.")
            


