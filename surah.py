from requests import get

reciter = "mishaari_raashid_al_3afaasee"
#surah_url = str(surah_number).zfill(3)

#url = "http://download.quranicaudio.com/quran/mishaari_raashid_al_3afaasee/001.mp3"

surah_number = 1 
for i in range(3):
    url = "http://download.quranicaudio.com/quran/" + reciter + "/" + str(surah_number) +  ".mp3"
    print(url)
    int(surah_number)
    surah_number += 1
    str(surah_number)
"""
def download(url, file_name):
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)

"""
