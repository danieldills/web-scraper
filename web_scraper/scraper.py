from bs4 import BeautifulSoup
import requests
import time

url = "https://en.wikipedia.org/wiki/History_of_Mexico"
req_string = "citation needed"

def get_citations_needed_count():
  res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    pararaph_list = soup.find_all('p') 
    citation_count = 0

    # for loop goes here

def get_citations_needed_report():
  pass
