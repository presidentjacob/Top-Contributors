from bs4 import BeautifulSoup
import requests

def get_url(url):
    response = requests.get(url)
    # Check response if the response is successful
    if response.status_code == 200:
        return get_all(response)
    else:
        # If response is not 200, raise an exception with the status code and return None
        raise Exception(f'Response status code: {response.status_code}')
    return None

def get_all(response):
    # Create soup to find all people
    soup = BeautifulSoup(response.text, 'lxml')
    find_people = soup.find_all('dd')
    # Create a dictionary to store all people
    all_people = dict()

