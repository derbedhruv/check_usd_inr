from urllib import request, parse
import datetime, pytz, re

DOLLAR_RUPEE_WEBSITE = "http://dollarrupee.in/"
STRING_TO_LOOK_FOR = 'Current USD to INR exchange rate equals <strong>'
LENGTH_OF_DIGITS = 7
LOG_FILENAME = "usdinr.log"
EXPECTED_INR_REGEX = "\d\d\.\d\d\d\d"

def getusdinr():
  # call the dollar rupee website and check status
  resp = request.urlopen(DOLLAR_RUPEE_WEBSITE).read().decode('utf-8')
  loc = resp.find(STRING_TO_LOOK_FOR) + len(STRING_TO_LOOK_FOR)
  return resp[loc:loc+LENGTH_OF_DIGITS]

def expectedinrformat(inr):
  # check if the INR parsed value is in expected format
  return re.compile(EXPECTED_INR_REGEX).match(inr)

if __name__ == "__main__":
  inr = getusdinr()
  print(inr)
  print(expectedinrformat(inr))
