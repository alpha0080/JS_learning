import json
from pprint import pprint

file = "C:/alphaOnly/github/JS_learning/json/effect_a_dot.json"
exportFile = "C:/alphaOnly/github/JS_learning/json/effect_a_dot_min.json"
with open(file) as data_file:    
    data = json.load(data_file)
    
    
originalData = data

"""
"pID_1":{"base":[pw,ph,imageIndex,vis],
         "dTime":{1:[x,y,trans,angle,h,w]}}
"""


#print originalData.keys()
newDictData = {}
for i in originalData.keys():
  #print i.split("_")
    if i.split("_")[0] == "pId" :
        print i
        baseData = [];
        newDictData.update({i:{}})
       # print originalData[i]["pivot_w"]
        baseData.append(originalData[i]["pivot_w"])
        baseData.append(originalData[i]["pivot_h"])
        #baseData.append(originalData[i]["translate"]["index"])
       # baseData.append(originalData[i]["translate"]["vis"])
        #newDictData.update({i.split("_")[0]:{}})
        newDictData.update({i:{"base":baseData,"dt":[]}})
        
totalTime = len(originalData["pId_1"]["translate"])
timeList  = []

for i in  range(0,totalTime):
    
    #print originalData["pId_1"]["translate"][i]["time"]
    timeList.append(originalData["pId_1"]["translate"][i]["time"])
#ppIDcount = len(newDictData.keys())
for i in newDictData.keys():
    for j in range(0,totalTime):
        #originalData[i]["translate"][i]["time"]
        dtData = []
        dtData.append(originalData[i]["translate"][j]["x"])
        dtData.append(originalData[i]["translate"][j]["y"])
        dtData.append(originalData[i]["translate"][j]["trans"])
        dtData.append(originalData[i]["rotate"][j]["angle"])
        dtData.append(originalData[i]["scale"][j]["w"])
        dtData.append(originalData[i]["scale"][j]["h"])
        newDictData[i]["dt"].append({originalData[i]["translate"][j]["time"]:dtData})
        
        
for i in newDictData.keys():   
    #print originalData[i]["translate"][0]["index"]
  #  print originalData[i]["translate"][0]["vis"]
    newDictData[i]["base"].append(originalData[i]["translate"][0]["index"])
    newDictData[i]["base"].append(originalData[i]["translate"][0]["vis"])
    
    
    
instancerKeys = originalData["instancer"].keys() 

for i in instancerKeys:
    
    print i
    base =[]
    base.append(originalData["instancer"][i]["bbox_w"])
    base.append(originalData["instancer"][i]["bbox_h"])
    base.append(originalData["instancer"][i]["pivot_w"])
    base.append(originalData["instancer"][i]["pivot_h"])
    base.append(originalData["instancer"][i]["offset"])

    newDictData.update({i:{"base":base,"dt":[]}})    
    
    
    
for i in instancerKeys:
    for j in range(0,totalTime):
        #originalData[i]["translate"][i]["time"]
        dtData = []
        dtData.append(originalData["instancer"][i]["translate"][j]["x"])
        dtData.append(originalData["instancer"][i]["translate"][j]["y"])
        dtData.append(originalData["instancer"][i]["translate"][j]["trans"])
        dtData.append(originalData["instancer"][i]["rotate"][j]["angle"])
        dtData.append(originalData["instancer"][i]["scale"][j]["w"])
        dtData.append(originalData["instancer"][i]["scale"][j]["h"])
        newDictData[i]["dt"].append({originalData["instancer"][i]["translate"][j]["time"]:dtData})
            
newDictData.update({"metaData":originalData["metaData"]})
#for i in range(0,totalTime):
#    print i

writeData = json.dumps(newDictData) 
#writeData = json.dumps(newDictData, sort_keys=True , indent =4) 
#writeData = json.dumps(newDictData, sort_keys=True , indent =4) 

#print timeList       
#print len(originalData["pId_1"]["translate"])
        
#print newDictData
type(newDictData)
with open(exportFile, 'w') as the_file:
    the_file.write(writeData)
        

    