import requests

class currencyConversion:  
    def convert_currency(self,amount, from_cur, to_cur):
        url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_cur.upper()}&to={to_cur.upper()}"
        response = requests.get(url)
        data = response.json()
        return round((data['rates'][to_cur.upper()]),2) #returns coverted rate


amt=3600
from_curr='inr'
to_curr='usd'

currency_obj=currencyConversion()
result=currency_obj.convert_currency(amt, from_curr, to_curr)


print(f'{amt} {from_curr.upper()} -> {to_curr.upper()} {result}')
