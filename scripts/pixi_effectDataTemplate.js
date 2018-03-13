
function loadGlobalData() {
    var PIXI_globalData = {
        "BGA": {
            "URL": "",
            "width": 1920,
            "height": 1080,
            "BGColor": "FFFFFF",
            "screenScale": 1
        },
        "effect_A": {
            "motionJson": "",
            "spritesImageMode": 1,
            "stillImageName": "",
            "spritesJson": "",
            "spritesImage": "",
            "anchor": 0.5,
            "blendMode": "NORMAL",
            "adjust": {
                "speed": 1,
                "frameSpeed": 1,
                "spritesSize": 1,
                "spritesSizeRandom": 0,
                "spritesRotation": 0,
                "spritesRotationRandom": 0,
                "spritesFrameOffset": 5,
                "spritesTrans": 1,
                "spritesBlur": 0
            },
            "stageDescriptJsonFile": "",
            "stageDescriptJsonData": "",
            "stage": {
                "stage_01": [{
                        "position": {
                            "x": 0,
                            "y": 0
                        }
                    },
                    {
                        "scale": 1
                    },
                    {
                        "rotation": 0
                    },
                    {
                        "blendMode": 0
                    }]
            }
        },
        "effect_B": {
            "motionJson": "",
            "spritesImageMode": 1,
            "stillImageName": "",
            "spritesJson": "",
            "spritesImage": "",
            "anchor": 0.5,
            "blendMode": "NORMAL",
            "adjust": {
                "speed": 1,
                "frameSpeed": 1,
                "spritesSize": 1,
                "spritesSizeRandom": 0,
                "spritesRotation": 0,
                "spritesRotationRandom": 0,
                "spritesFrameOffset": 5,
                "spritesBlur": 0
            },
            "stageDescriptJsonFile": "",
            "stageDescriptJsonData": "",
            "stage": {
                "stage_01": [{
                        "position": {
                            "x": 0,
                            "y": 0
                        }
                    },
                    {
                        "scale": 1
                    },
                    {
                        "rotation": 0
                    },
                    {
                        "blendMode": 0
                    }]
            }
        },
        "effect_C": {
            "motionJson": "",
            "spritesImageMode": 1,
            "stillImageName": "",
            "spritesJson": "",
            "spritesImage": "",
            "anchor": 0.5,
            "blendMode": "NORMAL",
            "adjust": {
                "speed": 1,
                "frameSpeed": 1,
                "spritesSize": 1,
                "spritesSizeRandom": 0,
                "spritesRotation": 0,
                "spritesRotationRandom": 0,
                "spritesFrameOffset": 5,
                "spritesBlur": 0
            },
            "stageDescriptJsonFile": "",
            "stageDescriptJsonData": "",
            "stage": {
                "stage_01": [{
                        "position": {
                            "x": 0,
                            "y": 0
                        }
                    },
                    {
                        "scale": 1
                    },
                    {
                        "rotation": 0
                    },
                    {
                        "blendMode": 0
                    }]
            }
        },
        "inputD": {
            "motionJson": "",
            "spritesImageMode": 1,
            "stillImageName": "",
            "spritesJson": "",
            "spritesImage": "",
            "anchor": 0.5,
            "blendMode": "NORMAL",
            "adjust": {
                "speed": 1,
                "frameSpeed": 1,
                "spritesSize": 1,
                "spritesSizeRandom": 0,
                "spritesRotation": 0,
                "spritesRotationRandom": 0,
                "spritesFrameOffset": 5,
                "spritesBlur": 0
            },
            "stageDescriptJsonFile": "",
            "stageDescriptJsonData": "",
            "stage": {
                "stage_01": [{
                        "position": {
                            "x": 0,
                            "y": 0
                        }
                    },
                    {
                        "scale": 1
                    },
                    {
                        "rotation": 0
                    },
                    {
                        "blendMode": 0
                    }]
            }
        },
        "inputE": {
            "motionJson": "",
            "spritesImageMode": 1,
            "stillImageName": "",
            "spritesJson": "",
            "spritesImage": "",
            "anchor": 0.5,
            "blendMode": "NORMAL",
            "adjust": {
                "speed": 1,
                "frameSpeed": 1,
                "spritesSize": 1,
                "spritesSizeRandom": 0,
                "spritesRotation": 0,
                "spritesRotationRandom": 0,
                "spritesFrameOffset": 5,
                "spritesBlur": 0
            },
            "stageDescriptJsonFile": "",
            "stageDescriptJsonData": "",
            "stage": {
                "stage_01": [{
                        "position": {
                            "x": 0,
                            "y": 0
                        }
                    },
                    {
                        "scale": 1
                    },
                    {
                        "rotation": 0
                    },
                    {
                        "blendMode": 0
                    }]
            }
        }

    };

    return PIXI_globalData;
};


function getSpritesImagesData(id, url, effectName) {
    delete loader.resources[id];
    //load.reset();
    loader.add(id, url)
        .load(function (loader, resources) {
            //console.log("frameList",resources[String(id)].data.frames);
            //frameList = resources[String(id)].data.frames;
            effectDataTemplate.spritesImageId = id;
            effectDataTemplate.spriteImage = url.split('.')[0] + ".png";
            effectDataTemplate.frameList = (Object.keys(resources[String(id)].data.frames));
            effectDataTemplate.frameLength = (Object.keys(resources[String(id)].data.frames).length);
            effectList[effectName] = effectDataTemplate;
        });
    //.load();
    console.log("effectList", effectList);
};


function getMotionData(id, url, effectName) {
    delete loader.resources[id];
    // load.reset();

    loader.add(id, url)
        .load(function (loader, resources) {
            var motionDataKeysCount = Object.keys(resources[String(id)].data).length;
            var motionDataKeys = Object.keys(resources[String(id)].data);
            effectDataTemplate.motionDataID = id;
            effectDataTemplate.motionDataURL = url;
            effectDataTemplate.motionData = resources[String(id)].data;
            effectDataTemplate.instancerCount = resources[String(id)].data.metaData.instancer_num;
            effectDataTemplate.instancerID = Object.keys(resources[String(id)].data.instancer);

            var ppIDList = [];

            for (var i = 0; i < motionDataKeysCount; i++) {
                //console.log("show motionData", i ,motionDataKeys[i],motionDataKeys[i].slice(0,3));
                if (motionDataKeys[i].slice(0, 3) == "pId") {
                    //console.log("show motionData 3",motionDataKeys[i] );
                    ppIDList.push(motionDataKeys[i]);
                };
            };
            //console.log("ppidList",ppIDList);
            effectDataTemplate.ppID = ppIDList;
            effectDataTemplate.ppCount = resources[String(id)].data.metaData.particle_num;
            effectList[effectName] = effectDataTemplate;


        });

    console.log("effectList", effectList);

};
