import maya.cmds as cmds
import json
import random
import os
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
    	#{ "name": "star2", "bone": "star2", "color": "ffffff00", "attachment": "star", "blend": "additive" },
    	
    	
def getSkinsList(slotList):
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
            
            
        
        
        

def getAnimationList(slotList,boneList,fps,start,end,offsetRange):
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
       # print fileNode , cmds.getAttr("%s.useFrameExtension"%fileNode)
       # print fileNode , attachment

            #print keyFrameList
                
        
        
        
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
                    
        #print keyFrameList
        #keyFrameListCount = len(keyFrameListCount) 



        
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
                if int(i) in range(start,end+1):
                 #   print i
                    translateX = float("%.2f"%(cmds.keyframe( boneName,at='tx',t=(i,i),q=True,eval=True)[0]))          
                    translateY = float("%.2f"%(cmds.keyframe( boneName,at='ty',t=(i,i),q=True,eval=True)[0]))
                    rotate = float( "%.2f"%(cmds.keyframe( boneName,at='rz',t=(i,i),q=True,eval=True)[0]))
                    width = float("%.2f"%(cmds.keyframe( boneName,at='sx',t=(i,i),q=True,eval=True)[0]))
                    height = float("%.2f"%(cmds.keyframe( boneName,at='sy',t=(i,i),q=True,eval=True)[0]))
                    originalWidth = float("%.2f"%(cmds.keyframe( boneName,at='sx',t=(0,0),q=True,eval=True)[0]))
                    originalHeight = float("%.2f"%(cmds.keyframe( boneName,at='sy',t=(0,0),q=True,eval=True)[0]))
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
            boneAnimationDict = {str(boneName):{"translate":translateKeyValueList,"scale":scaleKeyValueList,"rotate":rotateKeyValueList}}
            animationList[actionName]["bones"].update(boneAnimationDict)
        #print animationList
       
    return animationList    
        
        
        

    
def getExportJson(fileName,boneList,slotList,skinList,animationList):
    exportFileName =fileName# "//mcd-server/webServer/spineTest/effectB/effectB_01.json"
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
    cmds.currentTime(0,e=True)
    rootName = "root_xz_freeSpin_effectA"
    fileName = "//mcd-one/3d_project/xiang_long_xian_rui/assets/other/freespin_effect_a/concept/sourceimages/xz_freeSpinEffect01.json"
    boneList = getAllbones(rootName)
    slotList = getAllSlots(boneList)
    skinList = getSkinsList(slotList)
    animationList = getAnimationList(slotList,boneList,30,0,125,0)
    getExportJson(fileName,boneList,slotList,skinList,animationList)


def copyKeyTOJoint():
    for i in cmds.ls(sl=True):
        #print i
        keyFrameList = cmds.keyframe(i, attribute='translateX', query=True, cp =True)
        
      #  print keyFrameList
        bone = cmds.createNode("joint",n= "joint##")

        createPolyPlane = cmds.polyPlane(n="slot_##",sx= 1,sy=1)[0]
     #   print createPolyPlane
        cmds.setAttr("%s.scaleX"%createPolyPlane,50)
        cmds.setAttr("%s.scaleZ"%createPolyPlane,50)
        cmds.setAttr("%s.rotateX"%createPolyPlane,90)
        cmds.parent(createPolyPlane,bone)
        #print "i",i
        
        cmds.copyKey(i)
        cmds.pasteKey(bone)
        
    
    
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

#copyKeyTOJoint()