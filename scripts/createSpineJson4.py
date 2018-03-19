import maya.cmds as cmds
import json


fps = 120
exportFileName = "C:/alphaOnly/github/JS_learning/spineTest/powerup2.json"

exportJson = {"bones":[],"slots":[],"skins": {"default":{}},"animations":{}}
bones = [{ "name": "root" }]
slots = []
skins = {"default":{}}
animations = {}

skeleton = { "hash": "", "spine": "3.6.32", "width": 1920, "height": 1024, "images": "" },

## define bone  
boneList =  cmds.listRelatives( "root", c=True)
cmds.currentTime(0,e=True)  ## move to frame 0, as bind pose
for i in boneList:
    x = int( cmds.getAttr("%s.translateX"%i))
    y = int( cmds.getAttr("%s.translateY"%i))
    r = int( cmds.getAttr("%s.rotateZ"%i))

    boneDict= {"name":i,"parent":"root","rotation":r,"x" :x,"y" :y }
    bones.append(boneDict)

## define slots  
slotFileDict = {}
for i in range(0,len(boneList)):
    
    getObj =  cmds.ls(boneList[i],dag=1)[1]
    shadingGrps = cmds.listConnections(getObj,type='shadingEngine')
    shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
    fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')
    currentFile = cmds.getAttr("%s.fileTextureName" % fileNode[0])
    fileInSlot = currentFile.split("/")[-1].split(".")[0]
    alphaGain = "%02x"%int((cmds.getAttr("%s.alphaGain"%fileNode[0])/1)*255)
    colorGain =  cmds.getAttr("%s.colorGain"%fileNode[0])[0]
    colorGainHex = "%02x"%int((colorGain[0]/1)*255) + "%02x"%int((colorGain[1]/1)*255) +"%02x"%int((colorGain[2]/1)*255)
    exportColorHex = colorGainHex + alphaGain 
    
    slotDict = {"name":"pId_%s"%i,"bone":boneList[i],"color": exportColorHex,"attachment":fileInSlot, "blend": "normal"}
    slotFileDict.update({fileInSlot:fileNode})
    slots.append(slotDict)
    

## define skins  
#for i in range(0,len(boneList)):
for i in range(0,len(slots)):
   # print i["name"]
    getObj =  cmds.ls(boneList[i],dag=1)[1]
    shadingGrps = cmds.listConnections(getObj,type='shadingEngine')
    shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
    fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')
    currentFile = cmds.getAttr("%s.fileTextureName" % fileNode[0])
    fileInSlot = currentFile.split("/")[-1].split(".")[0]

    attachmentImage =fileInSlot
    width = int(cmds.getAttr( "%s.scaleX"%slots[i]["bone"]))
    height = int(cmds.getAttr( "%s.scaleZ"%slots[i]["bone"]))
    

    skins["default"].update({slots[i]["name"]:{	attachmentImage: { "width": width, "height": height }}})


##define animations ,bone

actionName = "testAction"
actionAnimation={actionName:{"slots":{},
                             "bones":{}}}

'''
actionAnimation ={actionName:{"slots":{slotName:{
                                                 "attachment":[],
                                                 "color":[],
                                                 }
                                        },
                              "bones":{boneName:{
                                                 "translate":[],
                                                 "scale":[],
                                                 "rotate":[]}}
                              }
                    }
'''
for bone in boneList:
    keyFrameList = cmds.keyframe(bone, attribute='translateX', query=True, cp =True)
    translateKeyValueList=[]
    scaleKeyValueList=[]
    rotateKeyValueList=[]
  #  print keyFrameList
    if keyFrameList == None :
        pass
    else:
        for i in keyFrameList:
            translateX = float("%.2f"%(cmds.keyframe( bone,at='tx',t=(i,i),q=True,eval=True)[0]))          
            translateY = float("%.2f"%(cmds.keyframe( bone,at='ty',t=(i,i),q=True,eval=True)[0]))
            rotate = float( "%.2f"%(cmds.keyframe( bone,at='rz',t=(i,i),q=True,eval=True)[0]))
            width = float("%.2f"%(cmds.keyframe( bone,at='sx',t=(i,i),q=True,eval=True)[0]))
            height = float("%.2f"%(cmds.keyframe( bone,at='sz',t=(i,i),q=True,eval=True)[0]))
            originalWidth = float("%.2f"%(cmds.keyframe( bone,at='sx',t=(0,0),q=True,eval=True)[0]))
            originalHeight = float("%.2f"%(cmds.keyframe( bone,at='sx',t=(0,0),q=True,eval=True)[0]))
            scaleX = width/ originalWidth
            scaleY = height /originalHeight
            if i == 0:
               # print "0000"
                translateKeyValueList.append({"time":i/fps,"x":translateX,"y":translateY})  #,"curve": [ 0.25, 0, 0.75, 1 ]
            else:
                translateKeyValueList.append({"time":i/fps,"x":translateX,"y":translateY})  #,"curve": [ 0.25, 0, 0.75, 1 ]
            scaleKeyValueList.append({"time":i/fps,"x":scaleX,"y":scaleY})
            rotateKeyValueList.append({"time":i/fps,"angle":rotate})
            
        boneAnimationDict = {str(bone):{"translate":translateKeyValueList,"scale":scaleKeyValueList,"rotate":rotateKeyValueList}}
        actionAnimation[actionName]["bones"].update(boneAnimationDict)


##define animations ,slot

soltsAnimationDict= {}
for slot in slots:
    tempSlotDict = {slot["name"]:{"color":[]}}
    soltsAnimationDict.update(tempSlotDict)
   # soltsAnimationDict["color"].update({slot["name"]:{"color":[],"attachment":[]}})
    getParentBone = cmds.ls(slot["bone"],dag = 1)[1]
  #  print slot["name"],getParentBone
    shadingGrps = cmds.listConnections(getParentBone,type='shadingEngine')
    shaders = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
    fileNode = cmds.listConnections('%s.color' % (shaders[0]), type='file')
    currentFile = cmds.getAttr("%s.fileTextureName" % fileNode[0])
    fileInSlot = currentFile.split("/")[-1].split(".")[0]

    attachmentImage =fileInSlot
    print slot["name"],fileNode ,attachmentImage
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
            
        
    for i in keyFrameList:
        cmds.currentTime(i,e=True)
      #  print 
        alphaGain = cmds.getAttr( "%s.alphaGain"%fileNode[0])
        colorGain = cmds.getAttr("%s.colorGain"%fileNode[0])[0]
        alphaGainHex = "%02x"%int((alphaGain/1)*255)
        colorGainHex = "%02x"%int((colorGain[0]/1)*255) + "%02x"%int((colorGain[1]/1)*255) +"%02x"%int((colorGain[2]/1)*255)
        exportColorHex = str(colorGainHex + alphaGainHex)
      #  print slot["name"],fileNode ,i,attachmentImage,exportColorHex
        soltsAnimationDict[slot["name"]]["color"].append({"time": i/60, "color": exportColorHex })
   # print soltsAnimationDict
actionAnimation[actionName]["slots"].update(soltsAnimationDict)
#print actionAnimation
animations.update(actionAnimation)

#ecportJson.update({"skeleton":skeleton})
    
exportJson["bones"] = bones
exportJson["slots"] = slots
exportJson["skins"] = skins
exportJson["animations"]=animations
#print ecportJson
writeData = json.dumps(exportJson, sort_keys=True , indent =4) 
#writeData = json.dumps(exportJson) 
with open(exportFileName, 'w') as the_file:
    the_file.write(writeData)
        
