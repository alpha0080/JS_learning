
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

        
def getBorderEdgeList(): 
    borderEdgeList = []      
    for i in cmds.ls(sl=True,fl=True):
        borderEdgeList.append(i)
        
    return borderEdgeList
    
    
borderEdge = getBorderEdgeList()
print getUVData("pPlane3",borderEdge)
