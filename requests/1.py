import requests

def req1():
    base_url = 'http://localhost:8000'

    # Define the endpoint and parameters
    endpoint = '/app1'  # Accessing /app1
    params = {
        'username': 'kekwmek',
        'message': 'govchernovar'
        }  # Optional query parameters

    # Send the Post request
    response = requests.post(url=base_url + endpoint, json=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the JSON response
        print(response.json())
    else:
        print(f'Error {response=}')



def req2():
    base_url = 'http://localhost:8000'

    # Define the endpoint and parameters
    endpoint = '/user_is_adult'  # Accessing /app1
    params = {
        'username': 'kekwmek',
        'age': 15
        }  # Optional query parameters

    # Send the Post request
    response = requests.post(url=base_url + endpoint, json=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the JSON response
        print(response.json())
    else:
        print(f'Error {response=}')


def req3():
    base_url = 'http://localhost:8000'

    # Define the endpoint and parameters
    endpoint = '/feedback/write'  # Accessing /app1
    params = {
        'username': 'shlypa',
        'fb_message': 'kak raz'
        }  # Optional query parameters

    # Send the Post request
    response = requests.post(url=base_url + endpoint, json=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Print the JSON response
        print(response.json())
    else:
        print(f'Error {response=}')


if __name__ == '__main__':
    req3()