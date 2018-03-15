import json
from pprint import pprint

file = "C:/alphaOnly/github/JS_learning/json/effect_a_glow_ray.json"
exportFile = "C:/alphaOnly/github/JS_learning/json/effect_a_glow_ray_min.json"
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
        baseData = {}
        newDictData.update({i:{}})
       # print originalData[i]["pivot_w"]
        baseData.update({"pw":(originalData[i]["pivot_w"])})
        baseData.update({"ph":(originalData[i]["pivot_h"])})
        #baseData.append(originalData[i]["translate"]["index"])
       # baseData.append(originalData[i]["translate"]["vis"])
        #newDictData.update({i.split("_")[0]:{}})
        newDictData.update({i:{"base":baseData,"dt":{}}})
        
totalTime = len(originalData["pId_1"]["translate"])
timeList  = []

for i in  range(0,totalTime):
    
    #print originalData["pId_1"]["translate"][i]["time"]
    timeList.append(originalData["pId_1"]["translate"][i]["time"])
#ppIDcount = len(newDictData.keys())
for i in newDictData.keys():
    for j in range(0,totalTime):
        #originalData[i]["translate"][i]["time"]
        dtData = {}
        dtData.update({"x":(originalData[i]["translate"][j]["x"])})
        dtData.update({"y":(originalData[i]["translate"][j]["y"])})
        dtData.update({"t":(originalData[i]["translate"][j]["trans"])})
        dtData.update({"a":(originalData[i]["rotate"][j]["angle"])})
        dtData.update({"w":(originalData[i]["scale"][j]["w"])})
        dtData.update({"h":(originalData[i]["scale"][j]["h"])})
        newDictData[i]["dt"].update({originalData[i]["translate"][j]["time"]:dtData})
        
        
for i in newDictData.keys():   
    #print originalData[i]["translate"][0]["index"]
  #  print originalData[i]["translate"][0]["vis"]
    newDictData[i]["base"].update({"i":(originalData[i]["translate"][0]["index"])})
    newDictData[i]["base"].update({"v":(originalData[i]["translate"][0]["vis"])})
    
    
    
instancerKeys = originalData["instancer"].keys() 

for i in instancerKeys:
    
    print i
    base ={}
    base.update({"bw":(originalData["instancer"][i]["bbox_w"])})
    base.update({"bh":(originalData["instancer"][i]["bbox_h"])})
    base.update({"pw":(originalData["instancer"][i]["pivot_w"])})
    base.update({"ph":(originalData["instancer"][i]["pivot_h"])})
    base.update({"of":(originalData["instancer"][i]["offset"])})

    newDictData.update({i:{"base":base,"dt":{}}})    
    
    
    
for i in instancerKeys:
    for j in range(0,totalTime):
        #originalData[i]["translate"][i]["time"]
        dtData = {}
        dtData.update({"x":(originalData["instancer"][i]["translate"][j]["x"])})
        dtData.update({"y":(originalData["instancer"][i]["translate"][j]["y"])})
        dtData.update({"t":(originalData["instancer"][i]["translate"][j]["trans"])})
        dtData.update({"a":(originalData["instancer"][i]["rotate"][j]["angle"])})
        dtData.update({"w":(originalData["instancer"][i]["scale"][j]["w"])})
        dtData.update({"h":(originalData["instancer"][i]["scale"][j]["h"])})
        newDictData[i]["dt"].update({originalData["instancer"][i]["translate"][j]["time"]:dtData})
            
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
        

    