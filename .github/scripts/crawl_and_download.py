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

    # Adjust search to be more flexible and account for different spellings (Immunization/Immunisation)
    link_container = soup.find(lambda tag: tag.name == "li" and "National Immunization Schedule" in tag.text)
    if link_container:
        link = link_container.find('a')
        if link and link.get('href'):
            download_url = link.get('href')
            file_name = download_url.split('/')[-1]
            download_file(download_url, file_name)
            print(f"Downloaded {file_name}")
        else:
            print("Link to National Immunisation Schedule not found.")
    else:
        print("National Immunisation Schedule not found.")

if __name__ == "__main__":
    main()
