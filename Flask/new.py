import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "RChJejuRsWKPUeevfDmNv3Ho-HN9hlejkTGxGW9HIcEE"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": [['id', 'cycle', 'setting1', 'setting2', 'setting3', 's1', 's2', 's3',
       's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13', 's14',
       's15', 's16', 's17', 's18', 's19', 's20', 's21', 'ttf']], "values": [[1.00000000e+00, 1.00000000e+00, 4.59770115e-01, 1.66666667e-01,
       0.00000000e+00, 0.00000000e+00, 1.83734940e-01, 4.06801831e-01,
       3.09756921e-01, 0.00000000e+00, 1.00000000e+00, 7.26247987e-01,
       2.42424242e-01, 1.09755003e-01, 0.00000000e+00, 3.69047619e-01,
       6.33262260e-01, 2.05882353e-01, 1.99607803e-01, 3.63986149e-01,
       0.00000000e+00, 3.33333333e-01, 0.00000000e+00, 0.00000000e+00,
       7.13178295e-01, 7.24661696e-01, 1.91000000e+02]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/bdf48ff8-8f81-449d-bc6e-1cc1018af3b7/predictions?version=2021-10-28', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
pred = response_scoring.json()
print(pred)

if(pred == 1):
    print("Engine Failure")
else:
    print("No Engine Failure")