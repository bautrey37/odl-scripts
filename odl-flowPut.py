import requests
import json
import os
import httplib2

# Re-Programs the flows from the FlowConfig file pulled from controller using FlowProgrammer API

h = httplib2.Http(".cache")
h.add_credentials('admin', 'admin')

baseUrl = 'http://10.190.94.120:8080/controller/nb/v2'
containerName = 'default'
service = 'flowprogrammer'
headers = {'content-type': 'application/json'}

def build_flow_url(baseUrl, service, containerName, switchType, switchId, flowName):
    postUrl = '/'.join([baseUrl, service, containerName, 'node', switchType, switchId, 'staticFlow', flowName])
    print postUrl
    return postUrl

def status_codes(code):
    if code == 201:
        print "Flow Config processed successfully"
        print "File posted: " + path + '\n'
    elif code == 200:
        print "Static Flow modified successfully"
        print "File posted: " + path + '\n'
    else:
        print "An error has occurred"
        print "Status: ", code

# file to program
dir_path = "./odl-flow-configs/"
file_name = "flowConfig_1.txt"
path = os.path.join(os.path.dirname(dir_path), file_name)
f = open(path, "rb")
flowsList = json.load(f)
#print json.dumps(flowsList, indent=2)

odlFlowConfigs = flowsList['flowConfig']
#print json.dumps(odlFlowConfigs, indent=2)

##Example Flow from API
#{"installInHw":"true","name":"flow1","node":{"id":"00:00:00:00:00:00:00:01","type":"OF"},"ingressPort":"1","priority":"500","etherType":"0x800","nwSrc":"9.9.1.1","actions":["OUTPUT=2"]}

for flow in odlFlowConfigs:
    switchType = flow['node']['type']
    switchId = flow['node']['id']
    name = flow['name']
    print json.dumps(flow, indent=2)

    # PUT is used to put a file onto a webpage.  Do not use POST
    r = requests.put(build_flow_url(baseUrl, service, containerName, switchType, switchId, name), auth=('admin', 'admin'), data=json.dumps(flow), headers=headers)
    status_codes(r.status_code)


