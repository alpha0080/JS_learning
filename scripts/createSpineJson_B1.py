import maya.cmds as cmds
import json

def getAllbones(rootJoint):
    boneList = []

    for i in cmds.ls(rootJoint,dag =2):
        if cmds.nodeType(i) =="joint":
            boneList.append(i)
    
    print boneList

    allBoneList = cmds.ls(type="joint" ,l =True)
    for i in allBoneList:
        boneShotName =  i.split("|")[-1]
        boneParent = cmds.listRelatives(boneShotName,p=True)
        
       # print boneShotName,boneParent
        boneDict = {"name":boneShotName,
                    "parent":boneParent,
                    "rotation":0,
                    "x": 0,
                    "y":0,
                    "scaleX":1,
                    "scaleY":1
                    }
        boneList.append(boneDict)
        
    return boneList
	#{ "name": "left-wing", "parent": "token-root", "length": 50, "rotation": 156.83, "x": -91.06, "y": 7.8 },

    #return allBoneList
    
    
def getAllSlots(boneList):
    slotList = []
    for i in boneList:
        boneName = i["name"]
        itemList = cmds.listRelatives(boneName,c=True)
        for j in itemList:
           # print j , cmds.nodeType(j)
            if cmds.nodeType(j) == "transform" :
                parentBone = cmds.listRelatives(j,p=True)[0]
                print j , cmds.listRelatives(j,p=True)[0]
                slotList.append({"name":j,
                                 "bone":parentBone,
                                 "color":"ffffffff",
                                 "attachment":"fileNode",
                                 "blend":"normal"})
    return slotList
    	#{ "name": "star2", "bone": "star2", "color": "ffffff00", "attachment": "star", "blend": "additive" },

    
def run():
    
    boneList = getAllbones()
    print getAllSlots(boneList),len(boneList)
    
def runB():
    rootName = "rootA"
    getAllbones(rootName)
    
    
#run()

runB()


