from bs4 import BeautifulSoup

with open("home.html", "r") as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, "lxml")
    tags = soup.find_all("h5")
    # print("tags: ", tags)

    courseSoup = soup.find_all("div", class_="card")
    for course in courseSoup:
        # print(course.h5) # type: ignore
        course_name = course.h5.text  # type: ignore
        course_price = course.a.text    # type: ignore 
        print(f"{course_name} costs {course_price}") # type: ignore