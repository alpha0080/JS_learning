//canvas



var loadEffect = {
	effectDataTemplate: {
		"spritesImageId": "",
		"spriteImage": "",
		"spriteImageURL": "",
		"frameList": "",
		"frameLength": "",
		"motionDataID": "",
		"motionDataURL": "",
		"motionData": "",
		"instancerCount": "",
		"instancerID": "",
		"ppID": "",
		"ppCount": "",
		"timeStart": "",
		"timeEnd": "",
		"timeLength": "",
		"sourceWidth": "",
		"sourceHeight": "",
		"screenWidth": "",
		"screenHeight": "",
		"sequence": "",
		"spritesData": "",
		"spritesImagesList": "",
		"spritesImagesSize": ""
	},
	loading_Progress: 0,
	createNew: function () {

		var effectData = {};

		effectData.newEvent = function (effectList, effectName) {
			//effectList[effectName] = effectDataTemplate;
		};




		effectData.readSources = function () {};
		effectData.readSpritesData = function (spritesID, spritesURL, effectName) {
			//loader.reset();
			delete loader.resources[spritesID];
			loader.add(spritesID, spritesURL)
				.on("progress", loadProgressHandler)
				.load(setup);

			function loadProgressHandler(loader, resource) {
				console.log("loading: " + resource.url);

				console.log("progress: " + loader.progress + "%");

				console.log("loading: " + resource.name);
			}

			function setup() {
				//loadEffect.myData =  

				var effectDataTemplate = {};
				console.log("All files loaded", loader.progress);
				//  console.log("loaderData",loader.resources[motionID].data); 
				// effectList[effectName]= loader.resources
				//  let motionData = resources[motionID]["data"];
				//function(){}

				let spritesData = loader.resources[spritesID].data;
				let spritesDataFrames = spritesData.frames
				var spritesImagesCount = Object.keys(spritesData.frames).length;
				var spritesImagesList = Object.keys(spritesData.frames)
				loadEffect.effectDataTemplate.spritesData = spritesData;
				loadEffect.effectDataTemplate.spritesImageId = spritesID;
				loadEffect.effectDataTemplate.spriteImage = spritesURL.split('.')[0] + ".png";
				loadEffect.effectDataTemplate.frameList = Object.keys(spritesData.frames);
				loadEffect.effectDataTemplate.frameLength = (Object.keys(spritesData.frames).length);
				loadEffect.effectDataTemplate.spriteImageURL = spritesURL;
				loadEffect.effectDataTemplate.spritesImagesList = spritesImagesList
				loadEffect.effectDataTemplate.spritesImagesCount = spritesImagesCount
				var spritesImagesSize = []
				for (var i in spritesImagesList) {
					//console.log(spritesDataFrames[spritesImagesList[i]].frame)
					spritesImagesSize.push(spritesDataFrames[spritesImagesList[i]].frame);
				};

				loadEffect.effectDataTemplate.spritesImagesSize = spritesImagesSize;
				//console.log("spritesData", spritesData, spritesDataFrames, spritesImagesSize);




				//console.log("Sprites laoder", loader.resources[spritesID]);

				effectList[effectName] = loadEffect.effectDataTemplate;
			};
		};
		effectData.readMotionData = function (motionID, motionURL, effectName) {

			//const loader = new PIXI.loaders.Loader()
			//loader.reset();
			//const resources = PIXI.loader.resources;
			delete loader.resources[motionID];
			//let templete
			loader.add(motionID, motionURL)
				.on("progress", loadProgressHandler)
				.load(setup);

			function loadProgressHandler(loader, resource) {
				console.log("loading: " + resource.url);

				console.log("progress: " + loader.progress + "%");

				console.log("loading: " + resource.name);
			}

			function setup() {
				//loadEffect.myData =  
				let motionData = loader.resources[motionID].data
				let motionDataKeysCount = Object.keys(motionData).length;
				let motionDataKeys = Object.keys(motionData);
				var effectDataTemplate = {};
				console.log("All files loaded", loader.progress);
				//  console.log("loaderData",loader.resources[motionID].data); 
				// effectList[effectName]= loader.resources
				//  let motionData = resources[motionID]["data"];
				//function(){}
				loadEffect.loading_Progress = loader.progress;
				loadEffect.effectDataTemplate.motionDataID = motionID;
				loadEffect.effectDataTemplate.motionDataURL = motionURL;
				loadEffect.effectDataTemplate.motionData = motionData;
				loadEffect.effectDataTemplate.instancerCount = motionData.metaData.instancer_num;
				loadEffect.effectDataTemplate.instancerID = Object.keys(motionData.instancer);
				loadEffect.effectDataTemplate.timeStart = motionData.metaData.frame_start;
				loadEffect.effectDataTemplate.timeEnd = motionData.metaData.frame_end;
				loadEffect.effectDataTemplate.timeLength = motionData.metaData.frame_end - motionData.metaData.frame_start + 1;
				loadEffect.effectDataTemplate.sourceWidth = motionData.metaData.source_width;
				loadEffect.effectDataTemplate.sourceHeight = motionData.metaData.source_height;
				loadEffect.effectDataTemplate.screenWidth = motionData.metaData.canvas_width;
				loadEffect.effectDataTemplate.screenHeight = motionData.metaData.canvas_height;
				loadEffect.effectDataTemplate.sequence = motionData.metaData.sequence;
				let ppIDList = [];
				for (let i = 0; i < motionDataKeysCount; i++) {
					if (motionDataKeys[i].slice(0, 3) == "pId") {
						ppIDList.push(motionDataKeys[i]);
					};
				};
				loadEffect.effectDataTemplate.ppID = ppIDList;
				loadEffect.effectDataTemplate.ppCount = motionData.metaData.particle_num;

				//console.log("frameList",frameList)

				effectList[effectName] = loadEffect.effectDataTemplate;
				console.log("effectList_motion", effectList)

			}
			// console.log("loaderData_finall",loader.resources);

		};
		effectData.loadData = function (motionID, motionURL, spritesID, spritesURL, effectName) {
			//loader.reset();
			//console.log("run loadData")
			delete loader.resources[motionID];
			delete loader.resources[spritesID];
			loader.add(motionID, motionURL)
				.add(spritesID, spritesURL)
			//console.log("loaderInSide", loader)
		};


		effectData.readData = function (motionID, motionURL, spritesID, spritesURL, effectName) {
			console.log(motionID, motionURL, spritesID, spritesURL, effectName);
			//effectList[effectName] = loadEffect.effectDataTemplate;
			//const loader = new PIXI.loaders.Loader()
			//loader.reset();
			//const resources = PIXI.loader.resources;
			//delete loader.resources[motionID];
			//delete loader.resources[spritesID];
			//let templete
			loader
				.on("progress", loadProgressHandler)
				.load(setup);

			function loadProgressHandler(loader, resource) {
				console.log("loading: " + resource.url);

				console.log("progress: " + loader.progress + "%");

				console.log("loading: " + resource.name);
			}

			function setup() {
				//loadEffect.myData =  

				let motionData = loader.resources[motionID].data
				//console.log("loader", loader, effectName, motionData.metaData.instancer_num)
				let instancerCount = motionData.metaData.instancer_num
				let motionDataKeysCount = Object.keys(motionData).length;
				let motionDataKeys = Object.keys(motionData);
				var effectDataTemplate = {};
				effectList[effectName]["instancerCount"] = motionData.metaData.instancer_num;
				console.log("motionData", effectList[effectName]["instancerCount"], effectName)
				//effectList[effectName][loadEffect.effectDataTemplate.instancerCount] = motionData.metaData.instancer_num;

				//  console.log("All files loaded", loader.progress);
				//  console.log("loaderData",loader.resources[motionID].data); 
				// effectList[effectName]= loader.resources
				//  let motionData = resources[motionID]["data"];
				//function(){}

				loadEffect.loading_Progress = loader.progress;
				effectList[effectName]["motionDataID"] = motionID;
				effectList[effectName]["motionDataURL"] = motionURL;
				effectList[effectName]["motionData"] = motionData;
				effectList[effectName]["instancerCount"] = motionData.metaData.instancer_num;
				effectList[effectName]["instancerID"] = Object.keys(motionData.instancer);
				effectList[effectName]["timeStart"] = motionData.metaData.frame_start;
				effectList[effectName]["timeEnd"] = motionData.metaData.frame_end;
				effectList[effectName]["timeLength"] = motionData.metaData.frame_end - motionData.metaData.frame_start + 1;
				effectList[effectName]["sourceWidth"] = motionData.metaData.source_width;
				effectList[effectName]["sourceHeight"] = motionData.metaData.source_height;
				effectList[effectName]["screenWidth"] = motionData.metaData.canvas_width;
				effectList[effectName]["screenHeight"] = motionData.metaData.canvas_height;
				effectList[effectName]["sequence"] = motionData.metaData.sequence;
				console.log("loader.resources", effectName, motionID, loader.resources, loadEffect.effectDataTemplate.instancerCount)

				let ppIDList = [];
				for (let i = 0; i < motionDataKeysCount; i++) {
					if (motionDataKeys[i].slice(0, 3) == "pId") {
						ppIDList.push(motionDataKeys[i]);
					};
				};
				effectList[effectName]["ppID"] = ppIDList;
				effectList[effectName]["ppCount"] = motionData.metaData.particle_num;
				let spritesData = loader.resources[spritesID].data;
				let spritesDataFrames = spritesData.frames
				var spritesImagesCount = Object.keys(spritesData.frames).length;
				var spritesImagesList = Object.keys(spritesData.frames)
				effectList[effectName]["spritesData"] = spritesData;
				effectList[effectName]["spritesImageId"] = spritesID;
				effectList[effectName]["spriteImage"] = spritesURL.split('.')[0] + ".png";
				effectList[effectName]["frameList"] = Object.keys(spritesData.frames);
				effectList[effectName]["frameLength"] = (Object.keys(spritesData.frames).length);
				effectList[effectName]["spriteImageURL"] = spritesURL;
				effectList[effectName]["spritesImagesList"] = spritesImagesList
				effectList[effectName]["spritesImagesCount"] = spritesImagesCount
				var spritesImagesSize = []
				for (var i in spritesImagesList) {
					//  console.log(spritesDataFrames[spritesImagesList[i]].frame)
					spritesImagesSize.push(spritesDataFrames[spritesImagesList[i]].frame);
				};

				effectList[effectName]["spritesImagesSize"] = spritesImagesSize;
				//console.log("spritesData",spritesData,spritesDataFrames,spritesImagesSize);




				//console.log("loadEffect.effectDataTemplater", loadEffect.effectDataTemplate);


			}
			// console.log("loaderData_finall",loader.resources);
		};

		effectData.readEffectEvent = function () {


			loadEffect.loading_Progress += 20;
			return loadEffect.loading_Progress
			//loadEffect.myData = resources;

		};
		return effectData;
	}

};
var defineSpriteEvent = {

	createNew: function () {
		//console.log("effectList", effectList);
		var event = {};
		event.define = function (effectList, effectName) {
			var callEffectList = effectList[effectName];
			var ppCount = callEffectList.ppCount;
			var ppID = callEffectList.ppID;
			var frameList = callEffectList.frameList;
			var motionData = callEffectList.motionData;
			var timeStart = callEffectList.motionData.metaData.frame_start;
			var timeEnd = callEffectList.motionData.metaData.frame_end;
			var timeLength = timeEnd - timeStart + 1;
			var containerHeight = callEffectList.motionData.metaData.source_height;
			var containerWidth = callEffectList.motionData.metaData.source_width;
			var instancerCount = callEffectList.instancerCount;
			var instancerID = callEffectList.instancerID;
			var sourceImagesW = callEffectList.spritesImagesSize[0].w
			var sourceImagesH = callEffectList.spritesImagesSize[0].h
			//console.log("effectName instancerCount", effectName, instancerCount)

			var animSpritesList = [];
			for (var i in frameList) {

				animSpritesList.push(PIXI.Texture.fromFrame(frameList[i]));
			};
			let templEffectList = [];
			for (var i = 0; i < instancerCount; i++) { //複製pp到instancer中
				var effectContainer = new PIXI.Container();

				effectContainer.name = "container_" + effectName;
				//containerList[effectName] = effectContainer
				app.stage.addChild(effectContainer);
				//console.log("app.stage", effectContainer.name)

				screenWidth = app.renderer.screen.width;
				screenHeight = app.renderer.screen.height;

				templEffectList.push(effectContainer);

				//console.log("tempEffectList", templEffectList)

				/*
					// container 置中

					effectContainer.pivot.x = containerWidth / 2 + effectContainer.width / 2 //freeze pivot and move to center
					effectContainer.pivot.y = containerHeight / 2 + effectContainer.height / 2
					effectContainer.x = screenWidth / 2;
					effectContainer.y = screenHeight / 2;
					*/


				for (var j = 0; j < ppCount; j++) { // <ppCount 為每個PP都建立一個anim event，< sampleCount 則為建立樣本數量
					var anim = new PIXI.extras.AnimatedSprite(animSpritesList);
                    /*
					let ppIDKey = "pId_" + String(j);
					var x = motionData[ppIDKey].translate[1].x; //[0]，在frame =0 時的取樣
					var y = motionData[ppIDKey].translate[1].y;
					var w = motionData[ppIDKey].scale[1].w;
					var h = motionData[ppIDKey].scale[1].h;
					var rotation = motionData[ppIDKey].rotate[1].angle;
					var trans = motionData[ppIDKey].translate[1].trans;
					var vis = motionData[ppIDKey].translate[1].vis;

					var pw = motionData[ppIDKey].pivot_w;
					var ph = motionData[ppIDKey].pivot_h;

					var scale = w / sourceImagesW

					//	anim.pivot.x =w *pw;
					//	anim.pivot.y =h *ph
					//console.log("pivot w h",anim.pivot.x,anim.pivot.y,ppIDKey,pw,ph);
					//anim.animationSpeed = 1; //frameSpeed; 播放速度

					//anim.gotoAndPlay(0) //跳至sprites images中的 相對圖序
                    */
					anim.play();

					effectContainer.addChild(anim);
					//console.log("appStageContainers in class",appStageContainers);


					//anim.pivot.x =40;
					// anim.pivot.x =80;
					// anim.anchor.set(0.5);
					//sprites 歸零            
					//anim.pivot.x = 40
					//anim.pivot.y = 80
					//anim.pivot.x = pw * w;
					//anim.pivot.y = ph * h;
					//anim.x = -pw * w;
					//anim.y = -ph * h;
					// anim.width = w; // 圖寬
					//anim.height = h; // 圖高

					//anim.x = x - w / 2;
					//anim.y = y - h / 2;
					// console.log("anim.pivot", w, h, anim.pivot.x, anim.pivot.y)
					//anim.rotation = -rotation / (180 / Math.PI); //旋轉
                    //anim.blendMode = 0;
				};
			};

			appStageContainers["effects"][effectContainer.name] = templEffectList;
		};
		event.getSpritesData = function (effectName) { //收集spritesData
			//var callEffectList = effectList[effectName];
			// var effectContainerLIst = {};
			// effectContainerLIst[]
			// containerList[effectName] ={}

			containerKeys = Object.keys(app.stage.children);
			var allContainer = app.stage.children;
		//	console.log("allContainer", allContainer);
			var allContainerList = {};
			var allEffectContainer = [];
			var allBGContainer = [];
			var allDrawContainer = [];
			var allUIContainer = [];


			for (var i in allContainer) {
				//console.log("container", allContainer[i]);
				let containerName = allContainer[i].name;
				//console.log(containerName,containerName.split("_"));
				if (containerName.split("_")[1] == "effect") {
					allEffectContainer.push(allContainer[i])
				} else if (containerName.split("_")[1] == "BG") {
					allBGContainer.push(allContainer[i])
				} else if (containerName.split("_")[1] == "draw") {
					allDrawContainer.push(allContainer[i])
				} else if (containerName.split("_")[1] == "UI") {
					allUIContainer.push(allContainer[i])
				};

			};
			var tempEffectList = {};
			tempEffectList[effectName] = allEffectContainer;

			allContainerList["effect"] = tempEffectList;
			allContainerList["BG"] = allBGContainer;
			allContainerList["Grpahics"] = allDrawContainer;
			allContainerList["UI"] = allUIContainer;
			console.log("allContainerList", allContainerList);
			return allContainerList;
			// console.log("spritesData",app.stage.children);

		};
		event.getAllAnimList = function (animEventList) { //調整anim/sprites的各種數據
			//  console.log("dfdsfdd", animEventList)
			var allAnimList = [];
			// console.log("animEventList",animEventList);
			for (i in animEventList) { //選取effect container
				//console.log(i,animEventList[i]);

				// console.log("animEventList.child",animEventList[i]) ; 
				for (j in animEventList[i].children) {
					// console.log(i,j)
					var anim = animEventList[i].children[j];
					//  console.log("anim",anim);
					// anim.y =  -300;
					// console.log("anim",animEventList[i].children[j]);
					var anim = animEventList[i].children[j];
					allAnimList.push(anim)
				};

			};
			return allAnimList;

		};

		event.adjustAnimTransform = function (effectList, effectName, effectContainer, eventTick,adjustList) {
			//eventTick = 0
			// console.log("eventTick",eventTick)
			var callEffectList = effectList[effectName];
			var ppCount = callEffectList.ppCount;
			var ppID = callEffectList.ppID;
			var frameList = callEffectList.frameList;
			var motionData = callEffectList.motionData;
			var timeStart = callEffectList.motionData.metaData.frame_start;
			var timeEnd = callEffectList.motionData.metaData.frame_end;
			var timeLength = timeEnd - timeStart + 1;
			var containerHeight = callEffectList.motionData.metaData.source_height;
			var containerWidth = callEffectList.motionData.metaData.source_width;
			var instancerCount = 1 // callEffectList.instancerCount;
			var instancerID = callEffectList.instancerID;





			for (i in effectContainer) {
				let instancerKey = "instancer_" + String(i);
				// console.log("instancerKey",i,instancerKey);
				let instancerData = motionData.instancer[instancerKey];
				let offset = instancerData.offset; //instancer frame offset

				//console.log(effectContainer[effectName].adjust)
				var adjustTrans = PIXI_globalData[effectName].adjust.spritesTrans;
				var adjustSize = PIXI_globalData[effectName].adjust.spritesSize;
				var adjustRotation = PIXI_globalData[effectName].adjust.spritesRotation;
				var adjustSpeed = PIXI_globalData[effectName].adjust.speed;
				var adjustBlur = PIXI_globalData[effectName].adjust.spritesBlur;
				// console.log("offset",offset)

				if ((offset - eventTick) > 0) {
					var offsetEventTick = 0;
					var trans = 0;

				} else {
					var offsetEventTick = parseInt(eventTick - offset)



				};
				var containerX = instancerData.translate[offsetEventTick].x;
				var containerY = instancerData.translate[offsetEventTick].y;
				var containerTrans = instancerData.translate[offsetEventTick].trans;
				//var containerW = instancerData.scale[offsetEventTick].w;
				// var containerH = instancerData.scale[offsetEventTick].h;
				var containerRotation = instancerData.rotate[offsetEventTick].angle;
				var container_bbw = instancerData.bbox_w;
				var container_bbh = instancerData.bbox_h;
				var container_pw = instancerData.pivot_w;
				var container_ph = instancerData.pivot_h;
				effectContainer[i].pivot.x = containerWidth / 2 + container_pw;
				effectContainer[i].pivot.y = containerHeight / 2 + container_ph;
				// effectContainer[i].pivot.y =0//container_ph + effectContainer[i].height/2;
				// console.log("container wh",effectContainer[i].width,effectContainer[i].height,effectContainer[i].pivot.x,effectContainer[i].pivot.y);

				effectContainer[i].x = containerX + container_pw;
				effectContainer[i].y = containerY + container_ph;
				effectContainer[i].rotation = -containerRotation / (180 / Math.PI);
				effectContainer[i].alpha = containerTrans;
                effectContainer[i].scale.set(adjustList.containerScale)
				// console.log("chgange2")
				// effectContainer[i].x = containerX;
				// effectContainer[i].y = containerY;
				//console.log(effectContainer[i].pivot.x,effectContainer[i].pivot.y)
				// effectContainer[i].width = containerW;
				//effectContainer[i].height = containerH;
				// effectContainer[i].alpha = containerTrans;
				// effectContainer[i].rotation = -containerRotation/57.3;
				//  console.log("1", "containerX",containerX,"containerY", containerY,"container_bbw", container_bbw,"container_bbh", //container_bbh,"container_pw", container_pw,"container_ph", container_ph,"containerRotation",containerRotation)
				for (j in effectContainer[i].children) {
					let ppIDKey = "pId_" + String(j)

					//   console.log(ppIDKey);
					var x = motionData[ppIDKey].translate[offsetEventTick].x;
					var y = motionData[ppIDKey].translate[offsetEventTick].y;
					var w = motionData[ppIDKey].scale[offsetEventTick].w //* adjustSize;
					var h = motionData[ppIDKey].scale[offsetEventTick].h //* adjustSize;
					var rotation = motionData[ppIDKey].rotate[offsetEventTick].angle //+ adjustRotation;
					var trans = motionData[ppIDKey].translate[offsetEventTick].trans //* adjustTrans;
					var vis = motionData[ppIDKey].translate[offsetEventTick].vis;
					var pw = motionData[ppIDKey].pivot_w;
					var ph = motionData[ppIDKey].pivot_h;
					var pp = effectContainer[i].children[j];
                    var imageIndex = motionData[ppIDKey].translate[offsetEventTick].index;
                    
                    if (imageIndex == null){
                        pp.gotoAndPlay(adjustList.frameIndex);
                     
                    }else{ pp.gotoAndPlay(imageIndex);
                        };
                    if (motionData.metaData.sequence == false){pp.animationSpeed = 0}else{
                        pp.animationSpeed = adjustList.frameSpeed; //frameSpeed; 播放速度
                    }
                  //  console.log("trans",offsetEventTick,trans,);
                   // pp.gotoAndPlay(5);
                    //pp.animationSpeed = 0;
					pp.anchor.set(pw, ph); // set to pivot scale  
					pp.x = x + (-0.5 * w + w * pw) // 0.5 * width + width*(pivot width scale)
					pp.y = y + (-0.5 * h + h * ph) // 0.5 * height + height*(pivot height scale)

					pp.width = w*adjustList.spritesSize;
					pp.height = h*adjustList.spritesSize;
					pp.alpha = trans*adjustList.spritesTrans;
					pp.rotation = -rotation / 57.3 -adjustList.spritesRotation/57.3 ;
					
					pp.gotoAndPlay(adjustList.frameIndex)
					pp.blendMode = adjustList.blendMode;
					//console.log("adjustSpeed",adjustSpeed)



				};

			};


		};
		event.runApp = function (effectList, effectName, effectContainer, adjustList) {
			var callEffectList = effectList[effectName];

			var timeStart = callEffectList.motionData.metaData.frame_start;
			var timeEnd = callEffectList.motionData.metaData.frame_end;
			var timeLength = timeEnd - timeStart + 1;
            
			var tick = 0
			app.ticker.add(function () {

				var speed = PIXI_globalData[effectName].adjust.speed
				//var blendMode = blendModeIndex
				tick += Math.floor(speed);
				eventTick = tick % timeLength;
				event.adjustAnimTransform(effectList, effectName, effectContainer, eventTick, adjustList);
				//event.adjustAnimTransform = function(effectList, effectName, effectContainer, eventTick,adjustList) 
			});

		};
		return event;
	}

};
var objectInfo = {
	createNew: function () {
		var selectedInfo = {};

		selectedInfo.getInfo = function (selectObject) {
			console.log("selectObject", selectObject, selectObject.name);

			var objectData = {
				"name": selectObject.name,
				"w": selectObject.width,
				"h": selectObject.height,
				"x": selectObject.x,
				"y": selectObject.y,
				"px": selectObject.pivot.x,
				"py": selectObject.pivot.y,
				"r": selectObject.rotation,
				"alpha": selectObject.alpha,
				"vis": selectObject.visible,
				"children": selectObject.children,
				"transform": selectObject.transform,
				"parent": selectObject.parent
			};
			console.log(objectData);
		};

		return selectedInfo;
	} //注意格式，後面別加上;
};
var drawBox = {

	createNew: function () {
		var draw = {};
		draw.testA = "ggg";
		draw.testB = function () {
			for (var i = 0; i < 10; i++) {
				console.log(i)
			}
		};
		draw.rect = function (x, y, w, h) {
			console.log("testC")
			var graphics = new PIXI.Graphics();

			// set a fill and line style
			graphics.beginFill(0xcc9999, 0.7);
			graphics.lineStyle(1, 0xffd900, 1);
			graphics.drawRect(x, y, w, h);

			graphics.endFill();
			graphics.pivot.x = w / 2;
			graphics.pivot.y = h / 2;
			graphics.x = app.renderer.screen.width / 2;
			graphics.y = app.renderer.screen.height / 2;

			return graphics;
		};
		draw.circle = function (x, y, r) {
			var graphics = new PIXI.Graphics();
			graphics.beginFill(0xaa2255, 1);
			graphics.lineStyle(2, 0x000000, 1);
			graphics.drawCircle(x, y, r);
			graphics.endFill();
			graphics.pivot.x = r;
			graphics.pivot.y = r;
			graphics.x = app.renderer.screen.width / 2;
			graphics.y = app.renderer.screen.height / 2;
			return graphics
		};
		draw.cross = function (x, y, length) {
			var graphics = new PIXI.Graphics();
			graphics.beginFill(0xcccccc, 1);
			graphics.lineStyle(2, 0xcc3333, 1);
			graphics.moveTo(x - length, 0);
			graphics.lineTo(x + length, 0);
			graphics.moveTo(0, y - length);
			graphics.lineTo(0, y + length);
			graphics.pivot.x = x;
			graphics.pivot.y = y;
			graphics.x = app.renderer.screen.width / 2;
			graphics.y = app.renderer.screen.height / 2;
			graphics.endFill();
			return graphics

		};
		draw.drawBB = function (x, y, containerW, containerH) {
			var graphics = new PIXI.Graphics();

			// set a fill and line style
			graphics.beginFill(0x33FFFF, 0.3);
			graphics.lineStyle(2, 0xff0900, 1);
			graphics.drawRect(0, 0, containerW, containerH);

			graphics.endFill();
			graphics.pivot.x = containerW / 2;
			graphics.pivot.y = containerH / 2;
			graphics.x = app.renderer.screen.width / 2;
			graphics.y = app.renderer.screen.height / 2;
			return graphics
		};
		return draw;
	} //注意格式，後面別加上;
};



//sprites and container

var defineAssetLib = {
	appStageContainers: {
		"BG": {},
		"effects": {},
		"UI": {},
		"symbols": {},
		"graphics": {},
		"props": {},
		"ide": {}
	},
	createNew: function () {
		var selectedInfo = {};

		selectedInfo.getInfo = function () {


			console.log("appStageContainers", defineAssetLib.appStageContainers);
			return defineAssetLib.appStageContainers;
		};
		selectedInfo.addEvent = function (containerEvent, containerName, type) {

			defineAssetLib.appStageContainers[type][containerName] = [];
			defineAssetLib.appStageContainers[type][containerName].push(containerEvent);

		};
		return selectedInfo;
	} //注意格式，後面別加上;
};


//UI


var createUI = {
	createNew: function () {
		var uiLayout = {};

		uiLayout.test = function () {
			console.log("start ideUI create");
		};

		uiLayout.createCanvasStage = function (width, height, x, y, color, border) {
			let app = new PIXI.Application(width, height, {
				backgroundColor: color
			});
			app.view.style.border = border;
			app.view.style.position = 'absolute';
			let leftX = String(x) + "px";
			let topY = String(y) + "px";
			app.view.style.left = leftX;
			app.view.style.top = topY;

			document.body.appendChild(app.view);
			return app;



		};

		uiLayout.createInfoBoxStage = function (width, height, x, y, color) {
			// console.log("selectObject", selectObject, selectObject.name);
			let app = new PIXI.Application(width, height, {
				backgroundColor: color
			});
			app.view.style.border = "2px solid brown";
			app.view.style.position = 'absolute';
			let leftX = String(x) + "px";
			let topY = String(y) + "px";
			app.view.style.left = leftX;
			app.view.style.top = topY;




			document.body.appendChild(app.view);



			let graphics = new PIXI.Graphics();

			// set a fill and line style
			graphics.beginFill(0xcc9999, 0.7);
			graphics.lineStyle(1, 0xffd900, 1);
			graphics.drawRect(0, 0, app.renderer.screen.width, 30);
			graphics.endFill();

			//graphics.interactive = true;
			//graphics.buttonMode = true;
			//ideApp.interactive = true;
			//ideApp.buttonMode = true;
			app.stage.addChild(graphics);
			return app;


		};
		uiLayout.createStageInfo = function (appStage, x, y, w, h) {
			let container_stageUI = new PIXI.Container();
			container_stageUI.name = "container_stageUI";
			appStage.addChild(container_stageUI);
			container_stageUI.x = x;
			container_stageUI.y = y;
			container_stageUI.width = w;
			container_stageUI.height = h;
			let graphics = new PIXI.Graphics();
			graphics.beginFill(0xcc9999, 1);
			graphics.lineStyle(2, 0xffd900, 1);
			graphics.drawRect(0, 0, w, 40);
			graphics.endFill();

			graphics.beginFill(0xEEEEEE, 1);
			graphics.lineStyle(2, 0xffd900, 1);
			graphics.drawRect(0, 41, w, 600);
			graphics.endFill();
			container_stageUI.addChild(graphics);
			let ideText = new PIXI.Text('stage info');
			ideText.x = 30;
			ideText.y = 2;
			container_stageUI.addChild(ideText);
			appStageContainers["ide"][container_stageUI.name] = [];
			appStageContainers["ide"][container_stageUI.name].push(container_stageUI);

			return container_stageUI;

		};

		return uiLayout;
	} //注意格式，後面別加上;
};
