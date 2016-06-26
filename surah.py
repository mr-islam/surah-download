from requests import get

def download(url, file_name):
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)


