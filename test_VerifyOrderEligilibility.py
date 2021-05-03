import requests
import json
import jsonpath
import test_FetchSubscription
import pytest


def test_verifyordereligibility(newmsisdn, newcustAcc, SubsId):

            url="https://ysita-bssapi.staging.qvantel.net/v3/yoigo/orders/order-eligibilities-validate"
            headers = {'Authorization': 'Token token=010164a2f544432b905db047e16947dc', 'X-Trace-Token': '5a1fc588-183f-4c0d-a593-ce0c351def0c', 'Content-Type': 'application/vnd.api+json'}

            #Abrir y leer archivo
            file = open('//Users//rebeca.modrego//Desktop//API//order_eligibility_validate.json', 'r+')
            file_input=file.read()
            #Transformar a JSON
            json_file=json.loads(file_input)
            oldAccId=jsonpath.jsonpath(json_file,"data.attributes.customer-info.account-id")

            oldMsisdn=jsonpath.jsonpath(json_file,"data.attributes.customer-info.phone-number.msisdn")

            x=test_FetchSubscription.test_fetchsubscription(SubsId)


            newmsisdn=x[0]
            newcustAcc=x[1]

            #print(newmsisdn)
            #print(newcustAcc)

            file_input=file_input.replace(oldMsisdn[0],newmsisdn)
            file_input=file_input.replace(str(oldAccId[0]),newcustAcc)

            #print(file_input)

            json_file1=json.loads(file_input)
            response=requests.post(url, headers=headers, json=json_file1)
            output_json=json.loads(response.text)
            output=jsonpath.jsonpath(output_json,"data.attributes.is-order-allowed")

            output1=jsonpath.jsonpath(output_json,"data.attributes.rejection-reason")

            #Return if order is allowed or not
            return (output[0], output1[0])



