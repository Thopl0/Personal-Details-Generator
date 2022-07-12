import json
from get_details import get_details
from get_edu import get_uni, get_deg


# getting all the details
data = {}
def get_data() -> None:
    num_of_entries = int(input("Enter the number of entries:\n>>"))

    for i in range(num_of_entries):
        print(f"getting entry {i+1}...")
        education ={}
        details = get_details()
        
        education["University"] = get_uni()
        education["Degree"], education["Degree Type"], education["From Year"], education["To Year"], education["GPA"] = get_deg()

        details["Education"] = education

        data[f"Person {i+1}"] = details


def write_data_json():
    get_data()
    with open("data.json", "a") as entries:
        json.dump(data, entries, indent=4)


write_data_json()