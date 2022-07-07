from req import get_html

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

    
    titles["Job"] = employment[1]
    del titles["Email"]

    return titles

if __name__ == "__main__":
    get_details()