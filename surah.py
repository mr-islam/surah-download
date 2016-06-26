from requests import get
import names
q_reciter = input('Which reciter would you like to listen to? \n 1 - Mishary Rashid Al \'Afasy \n 2 - [coming soon!] \n')

if q_reciter == 1:
    reciter = "mishaari_raashid_al_3afaasee"
##elif q_reciter == 2:
##    other reciter blablabla
else:
    reciter = "mishaari_raashid_al_3afaasee"

q_surahs = input('Would you like to download all the Surahs? \n 1 - Yes, all of them! \n 2 - [coming soon] \n')

##if q_surahs == 1:
##    #bla
##else if q_surahs == 2:
##    #bla
##
#surah_name = names.s+surah_number
#print(surah_name)
##
surahs_to_download = input('How many Surahs would you like to download?')

def download(url, file_name):
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)

start_surah = input()

surah_number = 1 

for i in range(surahs_to_download):
    url = "http://download.quranicaudio.com/quran/" + reciter + "/" + str(surah_number).zfill(3) +  ".mp3"
    print('Surah ' + str(surah_number))

    file_name = 'Surah ' + str(surah_number)

    print('Donwloading ' + file_name)
    download(url, file_name)

    int(surah_number)
    print('incrementing... \n')
    surah_number += 1
    str(surah_number)

print('JazakAllahu Khairan for using!')
#TODO: option, number of surahs to download, or all - make it branches with prompts
#TODO: choice of reciter
#TODO: creat vars.py with name of sirah, to choose one suah to dowwnload, and also filenames
