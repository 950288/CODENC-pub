# boos 直聘网爬虫
import time
import openpyxl
from selenium import webdriver
from bs4 import BeautifulSoup
import os

# Create a new workbook and sheet
workbook = openpyxl.Workbook()
sheet = workbook.active

# Add the column headings to the sheet
sheet.append(["Job Title", "Location", "Salary", "Experience", "Education","skills"])


page = 1
while True:
    # Open a web browser and navigate to the website
    driver = webdriver.Chrome()
    if page == 1:
        driver.get("https://www.zhipin.com/web/geek/job?query=python&city=101010100")
    else:
        driver.get("https://www.zhipin.com/web/geek/job?query=python&city=101010100&page="+str(page))
    page += 1

    time.sleep(10)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')


    # Find all the job listings on the page
    jobs = soup.find_all("li", {"class": "job-card-wrapper"})
    if len(jobs) == 0:
        driver.quit()
        break

    # Iterate over the job elements
    for job in jobs:
        # Extract the data from the job element
        title = job.find("span", {"class": "job-name"}).text
        location = job.find("span", {"class": "job-area"}).text
        salary = job.find("span", {"class": "salary"}).text
        tag_list = job.find("ul", {"class": "tag-list"})
        tags = tag_list.find_all("li")
    
        if len(tags) != 2:
            continue
        experience = tags[0].text
        education = tags[1].text


        key_word_list = job.find("div", {"class": "job-card-footer"}).find("ul", {"class": "tag-list"})
        key_words = key_word_list.find_all("li")

        key_words = [tag.text for tag in key_words]

        print(",".join(key_words))
        
        # Add the data to the sheet as a new row
        sheet.append([title, location, salary, experience, education , ",".join(key_words)])

    driver.quit()

    if page == 15:
        break

try:
    if os.path.exists("jobs.xlsx"):
        os.remove("jobs.xlsx")
except FileNotFoundError:
    print("File not found")
# Save the workbook to a file
workbook.save("jobs.xlsx")




