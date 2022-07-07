from req import get_html
import random


def get_uni():
    uni_list = ['University of Southern California', 'North Carolina State University', 'Stevens Institute of Technology', 'University of Chicago', 'New Mexico State University', 'Wake Forest University', 'University of Utah', 'Binghamton University, State University of New York', 'Oakland University', 'University of Cincinnati', 'Oakland University', 'Florida International University', 'Kansas State University', 'University of California, Irvine', 'University of Iowa', 'University of Oregon', 'University of Southern California', 'University of Alabama', 'University of Arizona', 'New York University', 'Indiana University', 'University of Texas at El Paso', 'University of South Carolina', 'Columbia University', 'University of Illinois at Chicago', 'Binghamton University, State University of New York', 'Florida Institute of Technology', 'Colorado State University', 'Johns Hopkins University']
    soup = get_html("https://www.bestrandoms.com/random-college")

    try:
        uni_name = soup.find("body").find(class_="content").span.text

    except AttributeError:
        uni_name = random.choice(uni_list)

    gpa = round(random.uniform(2.50, 4.00), 2)

    return uni_name, gpa

if __name__ == "__main__":
    for i in range(10):
        print(get_uni())