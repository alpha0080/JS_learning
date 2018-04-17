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
          #  print "i",i
<<<<<<< HEAD
          #  print "ox",ox
          #  print "oy",oy
          #  print "oz",oz
          #  print "child",child
          #  print "length",length
=======
         #   print "ox",ox
          #  print "oy",oy
         #   print "oz",oz
          #  print "child",child
         #   print "length",length
>>>>>>> origin/master
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



def getAllSlots(boneList):
   # print boneList
    slotList = []
    for i in boneList:
        boneName = i["name"]
        itemList = cmds.listRelatives(boneName,c=True)
        for j in itemList:
           # print j , cmds.nodeType(j)
            if cmds.nodeType(j) == "transform" :
                parentBone = cmds.listRelatives(j,p=True)[0]
                getObj =  cmds.ls(j,dag=1)[1]
                shadingGrps = cmds.listConnections(getObj,type='shadingEngine')
                shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
                fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')
                currentFile = cmds.getAttr("%s.fileTextureName" % fileNode[0])
                fileInSlot = currentFile.split("/")[-1].split(".png")[0]
                print "fileInSlot",fileInSlot
                #print j , cmds.listRelatives(j,p=True)[0]
                print "%s.blendMode" % fileNode[0]
                try:
                    blendMode = cmds.getAttr("%s.blendMode" % fileNode[0])
                    
                    print blendMode
                except:
                    blendMode = "normal"
                slotList.append({"name":j,
                                 "bone":parentBone,
                                 "color":"ffffffff",
                                 "attachment":fileInSlot,
                                 "blend":blendMode})  #additive
    return slotList
    
    
    
 
 
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

<<<<<<< HEAD
def getUVData(meshName,borderEdges):
=======

def getUVData(meshName,joinName,borderEdges):
>>>>>>> origin/master
    uvCount = cmds.polyEvaluate(meshName,uv=True)
    uvCoordDict ={}
    for i in range(0,uvCount):
        uvCoord = cmds.polyEditUV("%s.map[%s]"%(meshName,i),q=True)
   
        uvCoordDict.update({i:uvCoord})
    triangleVertexDict = {} 
    faceCount = cmds.polyEvaluate(meshName,f=True)
    for i in range(0,faceCount):
        toVertex = cmds.polyListComponentConversion("%s.f[%s]"%(meshName,i),tv=True,)
        cmds.select(toVertex)
        faceRefVertex = cmds.ls(sl=True,fl=True)
        triangleVertexDict.update({i:faceRefVertex})
    cmds.select(cl=True)

    edgeCount = cmds.polyEvaluate(meshName,e=True)
<<<<<<< HEAD
 
    border = cmds.polyListComponentConversion(cmds.ls(sl=True,fl=True),uvs=True)

    cmds.select(cl=True)
    
    uvCoordListForSpine = []
    for i in uvCoordDict.keys():
     #   print i
        uvCoordListForSpine.append(uvCoordDict[i][0])
        uvCoordListForSpine.append(uvCoordDict[i][1])
   # print "uvCoordListForSpine",uvCoordListForSpine

    trianglesListForSpine = []
    for i in triangleVertexDict.keys():
        trianglesListForSpine.append(int(triangleVertexDict[i][0].split("[")[1].split("]")[0]))
        trianglesListForSpine.append(int(triangleVertexDict[i][1].split("[")[1].split("]")[0]))
        trianglesListForSpine.append(int(triangleVertexDict[i][2].split("[")[1].split("]")[0]))
        
   # print "trianglesListForSpine",trianglesListForSpine

    allvertexs = cmds.polyListComponentConversion(meshName,tv=True)
    #vertexList = []
    cmds.select(allvertexs)
    vertexList = cmds.ls(sl=True,fl=True)
    cmds.select(cl=True)
  #  print vertexList
    vertexPositionForSpine= []
    for i in vertexList:
     #   print cmds.pointPosition(i)
        vertexPositionForSpine.append(cmds.pointPosition(i)[0])
        vertexPositionForSpine.append(cmds.pointPosition(i)[1])
        
   # print "vertexPositionForSpin",vertexPositionForSpine

   # borderEdgesString = cmds.getAttr("%s.borderList"%meshName)
   # borderEdges = borderEdgesString.split(",")
    borderEdgesCount = len(borderEdges)
    
    edgesVertexDict = {}
    for i in range(0,borderEdgesCount):
        toVertex = cmds.polyListComponentConversion(borderEdges[i],tv=True,)
        cmds.select(toVertex)
        edgeRefVertex = cmds.ls(sl=True,fl=True)
        edgesVertexDict.update({i:edgeRefVertex})

    edgesVertexForSpineList = []
    for i in edgesVertexDict.keys():
        v1 = edgesVertexDict[i][0].split("[")[-1].split("]")[0]
        v2 = edgesVertexDict[i][1].split("[")[-1].split("]")[0]

        edgesVertexForSpineList.append(int(v1)*2)
        edgesVertexForSpineList.append(int(v2)*2)
    #print "edgesVertexForSpineList",edgesVertexForSpineList
    
    dataForSpine = {"uvs":uvCoordListForSpine,"triangles":trianglesListForSpine,
                    "vertices":vertexPositionForSpine,"hull":borderEdgesCount,
                    "edges":edgesVertexForSpineList}

    return dataForSpine

=======
>>>>>>> origin/master
 
    border = cmds.polyListComponentConversion(cmds.ls(sl=True,fl=True),uvs=True)

    cmds.select(cl=True)
    
    uvCoordListForSpine = []
    for i in uvCoordDict.keys():
     #   print i
        uvCoordListForSpine.append(uvCoordDict[i][0])
        uvCoordListForSpine.append(uvCoordDict[i][1])
   # print "uvCoordListForSpine",uvCoordListForSpine

    trianglesListForSpine = []
    for i in triangleVertexDict.keys():
        trianglesListForSpine.append(int(triangleVertexDict[i][0].split("[")[1].split("]")[0]))
        trianglesListForSpine.append(int(triangleVertexDict[i][1].split("[")[1].split("]")[0]))
        trianglesListForSpine.append(int(triangleVertexDict[i][2].split("[")[1].split("]")[0]))
        
   # print "trianglesListForSpine",trianglesListForSpine

    allvertexs = cmds.polyListComponentConversion(meshName,tv=True)
    #vertexList = []
    cmds.select(allvertexs)
    vertexList = cmds.ls(sl=True,fl=True)
    cmds.select(cl=True)
    ox = cmds.getAttr("%s.translateX"%joinName)
    oy = cmds.getAttr("%s.translateY"%joinName)
    print ox,oy

  #  print vertexList
    vertexPositionForSpine= []
    for i in vertexList:
     #   print cmds.pointPosition(i)
        vertexPositionForSpine.append(cmds.pointPosition(i)[0]-ox)
        vertexPositionForSpine.append(cmds.pointPosition(i)[1]-oy)
        
   # print "vertexPositionForSpin",vertexPositionForSpine

   # borderEdgesString = cmds.getAttr("%s.borderList"%meshName)
   # borderEdges = borderEdgesString.split(",")
    borderEdgesCount = len(borderEdges)
    
    edgesVertexDict = {}
    for i in range(0,borderEdgesCount):
        toVertex = cmds.polyListComponentConversion(borderEdges[i],tv=True,)
        cmds.select(toVertex)
        edgeRefVertex = cmds.ls(sl=True,fl=True)
        edgesVertexDict.update({i:edgeRefVertex})

    edgesVertexForSpineList = []
    for i in edgesVertexDict.keys():
        v1 = edgesVertexDict[i][0].split("[")[-1].split("]")[0]
        v2 = edgesVertexDict[i][1].split("[")[-1].split("]")[0]

        edgesVertexForSpineList.append(int(v1)*2)
        edgesVertexForSpineList.append(int(v2)*2)
    #print "edgesVertexForSpineList",edgesVertexForSpineList
    width = cmds.getAttr("%s.scaleX"%meshName)
    height = cmds.getAttr("%s.scaleZ"%meshName)

    dataForSpine = {"type":"mesh",
                    "width":width,
                    "height":height,
                    "uvs":uvCoordListForSpine,"triangles":trianglesListForSpine,
                    "vertices":vertexPositionForSpine,"hull":borderEdgesCount,
                    "edges":edgesVertexForSpineList}

    return dataForSpine

def getAllSlots(boneList):
    slotList = []
    for i in boneList:
        boneName = i["name"]
       # print i
       # print boneName
    
        itemList = cmds.listRelatives(boneName,c=True)
      #  print itemList
        for j in itemList:
           # print j , cmds.nodeType(j)
            if cmds.nodeType(j) == "transform" :
                parentBone = cmds.listRelatives(j,p=True)[0]
                getObj =  cmds.ls(j,dag=1)[1]
                shadingGrps = cmds.listConnections(getObj,type='shadingEngine')
                shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
                fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')
                currentFile = cmds.getAttr("%s.fileTextureName" % fileNode[0])
                fileInSlot = currentFile.split("/")[-1].split(".png")[0]
              #  print "fileInSlot",fileInSlot
                #print j , cmds.listRelatives(j,p=True)[0]
              #  print "%s.blendMode" % fileNode[0]
                try:
                    blendMode = cmds.getAttr("%s.blendMode" % fileNode[0])
                    
                #    print blendMode
                except:
                    blendMode = "normal"
                slotList.append({"name":j,
                                 "bone":parentBone,
                                 "color":"ffffffff",
                                 "attachment":fileInSlot,
                                 "blend":blendMode})  #additive
    return slotList
    
    
def getSkinsList(slotList):
    skinList= {"default":{}}
    for i in slotList:
        slotName = i["name"]
        joinName = i["bone"]
        attachment = i["attachment"]
        #print "slotName",slotName
        type = cmds.getAttr("%s.meshType"%slotName)
        if type == "mesh" :
            boneList = getMeshData(slotName)
            getSlotSkinData = getUVData(slotName,joinName,boneList)
           # getSlotSkinData.update({})
            slotSkinData = { slotName:{attachment:getSlotSkinData}}
            #print 'getSlotSkinData',getSlotSkinData
           # print 'slotSkinData',slotSkinData
            skinList["default"].update(slotSkinData)
        '''
        "slotName": {
			"attachementName": {
				"type": "mesh",
                "uvs": [],
                "triangles": [],
                "vertices": [],
                "hull":"",
                "edges": [],
                "width":"",
                "height":""
                }
        '''
    return skinList
def getSkinsListB(slotList):
    skinList= {"default":{}}
    
   # print "slotList",slotList
   # print "slotListLength",len(slotList)
        
    for i in slotList:
        slotName = i["name"]
        #print "slotName",slotName
        getObj =  cmds.ls(slotName,dag=1)[1]
        shadingGrps = cmds.listConnections(getObj,type='shadingEngine')
        shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
        fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')[0]
        currentFile = cmds.getAttr("%s.fileTextureName" % fileNode)
        fileInSlot = currentFile.split("/")[-1].split(".png")[0]
        attachmentImage =fileInSlot
        width = int(cmds.getAttr( "%s.scaleX"%slotName))
        height = int(cmds.getAttr( "%s.scaleZ"%slotName))
        x = int(cmds.getAttr( "%s.translateX"%slotName))
        y = int(cmds.getAttr( "%s.translateY"%slotName))
       # print "slotList",slotList
       # print "fileNode",fileNode
        if cmds.getAttr("%s.useFrameExtension"%fileNode) == True:
            fileName = cmds.getAttr("%s.fileTextureName"%fileNode).split("/")[-1]
            fileDir = cmds.getAttr("%s.fileTextureName"%fileNode).split(fileName)[0]
            
            allFiles = os.listdir(fileDir)
            sequenceList = []
            for j in allFiles:
               # print i.split(".")
                if j.split(".")[0] == fileName.split(".")[0]:
                    sequenceList.append(j)
                    
          #  print "sequenceList",sequenceList

              #  print width,height
            sequenceFrameInfoDict = {}
            for index in range(0,len(sequenceList)):
               # print sequenceList[index]
                sequenceFrameInfoDict.update({sequenceList[index].split(".png")[0]:{ "width": width, 
                                                                     "height": height,
                                                                     "x":x,
                                                                     "y":y }})
          #  print "sequenceFrameInfoDict",sequenceFrameInfoDict,type(sequenceFrameInfoDict)
                
            

            skinList["default"].update({slotName:sequenceFrameInfoDict})
                
                  
        else:


              #  print width,height
                

            skinList["default"].update({slotName:{	attachmentImage: { "width": width, 
                                                                     "height": height,
                                                                     "x":x,
                                                                     "y":y }}})
    return skinList
            
                
    
    
def exportSpineDefineJson(exportFileName,boneList):
    spineJson = {
                "bones": boneList,
                "animations": {}
                }
     
    writeData = json.dumps(spineJson, sort_keys=True , indent =4) 
    #writeData = json.dumps(exportJson) 
    with open(exportFileName, 'w') as the_file:
        the_file.write(writeData)     
               
 
 
def getExportJson(fileName,boneList,slotList,skinList):
    exportFileName =fileName# "//mcd-server/webServer/spineTest/effectB/effectB_01.json"
   # exportFileName = "C:/Users/alpha/Documents/GitHub/JS_learning/spineTest/spineJsonTest_02.json"

    exportDict = {}
    exportDict.update({"bones":boneList})
    exportDict.update({"slots":slotList})
    exportDict.update({"skins":skinList})
   # exportDict.update({"animations":animationList})


    #print ecportJson
    writeData = json.dumps(exportDict, sort_keys=True , indent =4) 
    #writeData = json.dumps(exportJson) 
    with open(exportFileName, 'w') as the_file:
        the_file.write(writeData)
  #  return exportDict               
               
    
def run():
    exportFileName =  "C:/alphaOnly/github/JS_learning/spineTest/skeletonTest/uvSkinTest.json"
    boneList = defineBone("joint6")
    slotList = getAllSlots(boneList)
    skinList = getSkinsList(slotList)
    getExportJson(exportFileName,boneList,slotList,skinList)
    print "boneList",boneList
    print "slotList",slotList
    print "skinList",skinList
    
    #getUVData(meshName,borderEdges)
    
    
<<<<<<< HEAD
#run()
def runB(meshName , boneRoot):
    borderEdge = getMeshData(meshName)
    boneList = defineBone(boneRoot)
    print getAllSlots(boneList)

   # cmds.select(borderEdge)
    
   # print getUVData(meshName,borderEdge)
    #print boneList
=======


def runB(meshName):
    
    boneList = getMeshData(meshName)
    dataForSpine = getUVData(meshName,boneList)
    
    print dataForSpine
#print getMeshData("polySurface1")
#cmds.select(getMeshData("polySurface3"))
>>>>>>> origin/master
#getSlotData("joint1")

runB("polySurface1","joint9")
    
    
#runB("polySurface1")


run()









