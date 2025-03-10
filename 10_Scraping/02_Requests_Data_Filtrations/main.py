from bs4 import BeautifulSoup
import requests
import time

print("Put some skill that you are not familiar with:")
unfamiliar_skill = input(">")
print(f"filtering out...{unfamiliar_skill}")

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=Python&txtLocation=').text

    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

    for idx, job in enumerate(jobs):
        pub_date = job.find('span', class_ = "sim-posted").span.text # type: ignore
        if 'few' in pub_date:
            comp_name = job.find('h3', class_ = "joblist-comp-name").text.replace(' ','') # type: ignore
            skills = job.find('div', class_ = "srp-skills").div.text.replace('\n', '').replace(' ','') # type: ignore
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                
                with open(f'posts/{idx}.txt', 'w') as f:
                
                    f.write(f"Company Name: {comp_name.strip()} \n") #type: ignore
                    f.write(f"Skills Required: {skills.strip()} \n") #type: ignore
                    f.write(f"More info: {more_info}")
                print(f"File Saved: {idx}.txt")



if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes")
        time.sleep(time_wait * 60)
        