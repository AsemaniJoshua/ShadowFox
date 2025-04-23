import csv

# Defining the dictionary
my_dict = {}
# File Handling
with open("/home/pentest/Music/Frontend/ShadowFox/Beginners Task/Task 7/student_marks.csv", "r") as file:
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
        csv_dict["total"] = sum(map(int, row[3:11]))
        # Average
        csv_dict["average"] = csv_dict["total"] / 10
        my_dict.update({index: csv_dict})
        
        
# Printing the dictionary
print(my_dict)

# Writing my_dict to a new file
with open("New_Student_marks.csv", "w") as file:
    # converting my_dict to csv
    writer = csv.writer(file)
    # Writing the header
    writer.writerow(["Index", "Name", "Gender", "Date of Birth", "Maths", "Physics", "Chemistry", "English", "Biology", "Economics", "History", "Civics", "Total", "Average"])
    # Writing the data
    for index, row in my_dict.items():
        writer.writerow([index, row["name"], row["gender"], row["date_of_birth"], row["Maths"], row["Physics"], row["Chemistry"], row["English"], row["Biology"], row["Economics"], row["History"], row["Civics"], row["total"], row["average"]])
        
