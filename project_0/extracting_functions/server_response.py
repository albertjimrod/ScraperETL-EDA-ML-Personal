# Entering the address and check the response from the server.

import requests                 # Is an elegant and simple HTTP library for Python


def response(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            return requests.get(url)
            print("Conexión exitosa")

    
    except requests.exceptions.HTTPError as errh:
        print(f"Error HTTP: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error de conexión: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
