import requests
from bs4 import BeautifulSoup
import csv

neurips = "https://papers.nips.cc/paper_files/paper/2024"

# URL of the paper's abstract page
url = "https://papers.nips.cc/paper_files/paper/2024/hash/000f947dcaff8fbffcc3f53a1314f358-Abstract-Conference.html"

output_file = "output.csv"

# Extract links from the conference homepage
def get_all_links_and_save(url, output_csv):
    response = requests.get(url)
    response.raise_for_status()  
    soup = BeautifulSoup(response.text, 'html.parser')

    links = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href.startswith('/'):
            href = 'https://papers.nips.cc' + href
        links.append(href)

    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Hyperlink'])  
        for link in links:
            writer.writerow([link])

    print(f"{len(links)} links saved to {output_csv}")

# Extract abstract from the abstract page
def extract_abstract(page_url):
    response = requests.get(page_url)
    response.raise_for_status()  

    soup = BeautifulSoup(response.text, 'html.parser')

    abstract = soup.find('div', class_='p-3')
    abstract_text = abstract.get_text(strip=True)
    return str(abstract_text)

# Extract links to abstract pages and save to a csv file
# get_all_links_and_save(neurips, "neurips_2024_links.csv")

with open("neurips_2024_links.csv", "r", encoding="utf-8") as file:
    with open(output_file, "w+", encoding="utf-8") as output_file:
        reader = csv.reader(file)
        writer = csv.writer(output_file)
        count = 1
        for row in reader:
            print(row[0])         
            try:
                abstract = extract_abstract(row[0])
                print(abstract)
                writer.writerow(abstract)
                # output_file.write(', "/n",')
            except:
                print("Invalid link")

# abstract = extract_abstract(url)
# print(abstract)

# Writing the text to the file
# with open(file_path, "w", encoding="utf-8") as file:
#     file.write(abstract_text)