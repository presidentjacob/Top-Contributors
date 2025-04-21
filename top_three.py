from bs4 import BeautifulSoup
import requests

# Set all urls
year_2022 = 'https://openaccess.thecvf.com/CVPR2022?day=all'
year_2023 = 'https://openaccess.thecvf.com/CVPR2023?day=all'
year_2024 = 'https://openaccess.thecvf.com/CVPR2024?day=all'

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

    # Loop through all people and add them to the dictionary
    for people in find_people:
        for person in people.find_all('a'):
            name = person.text.strip()
            # Add to dictionary if name doesn't exist
            if name not in all_people:
                all_people[name] = 1
            # If name exists, increment the count
            else:
                all_people[name] += 1

    return all_people

def main():
    # Get all people from each year
    all_2022 = get_url(year_2022)
    all_2023 = get_url(year_2023)
    all_2024 = get_url(year_2024)

main()