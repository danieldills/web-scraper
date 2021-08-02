from bs4 import BeautifulSoup
import requests
import time

url = "https://en.wikipedia.org/wiki/History_of_Mexico"
required_string = "citation needed"

def get_citations_needed_count(url):
  res = requests.get(url)
  soup = BeautifulSoup(res.content, 'html.parser')
  para_list = soup.find_all('p') 
  citation_count = 0

  for item in para_list:
    for string in item.stripped_strings:
      if required_string in repr(string):
        citation_count += 1
  print(f'Number of Citations: {citation_count}\n')

def get_citations_needed_report(url):
    res = requests.get(url)
    list_with_citation = []
    results = []
    soup = BeautifulSoup(res.content, 'html.parser')

    pararaph_list = soup.find_all('p')

    for paragraph in pararaph_list:
        if required_string in paragraph.text:
            list_with_citation.append(paragraph.text)

    for paragraph in list_with_citation:
        head, sep, tail = paragraph.rpartition('[citation needed]')
        if required_string in head:
            new_head, sep, new_tail = head.partition('[citation needed]')
            results.append(new_head)
            results.append(new_tail)
        else:
            results.append(head)
    print('Paragraph with Citation needed:\n')
    for paragraph in results:
        print(paragraph)
        print()
        time.sleep(2)

get_citations_needed_count(url)
get_citations_needed_report(url)
