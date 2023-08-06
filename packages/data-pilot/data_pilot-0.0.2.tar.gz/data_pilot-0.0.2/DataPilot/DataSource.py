import requests
import decouple
from supabase import create_client, Client

# Alpha vantage API

def AlphaVantageIntraday(api_key:str="", symbol:str=""):

    url = "https://alpha-vantage.p.rapidapi.com/query"

    querystring = {
        "interval": "1min",
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "datatype": "json",
        "output_size": "compact"
    }

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()

# Supabase

# # Get your project URL and API key from the Supabase dashboard
# url:str = decouple.config("SUPABASE_MRDATA_PROJECT_URL")
# key:str = decouple.config("SUPABASE_MRDATA_API_KEY")
# email:str = decouple.config("SUPABASE_USER")
# password:str = decouple.config("SUPABASE_PASSWORD")
# mr_db:Client = create_client(url, key)
# user = mr_db.auth.sign_in_with_password({ "email": email, "password": password })

# user=postgres
# password=[YOUR-PASSWORD]
# host=db.cahulnvuzydcxbjzxnxc.supabase.co
# port=5432
# database=postgres
