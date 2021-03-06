import maya.cmds as cmds
import json

def getAllbones(rootJoint):
    allBoneList = []

    for i in cmds.ls(rootJoint,dag =2):
        if cmds.nodeType(i) =="joint":
            allBoneList.append(i)
    
   # print allBoneList
    
    #allBoneList = cmds.ls(type="joint" ,l =True)
    boneList = []
    for bone in allBoneList:
      #  print bone
        #boneShotName =  i.split("|")[-1]
        boneParent = cmds.listRelatives(bone,p=True)
        if boneParent == None:
            pass
        else:
           boneParent = boneParent[0]
            
        x = cmds.getAttr("%s.translateX"%bone)
        y = cmds.getAttr("%s.translateY"%bone)
        r = cmds.getAttr("%s.rotateZ"%bone)
        scaleX = cmds.getAttr("%s.scaleX"%bone)
        scaleY = cmds.getAttr("%s.scaleY"%bone)

       # print boneShotName,bone
        boneDict = {"name":bone,
                    "parent":boneParent,
                    "rotation":r,
                    "x": x,
                    "y":y,
                    "scaleX":scaleX,
                    "scaleY":scaleY
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
                getObj =  cmds.ls(j,dag=1)[1]
                shadingGrps = cmds.listConnections(getObj,type='shadingEngine')
                shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
                fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')
                currentFile = cmds.getAttr("%s.fileTextureName" % fileNode[0])
                fileInSlot = currentFile.split("/")[-1].split(".")[0]
               # print parentBone
                #print j , cmds.listRelatives(j,p=True)[0]
                slotList.append({"name":j,
                                 "bone":parentBone,
                                 "color":"ffffffff",
                                 "attachment":fileInSlot,
                                 "blend":"additive"})
    return slotList
    	#{ "name": "star2", "bone": "star2", "color": "ffffff00", "attachment": "star", "blend": "additive" },
    	
    	
def getSkinsList(slotList):
    skinList= {"default":{}}
    for i in slotList:
        slotName = i["name"]
       # print "solt",soltName
        getObj =  cmds.ls(slotName,dag=1)[1]
        shadingGrps = cmds.listConnections(getObj,type='shadingEngine')
        shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
        fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')
        currentFile = cmds.getAttr("%s.fileTextureName" % fileNode[0])
        fileInSlot = currentFile.split("/")[-1].split(".")[0]
        attachmentImage =fileInSlot
        width = int(cmds.getAttr( "%s.scaleX"%slotName))
        height = int(cmds.getAttr( "%s.scaleZ"%slotName))
        x = int(cmds.getAttr( "%s.translateX"%slotName))
        y = int(cmds.getAttr( "%s.translateY"%slotName))

      #  print width,height
        

        skinList["default"].update({slotName:{	attachmentImage: { "width": width, 
                                                                 "height": height,
                                                                 "x":x,
                                                                 "y":y }}})
    return skinList

def getAnimationList(slotList,boneList,fps):
    actionName = "testAction"
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
       # print fileNode , attachment
        
        keyFrameList = []
       # print slot, slotFileDict[slot]
        alphaGainkeyFrameList = cmds.keyframe(fileNode, attribute='alphaGain', query=True, cp =True)
        if alphaGainkeyFrameList == None :
            pass
        else:
            for i in alphaGainkeyFrameList:
                if i in keyFrameList:
                    pass
                else:
                    keyFrameList.append(i)
        colorGainKeyFrameList = cmds.keyframe(fileNode, attribute='colorGain', query=True, cp =True)
        if colorGainKeyFrameList == None :
            pass
        else:
            for i in colorGainKeyFrameList:
                if i in keyFrameList:
                    pass
                else:
                    keyFrameList.append(i) 
                    
     #   print keyFrameList
                
            
        for i in keyFrameList:
            cmds.currentTime(i,e=True)
            alphaGain = cmds.getAttr( "%s.alphaGain"%fileNode)
            colorGain = cmds.getAttr("%s.colorGain"%fileNode)[0]
          #  print alphaGain,colorGain
            
            alphaGainHex = "%02x"%int((alphaGain/1)*255)
            colorGainHex = "%02x"%int((colorGain[0]/1)*255) + "%02x"%int((colorGain[1]/1)*255) +"%02x"%int((colorGain[2]/1)*255)
            exportColorHex = str(colorGainHex + alphaGainHex)
          #  print slot["name"],fileNode ,i,attachmentImage,exportColorHex
            soltsAnimationDict[slotName]["color"].append({"time": i/fps, "color": exportColorHex })
        #print slotName
    actionAnimation[actionName]["slots"].update(soltsAnimationDict)
    animationList.update(actionAnimation)
   # print animationList

    for bone in boneList:
       # boneKeyFrameList = []
        boneName = bone["name"]
        keyFrameList = cmds.keyframe(boneName, attribute='translateX', query=True, cp =True)
       # print "keyFrameList",keyFrameList
    
      #  print "boneName",boneName
    
        translateKeyValueList=[]
        scaleKeyValueList=[]
        rotateKeyValueList=[]
      #  print keyFrameList
        if keyFrameList == None :
            pass
        else:
            for i in keyFrameList:
                translateX = float("%.2f"%(cmds.keyframe( boneName,at='tx',t=(i,i),q=True,eval=True)[0]))          
                translateY = float("%.2f"%(cmds.keyframe( boneName,at='ty',t=(i,i),q=True,eval=True)[0]))
                rotate = float( "%.2f"%(cmds.keyframe( boneName,at='rz',t=(i,i),q=True,eval=True)[0]))
                width = float("%.2f"%(cmds.keyframe( boneName,at='sx',t=(i,i),q=True,eval=True)[0]))
                height = float("%.2f"%(cmds.keyframe( boneName,at='sy',t=(i,i),q=True,eval=True)[0]))
                originalWidth = float("%.2f"%(cmds.keyframe( boneName,at='sx',t=(0,0),q=True,eval=True)[0]))
                originalHeight = float("%.2f"%(cmds.keyframe( boneName,at='sy',t=(0,0),q=True,eval=True)[0]))
                scaleX = width/ originalWidth
                scaleY = height /originalHeight
                print i ,boneName,rotate

                if i == 0:
                   # print "0000" getAnimationList
                    translateKeyValueList.append({"time":i/fps,"x":translateX,"y":translateY})  #,"curve": [ 0.25, 0, 0.75, 1 ]
                else:
                    translateKeyValueList.append({"time":i/fps,"x":translateX,"y":translateY})  #,"curve": [ 0.25, 0, 0.75, 1 ]
                scaleKeyValueList.append({"time":i/fps,"x":scaleX,"y":scaleY})
                rotateKeyValueList.append({"time":i/fps,"angle":rotate})
                
            boneAnimationDict = {str(boneName):{"translate":translateKeyValueList,"scale":scaleKeyValueList,"rotate":rotateKeyValueList}}
            animationList[actionName]["bones"].update(boneAnimationDict)
        #print animationList
       
    return animationList    
        


def getUVData(meshName,borderEdges):
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
        
        

    
def getExportJson(boneList,slotList,skinList,animationList):
    exportFileName = "//mcd-server/webServer/spineTest/effectB/effectB_01.json"
   # exportFileName = "C:/Users/alpha/Documents/GitHub/JS_learning/spineTest/spineJsonTest_02.json"

    exportDict = {}
    exportDict.update({"bones":boneList})
    exportDict.update({"slots":slotList})
    exportDict.update({"skins":skinList})
    exportDict.update({"animations":animationList})


    #print ecportJson
    writeData = json.dumps(exportDict, sort_keys=True , indent =4) 
    #writeData = json.dumps(exportJson) 
    with open(exportFileName, 'w') as the_file:
        the_file.write(writeData)
  #  return exportDict
    
    
def run():
    
    boneList = getAllbones()
    #print getAllSlots(boneList),len(boneList)
    
    cmds.select("slotB1")
def runB():
    rootName = "joint1"
    boneList = getAllbones(rootName)
    slotList ={}
    skinList = {}
    animationList = {}
    #print "boneList",boneList
   # slotList = getAllSlots(boneList)
    #print "slotList",slotList
    #skinList = getSkinsList(slotList)
    #animationList = getAnimationList(slotList,boneList,30)
    getExportJson(boneList,slotList,skinList,animationList)

    
    
#run()

runB()
'''
for i in cmds.ls(sl=True):
    print i, cmds.listRelatives(i,c=True)
    objectName = "%s|%s"%(i,cmds.listRelatives(i,c=True)[0])
    newName = i[:-3] +"_slot_"+ str( i[-3:])
  #  print newName
    cmds.rename(objectName,newName)
    
 '''   

