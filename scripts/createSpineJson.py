import maya.cmds as cmds
import json

exportFileName = "C:/alphaOnly/github/JS_learning/spineTest/powerup.json"

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

for i in range(0,len(boneList)):
    
    slotDict = {"name":"pId_%s"%i,"bone":boneList[i],"color": "ffffffff","attachment":"star", "blend": "additive"}
    slots.append(slotDict)
    

## define skins  
#for i in range(0,len(boneList)):
for i in slots:
   # print i["name"]
    attachmentImage = "star"
    width = int(cmds.getAttr( "%s.scaleX"%i["bone"]))
    height = int(cmds.getAttr( "%s.scaleZ"%i["bone"]))

    skins["default"].update({i["name"]:{	attachmentImage: { "width": width, "height": height }}})


##define animations

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
    print keyFrameList
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

            translateKeyValueList.append({"time":i/60,"x":translateX,"y":translateY})  #,"curve": [ 0.5, 0, 0.75, 1 ]
            scaleKeyValueList.append({"time":i/60,"x":scaleX,"y":scaleY})
            rotateKeyValueList.append({"time":i/60,"angle":rotate})
            
        boneAnimationDict = {str(bone):{"translate":translateKeyValueList,"scale":scaleKeyValueList,"rotate":rotateKeyValueList}}
        actionAnimation[actionName]["bones"].update(boneAnimationDict)

#print actionAnimation
animations.update(actionAnimation)
   # print i ,translateX,translateY,rotate,width,height



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
        
