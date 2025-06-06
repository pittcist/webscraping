import requests
from bs4 import BeautifulSoup
import time
import subprocess

# URL of the job posting
url1 = "https://openai.com/careers/account-director-digital-native/"

def download_page(url):
    # Send a GET request to the URL
    # Set headers to mimic a browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/114.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://openai.com/",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }

    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the HTML content to a file
        with open(url+".html", "w", encoding="utf-8") as file:
            file.write(response.text)
        print("HTML content saved to 'openai_job_posting.html'")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

    return(response.status_code)

def download_page_curl(url):
    # Build the curl command
    url = url.strip("\n")
    output_file = url.split("https://openai.com/careers/")[1].strip("/\n") + ".html"
    print(output_file)
    curl_command = [
        "curl",
        "-A", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",  # User-Agent to mimic a browser
        url,
        "-o", output_file # Output file
    ]

    # Run the command
    subprocess.run(curl_command, check=True)
    print(f"Page saved as '{output_file}'")

def retrive_links(filename):
     # Load the local HTML file
    with open(filename, "r", encoding="utf-8") as file:
        html_content = file.read()

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Exact class string to match
    target_class = "py-sm gap-4xs @md:flex-row @md:items-baseline @md:flex-grow @md:gap-4xs flex flex-grow flex-col items-start"

    # Find all <a> tags with the exact class
    links = soup.find_all("a", class_=lambda c: c and " ".join(c.split()) == target_class)

    # Extract href values
    hrefs = [link.get("href") for link in links if link.get("href")]

    # Print the extracted hrefs
    with open("file_links.txt", "w", encoding="utf-8") as file:
        for href in hrefs:
            print("https://openai.com"+href)
            file.write("https://openai.com"+href + "\n")


def read_links(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = file.readlines()
    return data

# download_page_curl("https://openai.com/careers/account-director-digital-native/")

# retrive_links("openai_jobs.html")

dt = read_links("file_links.txt")
for item in dt:
    print(item)
    download_page_curl(item)
    time.sleep(10)


# # Extract the job title
# abstract = soup.find('div', class_='relative flex flex-col items-center text-center')
# abstract_text = str(abstract)
# print(abstract_text)


