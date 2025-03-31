import requests
from bs4 import BeautifulSoup

# https://papers.nips.cc/paper_files/paper/2024 

# URL of the paper's abstract page
url = "https://papers.nips.cc/paper_files/paper/2024/hash/000f947dcaff8fbffcc3f53a1314f358-Abstract-Conference.html"

file_path = "output.txt"

# Send a GET request to the page
response = requests.get(url)
response.raise_for_status()  # Raise error if request failed

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the abstract content (usually in a <p> tag under a div or section)
abstract = soup.find('div', class_='p-3')
abstract_text = abstract.get_text(strip=True)

# Writing the text to the file
with open(file_path, "w", encoding="utf-8") as file:
    file.write(abstract_text)

