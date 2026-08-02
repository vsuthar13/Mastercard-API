import json
import requests
import oauth1.authenticationutils as authenticationutils
from oauth1.oauth import OAuth, SignatureMethod


CONSUMER_KEY = "XX" #Go to your project in the developer portal->Credentials->Get the consumer key from the Oauth keys table
p12_path = 'XX' #Local path to your p12 file
signing_key = authenticationutils.load_signing_key(p12_path, 'XX') #Password that you had set while generating the key in developer portal



url = "https://sandbox.api.mastercard.com/bin-resources/bin-ranges/account-searches"

payload_data ={
    "accountRange":"777305770"
}
payload_body = json.dumps(payload_data)

authHeader = OAuth.get_authorization_header(url, 'POST', payload_body, CONSUMER_KEY, signing_key,signature_method=SignatureMethod.RSA_SHA256)

headerdict = {'Authorization' : authHeader, 'Content-Type': 'application/json', 'Accept' : 'application/json'}
response=requests.post(url, headers=headerdict, data=payload_body)
print(response.json())
