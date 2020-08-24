'''
ws_indeed.py
References:
https://medium.com/@msalmon00/web-scraping-job-postings-from-indeed-96bd588dcb4b
https://stackoverflow.com/questions/55097699/scrap-top-100-job-results-from-indeed-using-beautifulsoup-python
https://requests.readthedocs.io/en/master/user/advanced/
https://www.youtube.com/watch?v=FLZvOKSCkxY
'''

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

''' INDEED URL STRUCTURE
Base: 
    "https://indeed.com/jobs?"
Job: 
    "q=" followed by job title/keywords/company - separated by +
Salary: 
    start with "+%24"; commas = "%2C" (EX. %2430%2C000 = $30,000)
Location: 
    "&l=" followed by location - separated by +
Job Type: 
    "&jt=" followed by job type
Experience Level: 
    "&explvl=" followed by experience level
New
    "&fromage=last"
Start
    "&start=" followed by ith result you want to start at (EX. 10)
'''

# URL = "https://www.indeed.com/jobs?q=biomedical+engineering+internships&start=10"
# page = requests.get(URL)
# print(page.status_code)
# soup = BeautifulSoup(page.text, "html5lib")
# tit = [t.get_text() for t in soup.find_all("div", attrs={'class':'title'})]
# com = [c.get_text() for c in soup.find_all('span', attrs={'company'})]
# loc = [l.get_text() for l in soup.find_all('span', attrs={'class':'location'})] 
# s_m = [s.get_text() for s in soup.find_all('div', attrs={'class':'summary'})]
# d_p = [dp.get_text() for dp in soup.find_all('span', attrs={'date'})]

# # TODO:
# DONE # (1) create pandas dataframe 
# # (2) analyze dataframe for relevant jobs - based on input params - natural language processing
# # (3) main function - input args/params  -> build URL
# DONE # (4) export data into excel doc
# # (5) BIG Q'S: .strip(), zip/newList, Session(), ID vs Class vs tags
# # (6) For each link, find job purpose, primary tasks, qualifications/skills/experience (if available)

filename = 'C:\Eclipse\Web_Scraper\indeed_job_postings.csv'
columns = ["location", "job_title", "company", "link"]

URL = "https://www.indeed.com/jobs?q=biomedical%20engineering%20internships"
results = []

with requests.Session() as s:
    for page in range(1):
        res = s.get(URL.format(page))
        soup = BeautifulSoup(res.content, 'lxml')
        
        # Find location - isolate city, state
        loc_temp = [item.text.strip() for item in soup.select('.location')]
        loc = [''.join([w for w in item.split()[:3] if not w.isdigit()]) for item in loc_temp]
        
        # Find job title
        titl = [item.text.strip() for item in soup.select('[data-tn-element=jobTitle]')]
        
        # Find company name
        comp = [item.text.strip() for item in soup.select('.company')]       
        
        # Find link
        href = [urljoin(URL, item.find('a')['href']) for item in soup.find_all('div', attrs={'class':'title'})]    
            
        data = list(zip(loc, titl, comp, href))
        results.append(data)

newList = [item for sublist in results for item in sublist]
df = pd.DataFrame(newList, columns=columns)  

# NLP 

df.to_csv(filename)

print("Yeaahh...")