import csv
import json
from get_details import get_details
from get_uni import get_uni


# getting all the details
data = []
def get_data():

    num_of_entries = int(input("Enter the number of entries:\n>>"))

    for i in range(num_of_entries):
        print(f"getting entry {i+1}...")
        details = get_details()
        details["University"], details["GPA"] = get_uni()

        data.append(details)

    field_names = details.keys()

    return field_names


# writing the details to csv file
def write_data_csv():
    field_names = get_data()
    print("writing entries...")
    with open("data.csv", "a") as entries:
        entry = csv.DictWriter(entries, fieldnames=field_names)
        entry.writeheader()

        for detail in data:
            entry.writerow(detail)
        

# writing the data to json file
def write_data_json():
    with open("data.json", "a") as entries:
        json.dump(data, entries, indent=2)


# writing the data to txt file
def write_data_txt():
    with open("data.txt", "a") as entries:
        for details in data:
            key = details.keys()
            value = details.values()

            for a, b in zip(key, value):
                entries.write(f"{a} = {b}\n")
            entries.write("\n\n\n\n")

write_data_csv()
write_data_json()
write_data_txt()