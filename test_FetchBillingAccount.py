import requests
import json
import jsonpath
import pytest


def test_fetch_BAcc(custAcc):
            #First create an order
            #Fetch the subscription-id using the msisdn of the created order
    url="https://ysita-bssapi.staging.qvantel.net/v3/yoigo/customers/billing-accounts/?filter=(EQ%20customer-account.id%20%22" + custAcc + "%22)"
    #Send GET request
    response=requests.get(url)
    #Display de BODY of the Output JSON
    json_response=json.loads(response.content)
    billingAcc = jsonpath.jsonpath(json_response, 'data.id')
    return (billingAcc)
