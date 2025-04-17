import csv

# Defining the dictionary
my_dict = {}
# File Handling
with open("./student_marks.csv", "r") as file:
    csv_reader = csv.reader(file)
    
    # Skipping the header
    next(csv_reader, None)
    # Reading each row and adding it to the dictionary

    for index, row in enumerate(csv_reader):
        csv_dict = {}
        csv_dict["name"] = row[0]
        csv_dict["gender"] = row[1]
        csv_dict["date_of_birth"] = row[2]
        csv_dict["Maths"] = row[3]
        csv_dict["Physics"] = row[4]
        csv_dict["Chemistry"] = row[5]
        csv_dict["English"] = row[6]
        csv_dict["Biology"] = row[7]
        csv_dict["Economics"] = row[8]
        csv_dict["History"] = row[9]
        csv_dict["Civics"] = row[10]
        my_dict.update({index: csv_dict})
        
        
# Printing the dictionary
print(my_dict)
        