import json
import requests
import oauth1.authenticationutils as authenticationutils
from oauth1.oauth import OAuth, SignatureMethod

CONSUMER_KEY = "XX"  #Go to your project in the developer portal->Credentials->Get the consumer key from the Oauth keys table


p12_path = 'XX' #Local path to your p12 file
signing_key = authenticationutils.load_signing_key(p12_path, 'XX') #Password that you had set while generating the key in developer portal

url="https://sandbox.api.mastercard.com/settlement/currencyrate/settlement-currencies"


authHeader = OAuth.get_authorization_header(url, 'GET', None, CONSUMER_KEY, signing_key,signature_method=SignatureMethod.RSA_PSS_SHA256)
headerdict = {'Authorization' : authHeader}
response=requests.get(url, headers=headerdict)
result=response.json()



for currency in result['data']['currencies']:
    print(currency['alphaCd'] + '-'+ currency['currNam'])