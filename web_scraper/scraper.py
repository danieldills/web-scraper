from bs4 import BeautifulSoup
import requests
import time

url = "https://en.wikipedia.org/wiki/History_of_Washington_(state)"
required_string = "citation needed"

def get_citations_needed_count(url):
  url_content = requests.get(url)
  soup = BeautifulSoup(url_content.content, 'html.parser')
  paragraph_list = soup.find_all('p') 
  citation_count = 0

  for item in paragraph_list:
    for string in item.stripped_strings:
      if required_string in repr(string):
        citation_count += 1
  print(f'Number of Citations: {citation_count}\n')

def get_citations_needed_report(url):
    url_content = requests.get(url)
    list_with_citation = []
    displayed_results = []
    soup = BeautifulSoup(url_content.content, 'html.parser')

    paragraph_list = soup.find_all('p')

    for paragraph in paragraph_list:
        if required_string in paragraph.text:
            list_with_citation.append(paragraph.text)

    for paragraph in list_with_citation:
        head, seperator, tail = paragraph.rpartition('[citation needed]')
        if required_string in head:
            new_head, seperator, new_tail = head.partition('[citation needed]')
            displayed_results.append(new_head)
            displayed_results.append(new_tail)
        else:
            displayed_results.append(head)
    print('Paragraph with Citation needed:\n')
    for paragraph in displayed_results:
        print(paragraph)
        print()
        time.sleep(2)

get_citations_needed_count(url)
get_citations_needed_report(url)
