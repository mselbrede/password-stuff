#This program downloads a dictionary and then uses it to construct a password made of four random words


import requests
import random
import hashlib
import os
word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"




def get_wordlist(site):
  if "wordlist.dic" in os.listdir(os.getcwd()):
    with open("wordlist.dic") as file:
      return file.readlines()
  else:
    with open("wordlist.dic", "w") as file:
      response = requests.get(word_site)
      file.write(response.content)
      return get_wordlist(site)

word_list = get_wordlist(word_site)
  


newpassword = ""
for i in range(4):
  newpassword = newpassword + random.choice(word_list).strip()

newPasswordHash = hashlib.sha256(newpassword)

print("A better password is:", newpassword)
print("The hash is", newPasswordHash.hexdigest())
print("Try that instead!")
