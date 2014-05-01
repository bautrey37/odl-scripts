import json
import httplib2

#Uses the FlowProgrammer API for the ODL Controller to delete all the flows on the controller

baseUrl = 'http://10.190.94.120:8080/controller/nb/v2'
containerName = 'default'
service = 'flowprogrammer'

h = httplib2.Http(".cache")
h.add_credentials('admin', 'admin')


def build_url(baseUrl, service, containerName):
    postUrl = '/'.join([baseUrl, service, containerName])
    return postUrl

def build_flow_url(baseUrl, service, containerName, switchType, switchId, flowName):
    postUrl = build_url(baseUrl, service, containerName) + '/'.join(['', 'node', switchType, switchId, 'staticFlow', flowName])
    return postUrl


# Get all the flows
resp, content = h.request(build_url(baseUrl, service, containerName), "GET")
flowsList = json.loads(content)
odlFlowConfigs = flowsList['flowConfig']

# Now go and delete them all
for flow in odlFlowConfigs:
    nodeType = flow['node']['type']
    nodeId = flow['node']['id']
    name = flow['name']
    deleteUrl = build_flow_url(baseUrl, service , containerName, nodeType, nodeId, name)
    resp, content = h.request(deleteUrl, "DELETE")

    if resp.status == 204:
        print 'Flow Config deleted successfully!'
    else:
        print resp.status

