from req import get_html

def get_country():
    soup = get_html("https://randommer.io/random-countries")

    country = soup.find("body").find(class_="text-sm-center").text

    return country

if __name__ == "__main__":
    for i in range(100):
        print(get_country())