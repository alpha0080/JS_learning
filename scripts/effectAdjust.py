import os
import random

#rename
for i in cmds.ls(sl=True):
   # print i, cmds.listRelatives(i,c=True)
    objectName = "%s|%s"%(i,cmds.listRelatives(i,c=True)[0])
   # print i ,newName
    newName = i[:-3] +"_slot"+ i.split("_")[-1]
    print i ," -- ",newName
    cmds.rename(objectName,newName)
    
    
###check sequences
#cmds.getAttr("%s.useFrameExtension"%nodeName) 

nodeName ="pasted__file5" 
if cmds.getAttr("%s.useFrameExtension"%nodeName) ==True: 
    fileName = cmds.getAttr("%s.fileTextureName"%nodeName).split("/")[-1]
    fileDir = cmds.getAttr("%s.fileTextureName"%nodeName).split(fileName)[0]
   # print fileDir
    allFiles = os.listdir(fileDir)
    sequenceList = []
    for i in allFiles:
       # print i.split(".")
        if i.split(".")[0] == fileName.split(".")[0]:
            sequenceList.append(i)
            
    print sequenceList
else:
    fileName = cmds.getAttr("%s.fileTextureName"%nodeName).split("/")[-1]
    print fileName
     
#如果為連續貼圖，則skin不指定attachment，在animation中指定
 
 
 
 
    
    
#copy key to joint

#cmds.createNode("joint",n= "joint##")


for i in cmds.ls(sl=True):
    #print i
    keyFrameList = cmds.keyframe(i, attribute='translateX', query=True, cp =True)
    
    print keyFrameList
    bone = cmds.createNode("joint",n= "effectD_cloudC_##")

    createPolyPlane = cmds.polyPlane(n="slot_##",sx= 1,sy=1)[0]
    print createPolyPlane
    cmds.setAttr("%s.scaleX"%createPolyPlane,50)
    cmds.setAttr("%s.scaleZ"%createPolyPlane,50)
    cmds.setAttr("%s.rotateX"%createPolyPlane,90)
    cmds.parent(createPolyPlane,bone)
    print "i",i
    
    cmds.copyKey(i)
    cmds.pasteKey(bone)
        
    
    
#offset all y keys
for i in cmds.ls(sl=True):
    keyFrameList = cmds.keyframe(i, attribute='translateY', query=True, cp =True)
    print keyFrameList
    for j in keyFrameList:
        cmds.currentTime(j,e=True)

        y= cmds.getAttr("%s.translateY"%i)-860
        cmds.setAttr("%s.translateY"%i,y)
        cmds.setKeyframe(i,attribute='translateY')


        
        
#offset all x keys
        
for i in cmds.ls(sl=True):
    keyFrameList = cmds.keyframe(i, attribute='translateX', query=True, cp =True)
    print keyFrameList
    offsetX = random.randint(-900,900)
    for j in keyFrameList:
        cmds.currentTime(j,e=True)

        x= cmds.getAttr("%s.translateX"%i)+ offsetX
        cmds.setAttr("%s.translateX"%i,x)
        cmds.setKeyframe(i,attribute='translateX')
        
        
#reScale all keys


        
for i in cmds.ls(sl=True):
    keyFrameList = cmds.keyframe(i, attribute='scaleX', query=True, cp =True)
    print keyFrameList
    rescale = 1.2
    for j in keyFrameList:
        cmds.currentTime(j,e=True)

        sx= cmds.getAttr("%s.scaleX"%i) * rescale
        cmds.setAttr("%s.scaleX"%i,sx)
        cmds.setKeyframe(i,attribute='scaleX')
        cmds.setAttr("%s.scaleY"%i,sx)
        cmds.setKeyframe(i,attribute='scaleY')
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
