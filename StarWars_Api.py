import requests

option = input("Escolhe a opção que deseja explorar: ").strip().lower()


def fetch_data(option):

    url = f"https://swapi.mimo.dev/api/{option}/"
    data = []
    try:
        response = requests.get(url)

        response.raise_for_status()

        data = response.json()
        print(f" o número de entidsdes total é de: {len(data)}")
        return data

    except requests.HTTPError as e:
        print(f"O erro gerado foi o erro de {e}")
        return None


data = fetch_data(option)

if data:
    for entity in data:
        name = entity["name"]
        print(name)
else:
    print("Unable to download data")
