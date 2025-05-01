# Scraping ShadowFox website for courses links
import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.shadowfox.in")

soup = BeautifulSoup(page.text, "html.parser")

# Extracting the courses
# Course cards
courses_cards = soup.find_all("div", class_="service-col")


# Course titles
course_titles = courses_cards.find_all("h3").text

# Course Image Links
course_image_links = courses_cards.find_all("img")["src"]

# Course Image Alts
course_image_alts = courses_cards.find_all("img")["alt"]

# Course Descriptions
course_descriptions = courses_cards.find_all("p").text

# Course Links
course_links = courses_cards.find_all("a")["href"]

# Creating a dictionary to store the course details
course_dict = {}

# Adding the course details to the dictionary
for index, course in enumerate(courses_cards):
    course_dict[index] = {
        "title": course_titles[index],
        "image_link": course_image_links[index],
        "image_alt": course_image_alts[index],
        "description": course_descriptions[index],
        "link": course_links[index]
    }

# Printing the dictionary
print(course_dict)




