import requests
import json
import jsonpath
import datetime
import test_VerifyOrderEligilibility
import pytest

#@pytest.fixture
#def start_exec():
    #global file
    #file = open('//Users//rebeca.modrego//Desktop//API//device_financing_conditions.json', 'r+')


def test_financingconditions(newmsisdn):

            url = "https://ysita-bssapi.staging.qvantel.net/v3/yoigo/revenue/device-financing-conditions-query"
            headers = {'Authorization': 'Token token=010164a2f544432b905db047e16947dc', 'X-Trace-Token': '5a1fc588-183f-4c0d-a593-ce0c351def0c', 'Content-Type': 'application/vnd.api+json'}

            #Abrir y leer archivo
            file=open('//Users//rebeca.modrego//Desktop//API//device_financing_conditions.json', 'r+')
            file_input=file.read()
            #Transformar a JSON
            json_file=json.loads(file_input)
            time=jsonpath.jsonpath(json_file,'data.attributes.reference-time')
            oldmsisdn=jsonpath.jsonpath(json_file,"data.attributes.msisdn")
            file_input=file_input.replace(oldmsisdn[0], newmsisdn)
            #Modifying the date -> today date + 00:00:00
            file_input=file_input.replace(time[0], str(datetime.date.today())+"T00:00:00.000Z")
            #print(file_input)
            json_file1=json.loads(file_input)
            response=requests.post(url, headers=headers, json=json_file1)
            #print(response.content)
            #print(response.status_code)
            #Convert output into JSON
            json_response1=json.loads(response.content)
            #print(json_response1)
            Q25Extension=jsonpath.jsonpath(json_response1,"data.attributes.quota-25-extension-status")
            permanency=jsonpath.jsonpath(json_response1,"data.attributes.permanency-contract-id")
            installment=jsonpath.jsonpath(json_response1,"data.attributes.installment-contract-id")
            discount=jsonpath.jsonpath(json_response1,"data.attributes.quota-25-discount-amount")

            #print(Q25Extension[0])
            #print(discount[0])
            #print(int(discount[0]))

            return (Q25Extension[0], permanency[0], installment[0], discount[0])
