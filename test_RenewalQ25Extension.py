import requests
import json
import jsonpath
import pytest


def test_renewalQ25extension(newcustAcc, newSubscriptionId, newbillingAcc, discount, PAYTERM, TERM):

            headers = {'Authorization': 'Token token=010164a2f544432b905db047e16947dc', 'X-Trace-Token': '5a1fc588-183f-4c0d-a593-ce0c351def0c', 'Content-Type': 'application/vnd.api+json'}
            url2= 'https://ysita-bssapi.staging.qvantel.net/v3/yoigo/orders/orders'

            file=open('//Users//rebeca.modrego//Desktop//API//Renewal_Q25_Extension_Permanency_Installments.json', 'r+')
            file_input=file.read()

            #Transformar fichero en formato JSON
            json_file=json.loads(file_input)

            #json.dumps(json_file, ch_q25_discount=discount, ch_installment_contract_id=PAYTERM, ch_permanent_contract_id=TERM)
            oldCustAcc=jsonpath.jsonpath(json_file, 'data.relationships.customer-account.data.id')
            oldBillAcc=jsonpath.jsonpath(json_file, 'included[0].relationships.billing-account.data.id')
            oldSubsId=jsonpath.jsonpath(json_file, 'data.attributes.parent-agreement-id')
            oldPAYTERM=jsonpath.jsonpath(json_file,'included[3].attributes.inputted-characteristics.CH_Installment_Contract_ID')
            oldDisc=jsonpath.jsonpath(json_file,'included[3].attributes.inputted-characteristics.CH_Q25_Discount')
            oldTERM=jsonpath.jsonpath(json_file, 'included[3].attributes.inputted-characteristics.CH_Permanent_Contract_ID')

            #print (oldBillAcc[0])
            file_input=file_input.replace(oldCustAcc[0],newcustAcc)
            file_input=file_input.replace(oldBillAcc[0],newbillingAcc)
            file_input=file_input.replace(oldSubsId[0],str(newSubscriptionId))
            file_input=file_input.replace(oldDisc[0], str(discount))
            file_input = file_input.replace(oldPAYTERM[0], str(PAYTERM))
            file_input = file_input.replace(oldTERM[0], str(TERM))

            json_file1 = json.loads(file_input)
            response = requests.post(url2, headers=headers, json=json_file1)

            print(response.content)
            content=response.content
            statuscode=response.status_code
            #print(response.status_code)
            return (content, statuscode)