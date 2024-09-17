import requests
import json

url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

currency_1 = "INR"
currency_2 = "USD"
amount = "1000"

querystring = {"from":currency_1,"to":currency_2,"amount":amount}

headers = {
	"x-rapidapi-key": "0cc89ece41mshcbca23e2acf4273p177c88jsnd79a21b2d18c",
	"x-rapidapi-host": "currency-converter18.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = json.loads(response.text)
converted_amount = data["result"]["convertedAmount"]
formated = "{:,.2f}".format(converted_amount)

print(formated)
