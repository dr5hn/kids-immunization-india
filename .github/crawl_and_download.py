# .github/scripts/crawl_and_download.py
import requests
from bs4 import BeautifulSoup

# URL to crawl
url = "https://main.mohfw.gov.in/?q=Organisation/Departments-of-Health-and-Family-Welfare/immunization"

def download_file(download_url, file_name):
    response = requests.get(download_url)
    with open(file_name, 'wb') as file:
        file.write(response.content)

def main():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the 'National Immunization Schedule' link
    link = soup.find('a', title="PDF that opens in a new window")
    if link:
        download_url = link.get('href')
        file_name = download_url.split('/')[-1]
        download_file(download_url, file_name)
        print(f"Downloaded {file_name}")
    else:
        print("National Immunization Schedule not found.")

if __name__ == "__main__":
    main()
