import json
import random
import copy
import republican
import cars

"""
There are 2 datasets you will be using in this assignment.
republican.trainingData
republican.testingData

cars.trainingData
cars.testingData

The datasets are an array of json-formatted objects.  Where each object has key-value pairs where they key is the attribute name and the value is 0 or 1.
For example,
data = [{"a": 0, "b":0, "c": 0},{"a": 0, "b":1, "c": 1}]
or
data = [{"a": 1, "b":0, "c": 0},{"a": 1, "b":1, "c": 1},{"a": 0, "b":1, "c": 0},{"a": 0, "b":0, "c": 1}]

You can access elements of data like this:
>>> data[1] 
{"a": 1, "b":1, "c": 1}

>>> data[1]["c"]
1
"""

#-------------------- Leave these functions alone! -------------------------  
def createNode(label):
    obj = {}
    obj["data"] = label
    obj["attr"] = {}
    obj["attr"]["rel"] = "folder"
    obj["attr"]["state"] = "open"
    obj["attr"]["id"] = label
    obj["children"] = []
    return obj   

def createLeaf(label):
    obj = {}
    obj["data"] = label
    obj["attr"] = {}
    obj["attr"]["rel"] = "file"
    obj["attr"]["state"] = "open"
    obj["attr"]["id"] = label
    obj["children"] = []
    return obj 
    
def writeHierarchyToJSFile(tree, filename):
    jsonstr =  "var tree = " + json.dumps(tree)
    f = open(filename, 'w')
    f.write(jsonstr)
    f.close()
    
def writeDataToPYFile(data, fileName):
    jsonstr =  "data = " + json.dumps(data)
    f = open(fileName, 'w')
    f.write(jsonstr)
    f.close()  

#-------------------- These functions are referenced in the homework -------------------------    
"""
#Step 2

tree = id3(republican.trainingData1, "republican", ["salary more than $100,000", "owns your own business","listenes to NPR","owns a truck","lives in a red state","watches The Daily Show"])
writeHierarchyToJSFile(tree, 'www/decisionTree.js')

def generateDataPartA(n):
    data = []
    for i in range(n):
        datapoint = {}
        
        datapoint["salary more than $100,000"] = 1 if random.random() > .5 else 0    
        datapoint["owns your own business"] = 1 if random.random() > .5 else 0  
        datapoint["listenes to NPR"] = 1 if random.random() > .5 else 0 
        datapoint["owns a truck"] = 1 if random.random() > .5 else 0  
        datapoint["lives in a red state"] = 1 if random.random() > .5 else 0  
        datapoint["watches The Daily Show"] = 1 if random.random() > .5 else 
        
        if datapoint["salary more than $100,000"] == 1:
            datapoint["republican"] = 1 
        else:
            datapoint["republican"] = 0 
        data.append(datapoint)

    return data
    
def generateDataPartB(n):
    data = []
    for i in range(n):
        datapoint = {}
                
        datapoint["salary more than $100,000"] = 1 if random.random() > .5 else 0    
        datapoint["owns your own business"] = 1 if random.random() > .5 else 0  
        datapoint["listenes to NPR"] = 1 if random.random() > .5 else 0 
        datapoint["owns a truck"] = 1 if random.random() > .5 else 0  
        datapoint["lives in a red state"] = 1 if random.random() > .5 else 0  
        datapoint["watches The Daily Show"] = 1 if random.random() > .5 else 
        
        if datapoint["salary more than $100,000"] == 1:
            datapoint["republican"] = 1 if random.random() > .05 else 0 
        else:
            datapoint["republican"] = 0 if random.random() > .05 else 1
        data.append(datapoint)

    return data
    
#Step 4

tree1 = id3(cars.trainingData,"acceptable", ["new paint job","many previous owners","recent oil change","has vanity plate","very high price","high price","mid price","low price","very high maintainance","high maintainance","mid maintainance","low maintainance","2 doors","3 doors","4 doors","5+ doors","2 passengers","4 passengers","more passengers","small boot","med boot","large boot"])   
tree2 = id3(cars.trainingData,"acceptable", ["very high price","high price","mid price","low price","very high maintainance","high maintainance","mid maintainance","low maintainance","2 doors","3 doors","4 doors","5+ doors","2 passengers","4 passengers","more passengers","small boot","med boot","large boot"])    
tree3 = id3(cars.trainingData,"acceptable", ["high safety","med safety","low safety","very high price","high price","mid price","low price","very high maintainance","high maintainance","mid maintainance","low maintainance","2 doors","3 doors","4 doors","5+ doors","2 passengers","4 passengers","more passengers","small boot","med boot","large boot"])
""" 
    
#-------------------- Fill in these functions -------------------------    
def id3(examples, targetAttribute, attributes, pruningCutOff):
    # node = createNode("foo")
    return node
    
def findBestAttribute(examples, targetAttribute, attributes):        
    return None
            
def calcChiSquared(C1, C2, targetAttribute):    
    return None

def evaluteTreeOnTrainingdata(tree, data, targetAttribute):
    return None

def getClassification(tree, datapoint):
    return None 
 
 
 
#-------------------- Run This Code -------------------------  

#create an example tree
#print it to a file
#open the file decisionTree.html in a web browser, perferrably one that isn't evil.  
  
tree = createNode("First Attribute to split on")
node1 = createNode("False")
node2 = createNode("True")
tree["children"].append(node1)
tree["children"].append(node2)

leaf1 = createLeaf("+")
leaf2 = createLeaf("-")

node1["children"].append("+")
node2["children"].append("- you can also add arbitrary text here!")  

writeHierarchyToJSFile(tree, 'www/decisionTree.js')  