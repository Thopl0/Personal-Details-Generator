from req import get_html
import random


def get_uni():
    uni_list = ['University of Southern California', 'North Carolina State University', 'Stevens Institute of Technology', 'University of Chicago', 'New Mexico State University', 'Wake Forest University', 'University of Utah', 'Binghamton University, State University of New York', 'Oakland University', 'University of Cincinnati', 'Oakland University', 'Florida International University', 'Kansas State University', 'University of California, Irvine', 'University of Iowa', 'University of Oregon', 'University of Southern California', 'University of Alabama', 'University of Arizona', 'New York University', 'Indiana University', 'University of Texas at El Paso', 'University of South Carolina', 'Columbia University', 'University of Illinois at Chicago', 'Binghamton University, State University of New York', 'Florida Institute of Technology', 'Colorado State University', 'Johns Hopkins University']
    soup = get_html("https://www.bestrandoms.com/random-college")

    try:
        uni_name = soup.find("body").find(class_="content").span.text

    except AttributeError:
        uni_name = random.choice(uni_list)

    return uni_name

def get_deg():
    with open("course_list.txt", "r") as f:
        courses = f.readlines()

    course_list = [course.replace("\n", "") for course in courses]

    degree_type = random.choice(["Bachelors", "Masters"])

    from_year = random.randint(2014, 2021)

    if from_year > 2019:
        to_year = f"Current{from_year+4}"

    else:
        to_year = from_year + random.randint(3, 5)

    gpa = round(random.uniform(2.50, 4.00), 2)

    return random.choice(course_list), degree_type, from_year, to_year, gpa


if __name__ == "__main__":
    get_edu()

if __name__ == "__main__":
    for i in range(10):
        print(get_uni())