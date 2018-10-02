#!/usb/bin/env python

#This program calculates the total entropy of a supplied password
#and then calculates how long it would take to break that password

from math import log
from getpass import getpass
import os
import re

def get_pool_length(password):
  pool_length = 0
  if re.match("(?=.*[a-z]).*", password): pool_length += 26
  if re.match("(?=.*[A-Z]).*", password): pool_length += 26
  if re.match("(?=.*[0-9]).*", password): pool_length += 10
  if re.match("(?=.*[ -\-:-@\[-\`{-~]).*", password): pool_length += 27  
## This regex is 3 different ranges and encompasses all printable special characters 16 + 7 + 4
  return pool_length


password = getpass()

pool_length = get_pool_length(password)
print "Character Pool Length is", pool_length, "Password Length is", len(password)

total_entropy = log(pool_length, 2) * len(password)

print "Total Entropy is", total_entropy
print "The number of possible combinations is:", 2 ** total_entropy
print "At 80 billion guesses per second, your password would last for", ((2 ** total_entropy)/(80000000000))/60/60/24/365, "Years" 
