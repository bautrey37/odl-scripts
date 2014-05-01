import requests
import json
import os

# Re-Programs the flows from the FlowConfig file pulled from controller using FlowProgrammer API

baseUrl = 'http://10.190.94.120:8080/controller/nb/v2'
containerName = 'default'
service = 'flowprogrammer'
headers = {'content-type': 'application/json'}

def build_flow_url(baseUrl, service, containerName, switchType, switchId, flowName):
    postUrl = '/'.join([baseUrl, service, containerName, 'node', switchType, switchId, 'staticFlow', flowName])
    print postUrl
    return postUrl

# file to program
dir_path = "./odl-flow-configs/"
file_name = "flowConfig_1.txt"
path = os.path.join(os.path.dirname(dir_path), file_name)
f = open(path, "rb")
flowsList = json.load(f)
#print json.dumps(flowsList, indent=2)

odlFlowConfigs = flowsList['flowConfig']
print json.dumps(odlFlowConfigs, indent=2)

for flow in odlFlowConfigs:
    switchType = flow['node']['type']
    switchId = flow['node']['id']
    name = flow['name']
    #read in rest of configuration from file
    payload = ''
    r = requests.post(build_flow_url(baseUrl, service, containerName, switchType, switchId, name), auth=('admin', 'admin'), data=payload, headers=headers)

    print "Headers: ", r.headers
    print "Text: " + r.text
    print "Status: ", r.status_code
    print "File posted: " + path

