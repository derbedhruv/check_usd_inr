# check if there's a high value of INR going on
# can check as global and local maxima
import requests, sys, datetime, pytz
from gmail import *

# MAIN: check xoom
XOOM_LINK = 'https://www.xoom.com/india/send-money'

response = requests.get(XOOM_LINK)
loc = response.text.find('1 USD =')
CURRENT_USD_INR_VALUE = response.text[loc+8: loc+15]

now = datetime.datetime.now(pytz.timezone('America/Los_Angeles'))
print("{} current USD = {}".format(now, CURRENT_USD_INR_VALUE))

if (float(CURRENT_USD_INR_VALUE) >= 70.0):
  # send an email saying that it is so
  message = create_message("me", "dhruv.joshi.1989@gmail.com", "Rupee has gone above 70!", "New value is {}".format(CURRENT_USD_INR_VALUE))
  send_message(service, "me", message )
else:
  message = create_message("me", "dhruv.joshi.1989@gmail.com", "Rupee is uninteresting", "value is {}".format(CURRENT_USD_INR_VALUE))
  send_message(service, "me", message )
