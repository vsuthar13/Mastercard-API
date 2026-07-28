import json

import requests
import oauth1.authenticationutils as authenticationutils
from oauth1.oauth import OAuth, SignatureMethod


CONSUMER_KEY = "XX" #Go to your project in the developer portal->Credentials->Get the consumer key from the Oauth keys table


p12_path = 'XX' #Local path to your p12 file
signing_key = authenticationutils.load_signing_key(p12_path, 'XX') #Password that you had set while generating the key in developer portal



url = "https://sandbox.api.mastercard.com/mastercom/v6/cases"

payload_data = {
    "caseType": "1",
    "chargebackRefNum": [
        "1111423456"
    ],
    "customerFilingNumber": "5482",
    "disputeAmount": "200.00",
    "currencyCode": "USD",
    "dueDate": "2021-02-20",
    "filedAgainstIca": "004321",
    "filingAs": "A",
    "filingIca": "001234",
    "memo": "This is a test memo",
    "messageText": "This is a test message",
    "changeReasonCodeFlag": "Y",
    "updatedChargebackReasonCode": "4863",
    "changeReasonCodeReason": "This is a test reason",
    "primaryAccountNum": "5123123412341234",
    "acquirerRefNum": "05131054165000000048149",
    "chargebackReasonCode": "4863",
    "merchantName": "test name",
    "violationCode": "D.2",
    "violationDate": "2021-01-15",
    "chargebackDate": "2021-02-15",
    "creditDate": "2021-02-15"
}

payload_body = json.dumps(payload_data)

authHeader = OAuth.get_authorization_header(url, 'POST', payload_body, CONSUMER_KEY, signing_key,signature_method=SignatureMethod.RSA_PSS_SHA256)
headerdict = {'Authorization' : authHeader, 'content-type': 'application/json', 'Accept' : 'application/json'}
response=requests.post(url, headers=headerdict, data=payload_body)
print(response.json()) #prints the caseID that we received from the API call

