# Reading CSV Files:

# reader --> Lets you iterate over rows of the CSV as lists
# DictReader --> Lets you iterate over rows of the CSV as OrderedDicts

#Tradional Method:
with open("C:/Users/Javed/PycharmProjects/pythonProject/pythonProject/CSV/fighters.csv") as file:
    data = file.read()
    print(data)

#Using Reader :
from csv import reader
with open("C:/Users/Javed/PycharmProjects/pythonProject/pythonProject/CSV/fighters.csv") as file:
    # Other Delimiters :
    # Readers accept a delimiter kwarg in case your data isnt separated by commas.
    csv_reader = reader(file, delimiter = ",")
    next(csv_reader)  #Dont want the headers.
    # print(csv_reader)   # prints csv_reader object -->   <_csv.reader object at 0x000001E0E77FC760>
    for fighter in csv_reader:   # each row in a list
        # print(fighter)
        print(f"{fighter[0]} is from {fighter[1]}")  # Any Header Data : Ex --> 'Name' cannot be accessed using Name Keyword, we have to use index as shown. This is the limitation of this.

#Using DictReader :
from csv import DictReader
with open("C:/Users/Javed/PycharmProjects/pythonProject/pythonProject/CSV/fighters.csv") as file:
    # Other Delimiters :
    # Readers accept a delimiter kwarg in case your data isnt separated by commas.
    csv_reader = DictReader(file, delimiter = ",")
    for fighter in csv_reader:  # each row is an OrderedDict!
        # print(fighter)
        name = fighter['Name']
        print(f"name : {name}")
        country = fighter['Country']
        print(f"country : {country}")
        height_in_cm = fighter['Height (in cm)']
        print(f"height_in_cm : {height_in_cm}")

# Write to a File:
from csv import writer
with open("cats.csv", "w") as file:  #Will create a new file if file does not exists.
    csv_writer = writer(file)
    csv_writer.writerow(["Name", "Age"])
    csv_writer.writerow(["Blue", 3])
    csv_writer.writerow(["Kitty", 2])
    csv_writer.writerow(["Tuffy", 1])

#Ignore below method of writing using writer: [Only for Reference]
from csv import reader , writer
with open ("C:/Users/Javed/PycharmProjects/pythonProject/pythonProject/CSV/fighters.csv") as file:
    csv_reader = reader(file)  #data never gets converted to list.
    with open("Screaming_Fighters.csv", "w") as file:
        csv_writer = writer(file)
        for fighter in csv_reader:
            csv_writer.writerow([s.upper() for s in fighter])

# Write to a file using DictWriter:
from csv import DictWriter
with open("cats_data.csv", "w") as file:
    headers = ["Name", "Breed", "Age"]
    csv_writer = DictWriter(file, fieldnames = headers)
    csv_writer.writeheader()  #This will write the header using fieldnames
    csv_writer.writerow({
        "Name" : "Garfield",
        "Breed" : "Orange Tabby",
        "Age" : 10
    })
#cm to inch conversion
def cm_to_inch(cm):
    return float(cm) * 0.393701

from csv import DictReader, DictWriter
with open("C:/Users/Javed/PycharmProjects/pythonProject/pythonProject/CSV/fighters.csv") as file:
    csv_reader = DictReader(file)
    fighters = list(csv_reader)  #V.V.V.V.IMP Step --> Always convert to list before writing files, otherwise will get an I/O Error if looped through csv_reader

with open("inches_fighters.csv", "w") as file:
    headers = ["Name", "Country", "Height"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for f in fighters:
        csv_writer.writerow({
            "Name" : f["Name"],
            "Country" : f["Country"],
            "Height" : cm_to_inch(f["Height (in cm)"])  #def cm_to_inch(cm):
        })


