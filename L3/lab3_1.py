# Opracuj program, korzystający z wyrażeń regularnych zmień przykładowy nagłówek wiadomości w słownik.

#biblioteka - wyrazenia regularne
import re

#naglowek wiadomosci
header = """From: author@example.com
User-Agent: Thunderbird 1.5.0.9 (X11/20061227)
MIME-Version: 1.0
To: editor@example.com"""

#wpisanie po zdaniu do slownika
sender , UA , version , receiver = header.split('\n')

#slowniki
dictionary = {
    "From ": sender,
    "User - Agent ": UA ,
    "MIME - Version ": version ,
    "To ": receiver ,
}

#wypisz to co wpisano do slownika
for i in dictionary :
    print(dictionary [i])

print('\n')

#email
email = r'[\w\.-]+@[\w\.-]+'

#nadawca
find_sender = re.search(email, sender)
if find_sender :
    print ("Sender : ", find_sender.group())
#UA
find_UA = UA.split(r":" ,1)
print ("UA : ", find_UA[1])

#wersja
find_version = version.split(r": ",1)
print("Version : ", find_version[1])

#odbiorca
find_receiver = re.search(email, receiver)
if find_receiver :
    print ("Receiver : ", find_receiver.group())
