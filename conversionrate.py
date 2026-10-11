import json
import requests
import oauth1.authenticationutils as authenticationutils
from oauth1.oauth import OAuth, SignatureMethod


CONSUMER_KEY = "XX" #Go to your project in the developer portal->Credentials->Get the consumer key from the Oauth keys table
p12_path = 'XX' #Local path to your p12 file
signing_key = authenticationutils.load_signing_key(p12_path, 'XX') #Password that you had set while generating the key in developer portal



base_url = "https://sandbox.api.mastercard.com/settlement/currencyrate/conversion-rate"

params ={
    "fxDate":"2026-10-11",
    "transCurr":"INR",
    "crdhldBillCurr":"USD",
    "bankFee":5,
    "transAmt":100
}

request = requests.Request(method="GET", url=base_url, params=params)
prepared=request.prepare()
prepared_url=prepared.url


authHeader = OAuth.get_authorization_header(prepared_url, 'GET','', CONSUMER_KEY, signing_key,signature_method=SignatureMethod.RSA_SHA256)

headerdict = {'Authorization' : authHeader, 'Accept' : 'application/json'}
response=requests.get(prepared_url, headers=headerdict)
result=response.json()
print(f'Conversion rate - {result['data']['conversionRate']}\nCardholder amount -{result['data']['crdhldBillAmt']}')