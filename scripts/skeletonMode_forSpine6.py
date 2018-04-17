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
import sys

sys.path.append("C:/Program Files/Pixar/RenderManProServer-21.5/lib/python2.7/Lib")
sys.path.append("C:/Program Files/Pixar/RenderManProServer-21.5/lib/python2.7/Lib/site-packages")

import ice


def getImageMetaData(fileNode):
    
    currentFile = cmds.getAttr("%s.fileTextureName" % fileNode)
    fileInSlot = currentFile.split("/")[-1].split(".png")[0]
    image = ice.Load(currentFile)
    imageMetaData = image.GetMetaData()
    imageSize = imageMetaData['Original Size']
    imageWidth = int(imageMetaData['Original Size'].split(" ")[0].split("(")[1])
    imageHeight = int(imageMetaData['Original Size'].split(" ")[1].split(")")[0])

    return currentFile,imageWidth,imageHeight



#print getImageMetaData("file1")






def getItemDepth(baseRoot):
    allNode =  cmds.ls(baseRoot,dag=2,l=True,typ ="joint")
    checkMaxDepth = []
    for i in allNode: #check joint depth
        if len(i.split("|")) in checkMaxDepth:
            pass
        else:
            checkMaxDepth.append(len(i.split("|")))
    depth =  sorted(checkMaxDepth)[-1]
   # return depth

    jointListByLevel = []
    for i in range(0,depth):
        for j in allNode:
            if len(j.split("|")) == i:
                if j.split("|")[-1] in jointListByLevel:
                    pass
                else:
                    jointListByLevel.append(j.split("|")[-1])
                
    return jointListByLevel
    
    
def defineBone(root):
    
    boneList=[]
    allNode =  getItemDepth(root)
    for i in allNode:
    #    print "i",i
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
         #   print "child",child
            if child == None:
                length = 0
            else:
                length = float("%.3f"%cmds.getAttr("%s.translateX"%child[0]))
               # print "length",length
                
            #length = cmds.getAttr("%s.translateX"%child)
         #   print length,type(length)
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
         #   print "ox",ox
          #  print "oy",oy
         #   print "oz",oz
          #  print "child",child
         #   print "length",length
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


def getUVData(meshName,joinName,borderEdges):
    
    getObj =  cmds.ls(meshName,dag=1)[1]
    print "meshName",meshName
    shadingGrps = cmds.listConnections(getObj ,type='shadingEngine')

    
    #shadingGrps = cmds.listConnections(meshName,type='shadingEngine')
    shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
    fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')[0]
    print fileNode
    imageWidth = getImageMetaData(fileNode)[1]
    imageHeight = getImageMetaData(fileNode)[1]


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
    width = imageWidth#cmds.getAttr("%s.scaleX"%meshName)
    height = imageHeight#cmds.getAttr#("%s.scaleZ"%meshName)

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
        print "itemList",boneName,itemList
        try:
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
        except:
            pass
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
    return skinList
  
  
def getAllkeyFrameList(nodeName,start,end):   
  #  print "nodeName",nodeName
    keyFrameList=[0.0,start,end]
    allKeyFrame = cmds.keyframe(nodeName,time=(start,end),query=True) 
   # print "allKeyFrame",allKeyFrame
    if allKeyFrame == None:
       # return keyFrameList
        pass
        
    else:
        
        for i in allKeyFrame:
            if i in keyFrameList:
                pass
            else:
                keyFrameList.append(i)
        
        keyFrameList =sorted(keyFrameList)
    return keyFrameList
        
    
#print getAllkeyFrameList("joint6",0,60)


def getAnimationList(slotList,boneList,fps,start,end,offsetRange,actionName):
    animationList = {}
    actionAnimation={actionName:{"slots":{},
                                 "bones":{}}}

    soltsAnimationDict= {}
    for slot in slotList:
        slotName = slot["name"]
        tempSlotDict = { slotName:{"color":[]}}
        soltsAnimationDict.update(tempSlotDict)
        getObj =  cmds.ls(slotName,dag=1)[1]
        shadingGrps = cmds.listConnections(getObj,type='shadingEngine')
        shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
        fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')[0]
        attachment = slot["attachment"]
        keyFrameList = getAllkeyFrameList(fileNode,start,end)
        
        for i in keyFrameList:
            if int(i) in range(start,end+1):
                cmds.currentTime(i,e=True)
                alphaGain = cmds.getAttr( "%s.alphaGain"%fileNode)
                colorGain = cmds.getAttr("%s.colorGain"%fileNode)[0]
                
                alphaGainHex = "%02x"%int((alphaGain/1)*255)
                colorGainHex = "%02x"%int((colorGain[0]/1)*255) + "%02x"%int((colorGain[1]/1)*255) +"%02x"%int((colorGain[2]/1)*255)
                exportColorHex = str(colorGainHex + alphaGainHex)
                soltsAnimationDict[slotName]["color"].append({"time": float(i)/fps, "color": exportColorHex })
            else:
                pass
            
            

        if cmds.getAttr("%s.useFrameExtension"%fileNode) == True:
            sequenceFrameList  = []
            soltsAnimationDict[slotName].update({"attachment":[]})
            fileName = cmds.getAttr("%s.fileTextureName"%fileNode).split("/")[-1]
            fileDir = cmds.getAttr("%s.fileTextureName"%fileNode).split(fileName)[0]
            
            allFiles = os.listdir(fileDir)
            sequenceList = []
            for j in allFiles:
               # print i.split(".")
                if j.split(".")[0] == fileName.split(".")[0]:
                    sequenceList.append(j)
                    
           # print sequenceList
            
            for i in range(start,end):
                sequenceFrameList.append(i)
            offsetFrame = random.randint(0,offsetRange)
           # print offsetFrame
            for i in sequenceFrameList:
               # print i ,float(i)/fps
                if int(i) in range(start,end+1):
                    
                   # print fileDir

                    attachmentFile = sequenceList[(i+offsetFrame)%(len(sequenceList))-1].split(".png")[0]
                    soltsAnimationDict[slotName]["attachment"].append({"time": float(i)/fps, "name": attachmentFile })
                    
                else:
                    pass    
        else:
            pass
                    
                    
            
    actionAnimation[actionName]["slots"].update(soltsAnimationDict)
    animationList.update(actionAnimation)
        
       # print "keyFrameList",keyFrameList

  #  return animationList
    
    for bone in boneList:
       # boneKeyFrameList = []
        boneName = bone["name"]
        keyFrameList = getAllkeyFrameList(boneName,start,end)
       # print "keyFrameList",keyFrameList
    
        translateKeyValueList=[]
        scaleKeyValueList=[]
        rotateKeyValueList=[]
      #  print keyFrameList
        if keyFrameList == None :
            pass
        else:
            for i in range(0,len(keyFrameList)):
                frame = float(keyFrameList[i])
                print "frame",frame
                if i == 0:
                    preFrame = 0
                  #  frame = 0.0
                    translateX =  float("%.4f"%(cmds.keyframe( boneName,at='tx',t=(0,0),q=True,eval=True)[0]))      
                    translateY =  float("%.4f"%(cmds.keyframe( boneName,at='ty',t=(0,0),q=True,eval=True)[0]))  
                    rotate = float("%.4f"%(cmds.keyframe( boneName,at='rz',t=(0,0),q=True,eval=True)[0]))      
                    scaleX = float("%.4f"%(cmds.keyframe( boneName,at='sx',t=(0,0),q=True,eval=True)[0]))      
                    scaleY = float("%.4f"%(cmds.keyframe( boneName,at='sy',t=(0,0),q=True,eval=True)[0]))      

                else:
                    
                    preFrame = keyFrameList[i-1]
                    
                    translateXFrame = float("%.4f"%(cmds.keyframe( boneName,at='tx',t=(frame,frame),q=True,eval=True)[0]))      
                    translateXpreFrame = float("%.4f"%(cmds.keyframe( boneName,at='tx',t=(preFrame,preFrame),q=True,eval=True)[0]))     
                    translateX =  translateXFrame-translateXpreFrame
                    
                    translateYFrame = float("%.4f"%(cmds.keyframe( boneName,at='ty',t=(frame,frame),q=True,eval=True)[0]))      
                    translateYpreFrame = float("%.4f"%(cmds.keyframe( boneName,at='ty',t=(preFrame,preFrame),q=True,eval=True)[0]))     
                    translateY =  translateYFrame-translateYpreFrame
                    
                    rotateFrame = float("%.4f"%(cmds.keyframe( boneName,at='rz',t=(frame,frame),q=True,eval=True)[0]))      
                    rotatePreFrame = float("%.4f"%(cmds.keyframe( boneName,at='rz',t=(preFrame,preFrame),q=True,eval=True)[0]))     
                    rotate =  rotateFrame#-rotatePreFrame
                    
                                    
                    scaleXFrame = float("%.4f"%(cmds.keyframe( boneName,at='sx',t=(frame,frame),q=True,eval=True)[0]))      
                    scaleXPreFrame = float("%.4f"%(cmds.keyframe( boneName,at='sx',t=(preFrame,preFrame),q=True,eval=True)[0]))     
                    scaleX =  scaleXFrame/scaleXPreFrame
                    
                    scaleYFrame = float("%.4f"%(cmds.keyframe( boneName,at='sy',t=(frame,frame),q=True,eval=True)[0]))      
                    scaleYPreFrame = float("%.4f"%(cmds.keyframe( boneName,at='sy',t=(preFrame,preFrame),q=True,eval=True)[0]))     
                    scaleY =  scaleYFrame/scaleYPreFrame
                
                
                
               # print boneName,frame,rotateFrame,rotatePreFrame,rotate
                translateKeyValueList.append({"time":frame/fps,"x":translateX,"y":translateY})  #,"curve": [ 0.25, 0, 0.75, 1 ]
                scaleKeyValueList.append({"time":frame/fps,"x":scaleX,"y":scaleY})
                rotateKeyValueList.append({"time":frame/fps,"angle":rotate})
            '''
            for i in keyFrameList:
                if int(i) in range(start,end+1):
                    print i,boneName

                    translateX = float("%.4f"%(cmds.keyframe( boneName,at='tx',t=(i,i),q=True,eval=True)[0]))          
                    translateY = float("%.4f"%(cmds.keyframe( boneName,at='ty',t=(i,i),q=True,eval=True)[0]))
                    rotate = float( "%.4f"%(cmds.keyframe( boneName,at='rz',t=(i,i),q=True,eval=True)[0]))
                    width = float("%.4f"%(cmds.keyframe( boneName,at='sx',t=(i,i),q=True,eval=True)[0]))
                    height = float("%.4f"%(cmds.keyframe( boneName,at='sy',t=(i,i),q=True,eval=True)[0]))
                    originalWidth = float("%.4f"%(cmds.keyframe( boneName,at='sx',t=(0,0),q=True,eval=True)[0]))
                    originalHeight = float("%.4f"%(cmds.keyframe( boneName,at='sy',t=(0,0),q=True,eval=True)[0]))
                    scaleX = width/ originalWidth
                    scaleY = height /originalHeight
                   # print i ,boneName,rotate

                    if i == 0:
                       # print "0000" getAnimationList
                        translateKeyValueList.append({"time":i/fps,"x":translateX,"y":translateY})  #,"curve": [ 0.25, 0, 0.75, 1 ]
                    else:
                        translateKeyValueList.append({"time":i/fps,"x":translateX,"y":translateY})  #,"curve": [ 0.25, 0, 0.75, 1 ]
                    scaleKeyValueList.append({"time":i/fps,"x":scaleX,"y":scaleY})
                    rotateKeyValueList.append({"time":i/fps,"angle":rotate})

                else:
                    pass
            '''
            boneAnimationDict = {str(boneName):{"translate":translateKeyValueList,"scale":scaleKeyValueList,"rotate":rotateKeyValueList}}
            animationList[actionName]["bones"].update(boneAnimationDict)

    return animationList    
        


   
        
        
    

    
    
def exportSpineDefineJson(exportFileName,boneList):
    spineJson = {
                "bones": boneList,
                "animations": {}
                }
     
    writeData = json.dumps(spineJson, sort_keys=True , indent =4) 
    #writeData = json.dumps(exportJson) 
    with open(exportFileName, 'w') as the_file:
        the_file.write(writeData)     
               
 
 
def getExportJson(fileName,boneList,slotList,skinList,animationList):
    exportFileName =fileName# "//mcd-server/webServer/spineTest/effectB/effectB_01.json"
   # exportFileName = "C:/Users/alpha/Documents/GitHub/JS_learning/spineTest/spineJsonTest_02.json"

    exportDict = {}
    exportDict.update({"bones":boneList})
    exportDict.update({"slots":slotList})
    exportDict.update({"skins":skinList})
    exportDict.update({"animations":animationList})
   # exportDict.update({"animations":animationList})


    #print ecportJson
    writeData = json.dumps(exportDict, sort_keys=True , indent =4) 
    #writeData = json.dumps(exportJson) 
    with open(exportFileName, 'w') as the_file:
        the_file.write(writeData)
  #  return exportDict               
               
    
def run():
    cmds.currentTime(0,e=True)
    exportFileName = "C:/Users/alpha/Documents/GitHub/JS_learning/spineTest/skeletonTest/uvSkinTest.json"
    #exportFileName =  "C:/alphaOnly/github/JS_learning/spineTest/skeletonTest/uvSkinTest.json"
    boneList = defineBone("joint6")
    slotList = getAllSlots(boneList)
    skinList = getSkinsList(slotList)
    animationList = getAnimationList(slotList,boneList,30,1,60,0,"testAct")

    getExportJson(exportFileName,boneList,slotList,skinList,animationList)
   # print "boneList",boneList
   # print "slotList",slotList
   # print "skinList",skinList
    
    #getUVData(meshName,borderEdges)
    
    


def runB(meshName):
    
    boneList = getMeshData(meshName)
    dataForSpine = getUVData(meshName,boneList)
    
    print dataForSpine
#print getMeshData("polySurface1")
#cmds.select(getMeshData("polySurface3"))
#getSlotData("joint1")
    
    
#runB("polySurface1")


run()









