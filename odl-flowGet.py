import httplib2
import json
import os

def write_flows(name, content):
    dir_path = "./odl-flow-configs/"
    file_name = name + ".txt"
    path = os.path.join(os.path.dirname(dir_path), file_name)
    print path
    f = open(path, "w")
    f.write(json.dumps(content, indent=2))
    print "Wrote to file"
    f.close()


h = httplib2.Http(".cache")
h.add_credentials('admin', 'admin')
resp, content = h.request('http://10.190.94.120:8080/controller/nb/v2/statistics/default/flow', "GET")
allFlowStats = json.loads(content)
flowStats = allFlowStats['flowStatistics']
#print json.dumps(flowStats, indent=2)
write_flows("test_config1", flowStats)


