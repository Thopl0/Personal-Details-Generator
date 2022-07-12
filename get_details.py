import random
from req import get_html
from get_country import get_country


def get_details():
    titles = {}

    soup = get_html("https://fakenamecreator.com/?gender=random&locale=ne_NP")

    res = soup.find("body").find_all(class_="card-body")[3].find_all("p")
    
    employment = soup.find("body").find_all(class_="card-body")[3].find_all("h3")[2].next_sibling.next_sibling.next_sibling.next_sibling.text.split(":")

    for details in res:
        detail = details.find_all("span")
        try:
            titles[detail[0].text.strip()] = detail[1].text
        
        except IndexError:
            pass

    job = {}
    start_salary = random.randint(100000, 500000)
    job["Occupation"] = employment[1]
    job["Preferred Country to Work"] = get_country()
    job["Experience"] = f"Less than {random.randint(1, 5)} years in related work"
    job["Salary Range"] = f"${start_salary} - ${start_salary + 100000}"

    titles["Country of Residence"] = get_country()
    titles["Job"] = job

    del titles["Email"]

    return titles

if __name__ == "__main__":
    get_details()