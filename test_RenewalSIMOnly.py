import requests
import json
import jsonpath
import pytest

def test_renewalsimonly(newcustAcc, newSubscriptionId, newbillingAcc):

            headers = {'Authorization': 'Token token=010164a2f544432b905db047e16947dc', 'X-Trace-Token': '5a1fc588-183f-4c0d-a593-ce0c351def0c', 'Content-Type': 'application/vnd.api+json'}
            url2= 'https://ysita-bssapi.staging.qvantel.net/v3/yoigo/orders/orders'


            #Create Renewal order SIM only
            #1. Open and read the file
            file=open('//Users//rebeca.modrego//Desktop//API//Renewal_SIM_Only_Financed_Terminal.json', 'r+')
            file_input=file.read()

            #Transformar fichero en formato JSON
            json_file=json.loads(file_input)

            #Sacar los valores de customer-account, billing-account y subscription-id del JSON anterior
            OldsubscriptionId=jsonpath.jsonpath(json_file,'data.attributes.parent-agreement-id')
            #print(OldsubscriptionId[0])

            OldCustAcc=jsonpath.jsonpath(json_file,'data.relationships.customer-account.data.id')
            #print(OldCustAcc[0])

            OldBillingAcc=jsonpath.jsonpath(json_file,'included[0].relationships.billing-account.data.id')
            #print(OldBillingAcc[0])

            #Hacemos el replace de los valores en el fichero txt antes de convertir a JSON
            file_input=file_input.replace(OldsubscriptionId[0],str(newSubscriptionId))
            #print(file_input)
            file_input=file_input.replace(OldCustAcc[0],newcustAcc)
            file_input=file_input.replace(OldBillingAcc[0],str(newbillingAcc))

            json_file1=json.loads(file_input)
            #print(json_file1)

            #Hacemos el pedido e Renuevo SIM Only
            response=requests.post(url2,headers=headers,json=json_file1)
            print(response.content)
            #print(response.status_code)
            content=response.content
            statuscode=response.status_code
            return (content, statuscode)