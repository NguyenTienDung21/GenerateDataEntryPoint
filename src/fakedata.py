import json
from copy import deepcopy

with open('data/samples/single/sample1.json') as f:
    data = json.load(f)
    Edges = data["edges"]
    newEdges = []
    newData = dict()
    for edge, idx in zip(Edges, range(len(Edges))) :
        newEdge = deepcopy(edge)
        newEdge['id'] = idx
        newEdges.append(newEdge)
    newData["paths"] = deepcopy(data["paths"])
    newData["nodes"] = deepcopy(data["nodes"])
    newData["edges"] = newEdges
    with open('fakedata.json', 'w') as f:
        json.dump(newData, f)

