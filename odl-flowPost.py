import requests
import json
import os

dir_path = "./odl-flow-configs/"
file_name = "setup1.txt"
path = os.path.join(os.path.dirname(dir_path), file_name)
f = open(path, "rb")
payload = json.load(f)
print payload

headers = {'content-type': 'application/json'}
baseUrl = "http://10.190.94.120:8080/controller/nb/v2"

# Will need to use the FlowProgrammer API to set flows.
# Will need to parse statistics file and upload flows one at a time
#r = requests.post(baseUrl + "/statistics/default/flow", auth=('admin', 'admin'), data=payload, headers=headers)

r = requests.get(baseUrl + "/statistics/default/flow", auth=('admin', 'admin'))

print "Headers: ", r.headers
print "Text: " + r.text
print "Status: ", r.status_code
print "File posted: " + path

