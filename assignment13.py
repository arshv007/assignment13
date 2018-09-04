#Question1

import requests
information=requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en")
print(info.status_code)
import json
det=information.json()
print(type(det))
print(det["quoteText"])
