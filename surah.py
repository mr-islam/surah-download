from requests import get

reciter = "mishaari_raashid_al_3afaasee"
surah_number = 1 
surah_url = str(surah_number).zfill(3)

#url = "http://download.quranicaudio.com/quran/mishaari_raashid_al_3afaasee/001.mp3"
url = "http://download.quranicaudio.com/quran/" + reciter + "/" + surah_url +  ".mp3"
"""
def download(url, file_name):
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)
"""
for i in range(3):
    print(url)
    str(int(surah_number) + 1)
