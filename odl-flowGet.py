import httplib2
import json
import os

url = "http://10.190.94.120:8080/controller/nb/v2"
container = "default"

def write_file(name, content):
    dir_path = "./odl-flow-configs/"
    file_name = name + ".txt"
    path = os.path.join(os.path.dirname(dir_path), file_name)
    print path
    f = open(path, "w")
    f.write(json.dumps(content, indent=2))
    print "Wrote to file"
    f.close()

# Writes the contents of the ODL Statistics
def statistics_get():
    resp, content = h.request(url + '/statistics/' + container + '/flow', "GET")
    allFlowStats = json.loads(content)
    #print json.dumps(allFlowStats, indent=2)
    flowStats = allFlowStats['flowStatistics']
    #print json.dumps(flowStats, indent=2)
    write_file("statistics_1", flowStats)

# Writes the contents of the ODL FlowProgrammer
# Contains a list of flows configured on the container
def flowProgrammer_get():
    resp, content = h.request(url + '/flowprogrammer/' + container, "GET")
    allFlowStats = json.loads(content)
    #print json.dumps(allFlowStats, indent=2)
    write_file("flowConfig_1", allFlowStats)

h = httplib2.Http(".cache")
h.add_credentials('admin', 'admin')

#statistics_get()
flowProgrammer_get()

