## rigging mode

'''
{
"bones": [
	{ "name": "root" },
	{ "name": "bone", "parent": "root", "length": 300 },
	{ "name": "bone2", "parent": "bone", "length": 200, "rotation": 40.31, "x": 300 }
],
"animations": {
	"animation": {}
}
}

print cmds.getAttr("joint4.)
'''
import maya.cmds as cmds
import json

def defineBone(root):
    
    boneList=[]
    allNode =  cmds.ls(root,dag=2)
    for i in allNode:
        if cmds.nodeType(i) == "joint":
          #  print i
            x = float("%.3f"%(cmds.getAttr("%s.translateX"%i)))
            y = float("%.3f"%(cmds.getAttr("%s.translateY"%i)))
            rz = float("%.3f"%(cmds.getAttr("%s.rotateZ"%i)))
            sx = float("%.3f"%(cmds.getAttr("%s.scaleX"%i)))
            sy = float("%.3f"%(cmds.getAttr("%s.scaleY"%i)))
            ox = float("%.3f"%(cmds.getAttr("%s.jointOrientX"%i)))
            oy = float("%.3f"%(cmds.getAttr("%s.jointOrientY"%i)))
            oz = float("%.3f"%(cmds.getAttr("%s.jointOrientZ"%i)))
            r  = oz+rz
            child = cmds.listRelatives(i,c=True)
            if child == None:
                length = 0
            else:
                length = cmds.getAttr("%s.translateX"%child[0])
            #length = cmds.getAttr("%s.translateX"%child)
            
            if cmds.listRelatives(i,p=True) == None:
                
                boneInfo = {"name":i,"rotation":r,"x":x,"y":y,"length":length,"color":"ffffffff"}
          #      print "It's root"
            else:
                parentBone = cmds.listRelatives(i,p=True)[0]
          #      print "bone,(joint):",i, "parent:",parentBone
                boneInfo = {"name":i,"parent":parentBone,"rotation":r,"x":x,"y":y,"length":length,"color":"ffffffff"}

          #  print "x",x
          #  print "y",y 
          #  print "r",r
          #  print "sx",sx
          #  print "sy",sy
          #  print boneInfo
            print "i",i
            print "ox",ox
            print "oy",oy
            print "oz",oz
            print "child",child
            print "length",length
            boneList.append(boneInfo)
    return boneList
            
                
     #       nodeName = cmds.listRelatives(i,p=True)[0]
           # print "bone,(joint):",i, "parent:",nodeName
         #   if cmds.nodeType(nodeName) == "joint":  #filter nodeType, joint
         #       print nodeName 

def getSlotData(boneName):
    
    for i in cmds.listConnections(boneName):
        print i,cmds.nodeType(i)
        print cmds.listConnections(i,d=True,type ="mesh")

 
#print cmds.listConnections("root_foot",d=True,type ="mesh")

def getMeshData(meshName):
    alledges = cmds.polyListComponentConversion(meshName,te=True)
    cmds.select(alledges)
    allEdgesList = cmds.ls(sl=True,fl=True)

    borderEdge = []
    for i in allEdgesList:
        toFace = cmds.select(cmds.polyListComponentConversion(i,tf=True))
        listFace = cmds.ls(sl=True,fl=True)
      #  print listFace
        if len(listFace )> 1:
            pass
        else:
            borderEdge.append(i)
    cmds.select(cl=True)

   # len(borderEdge)

   # cmds.select(borderEdge)

    return borderEdge

 
def exportSpineDefineJson(exportFileName,boneList):
    spineJson = {
                "bones": boneList,
                "animations": {}
                }
     
    writeData = json.dumps(spineJson, sort_keys=True , indent =4) 
    #writeData = json.dumps(exportJson) 
    with open(exportFileName, 'w') as the_file:
        the_file.write(writeData)     
               
               
               
    
def run():
    exportFileName =  "C:/Users/alpha/Documents/GitHub/JS_learning/spineTest/uvSkinTest.json"
    boneList = defineBone("joint9")
    
    exportSpineDefineJson(exportFileName,boneList)
    
#run()

print getMeshData("polySurface1")
#getSlotData("joint1")
    
    












