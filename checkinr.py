# check if there's a high value of INR going on
# can check as global and local maxima
import requests, sys

sys.path.append("../check_status_uscis")
from check import *

XOOM_LINK = 'https://www.xoom.com/india/send-money'

response = requests.get(XOOM_LINK)
loc = response.text.find('1 USD =')
CURRENT_USD_INR_VALUE = response.text[loc+8: loc+15]

print("current USD = " + CURRENT_USD_INR_VALUE)

if (float(CURRENT_USD_INR_VALUE) >= 70.0):
  # send an email saying that it is so
  pass
