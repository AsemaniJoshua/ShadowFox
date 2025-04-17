# Creating a list and a List of tuples of friends names and the length of their names.

# friends_names = ["Cant", "warr", "TJ", "Godw", "Edw"]
# tuple_list = []
# individual_tuple = ()

# for i in friends_names:
#     individual_tuple = (i, len(i))
#     tuple_list.append(individual_tuple)
    
# individual_tuple = ()

# # Printing the list of tuples.
# print(f"The list of tuples are below: \n{tuple_list}")


# Question 2
# Creating individual expenses for the 2 people.
your_expenses = {
"Hotel": 1200,
"Food": 800,
"Transportation": 500,
"Attractions": 300,
"Miscellaneous": 200
}

Second_expenses = {
"Hotel": 1000,
"Food": 900,
"Transportation": 600,
"Attractions": 400,
"Miscellaneous": 150
}

your_total_expenses = 0
second_total_expenses = 0

# Checking your total expense
for key, value in your_expenses.items():
    your_total_expenses += value
    
print(f"Your total expenses is: {your_total_expenses}")

# Checking second person total expense
for key, value in Second_expenses.items():
    second_total_expenses += value
    
print(f"The second person's total expenses is: {second_total_expenses}")

# Determining who spent more money
if your_total_expenses > second_total_expenses:
    print("You spent more money than the second person.")
elif your_total_expenses < second_total_expenses:
    print("The second person spent more money than you.")
else:
    print("Both of you guys spent equal money.")
    
    
# Finding out the expense category where there is a significant difference in spending between you and the second person.

max_diff = 0
max_diff_category = None

for category in your_expenses:
    diff = abs(your_expenses[category] - Second_expenses[category])
    
    if diff > max_diff:
        max_diff = diff
        max_diff_category = category
print(f"The category with the most significant difference in spending is: {max_diff_category} with a difference of {max_diff}.")
# Finding out the average spending for each category.
average_expenses = {}
for category in your_expenses:
    average_expenses[category] = (your_expenses[category] + Second_expenses[category]) / 2
print("The average spending for each category is:")
for category, average in average_expenses.items():
    print(f"{category}: {average}")
    
