from tkinter import Tk, ttk
from tkinter import *
from PIL import Image, ImageTk
import requests
import json

# Colors
cor01 = "#ced9d9"  # grey
cor0 = "#FFFFFF"   # white
cor1 = "#333333"   # black
cor2 = "#617268"   # olive

# Window setup
window = Tk()
window.geometry('300x320')
window.title("Converter")
window.configure(bg=cor01)
window.resizable(height=FALSE, width=FALSE)

# Frames
top = Frame(window, width=300, height=60, bg=cor2)
top.grid(row=0, column=0)

main = Frame(window, width=300, height=260, bg=cor01)
main.grid(row=1, column=0)

# Currency conversion function
def convert():
    try:
        # Get input values
        currency_1 = combo1.get()
        currency_2 = combo2.get()
        amount = value.get()

        # Validate if the amount is a number
        if not amount.replace('.', '', 1).isdigit():
            result['text'] = "Enter a valid amount"
            return

        # API request setup
        url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
        querystring = {"from": currency_1, "to": currency_2, "amount": amount}
        headers = {
            "x-rapidapi-key": "0cc89ece41mshcbca23e2acf4273p177c88jsnd79a21b2d18c",
            "x-rapidapi-host": "currency-converter18.p.rapidapi.com"
        }

        # API Request
        response = requests.get(url, headers=headers, params=querystring)
        data = json.loads(response.text)

        # Check if the API response contains the result
        if "result" in data:
            converted_amount = data["result"]["convertedAmount"]
            symbol = currency_symbols.get(currency_2, '')
            formatted = symbol + "{:,.2f}".format(converted_amount)
            result['text'] = formatted
        else:
            result['text'] = "Error in conversion"

    except requests.exceptions.RequestException as e:
        result['text'] = "Error connecting to API"
        print(f"API request error: {e}")

    except Exception as e:
        result['text'] = "An error occurred"
        print(f"Error: {e}")

# Currency symbols and list
currency_symbols = {
    'USD': '$', 'INR': '₹', 'EUR': '€', 'BRL': 'R$', 'CAD': '$', 'ALL': 'Lek', 'AFN': '؋',
    'ARS': '$', 'AWG': 'ƒ', 'AUD': '$', 'AZN': '₼', 'BSD': '$', 'BBD': '$', 'BYR': 'p.',
    'BZD': 'BZ$', 'BMD': '$', 'BOB': '$b', 'BAM': 'KM', 'BWP': 'P', 'BGN': 'лв', 'BND': '$',
    'KHR': '៛', 'CLP': '$', 'CNY': '¥', 'COP': '$', 'CRC': '₡', 'HRK': 'kn', 'CZK': 'Kč',
    'DKK': 'kr', 'DOP': 'RD$', 'EGP': '£', 'HUF': 'Ft', 'ISK': 'kr', 'IDR': 'Rp', 'IRR': '﷼',
    'ILS': '₪', 'JPY': '¥', 'KPW': '₩', 'KRW': '₩', 'MXN': '$', 'NGN': '₦', 'NOK': 'kr',
    'PKR': '₨', 'PHP': '₱', 'PLN': 'zł', 'QAR': '﷼', 'RUB': '₽', 'ZAR': 'R', 'THB': '฿',
    'GBP': '£', 'UYU': '$U', 'VND': '₫'
}

currency = ["CAD", "BRL", "EUR", "INR", "USD", "AFN", "ARS", "ALL", "AWG", "AUD", "AZN", "BSD", "BBD",
            "BYR", "BZD", "BMD", "BOB", "BAM", "BWP", "BGN", "BND", "KHR", "KYD", "CLP", "CNY", "COP",
            "CRC", "HRK", "CZK", "DKK", "DOP", "EGP", "HUF", "ISK", "IDR", "IRR", "ILS", "JPY", "KPW",
            "KRW", "MXN", "NGN", "NOK", "PKR", "PHP", "PLN", "RUB", "ZAR", "THB", "GBP", "UYU", "VND"]

# Top Frame
try:
    icon = Image.open("cc.png")  # Ensure this path points to your image
    icon = icon.resize((40, 40))
    icon = ImageTk.PhotoImage(icon)
except FileNotFoundError:
    print("Image file not found. Please make sure 'cc.png' is in the correct directory.")
    icon = None  # Placeholder in case the image is not found

# Use icon only if it was loaded successfully
if icon:
    app_name = Label(top, image=icon, compound=LEFT, text="Currency Converter", height=5, padx=13, pady=30, anchor=CENTER, font=('Arial 16 bold'), bg=cor2, fg=cor01)
else:
    app_name = Label(top, text="Currency Converter", height=5, padx=13, pady=30, anchor=CENTER, font=('Arial 16 bold'), bg=cor2, fg=cor01)

app_name.place(x=0, y=0)


# Main Frame
result = Label(main, text=" ", width=16, height=2, pady=7, relief="solid", anchor=CENTER, font=('Ivy 15 bold'), bg=cor01, fg=cor1)
result.place(x=50, y=10)

from_label = Label(main, text="From", width=8, height=1, padx=0, pady=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=cor01, fg=cor1)
from_label.place(x=48, y=90)
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo1['values'] = (currency)
combo1.place(x=50, y=115)

to_label = Label(main, text="To", width=8, height=1, padx=0, pady=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=cor01, fg=cor1)
to_label.place(x=158, y=90)
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy 12 bold"))
combo2['values'] = (currency)
combo2.place(x=160, y=115)

entry_label = Label(main, text="Enter", width=8, height=1, padx=0, pady=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=cor01, fg=cor1)
entry_label.place(x=48, y=140)
value = Entry(main, width=22, justify=CENTER, font=("Ivy 12 bold"), relief=SOLID)
value.place(x=50, y=162)

button = Button(main, text="Converter", width=19, padx=5, height=1, bg=cor2, fg=cor01, font=("Ivy 12 bold"), command=convert)
button.place(x=50, y=210)

window.mainloop()
