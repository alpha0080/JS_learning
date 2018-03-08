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
			effectList[effectName] = effectDataTemplate;
		};

		effectData.readSources = function () {};
		effectData.readSpritesData = function (spritesID, spritesURL, effectName) {
			const loader = new PIXI.loaders.Loader();
			//loader.reset();
			const resources = PIXI.loader.resources;
			delete loader.resources[spritesID];
			let templete
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
					console.log(spritesDataFrames[spritesImagesList[i]].frame)
					spritesImagesSize.push(spritesDataFrames[spritesImagesList[i]].frame);
				};

				loadEffect.effectDataTemplate.spritesImagesSize = spritesImagesSize;
				console.log("spritesData", spritesData, spritesDataFrames, spritesImagesSize);




				console.log("Sprites laoder", loader.resources[spritesID]);

				effectList[effectName] = loadEffect.effectDataTemplate;
			};
		};
		effectData.readMotionData = function (motionID, motionURL, effectName) {

			const loader = new PIXI.loaders.Loader()
			//loader.reset();
			const resources = PIXI.loader.resources;
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
		effectData.readData = function (motionID, motionURL, spritesID, spritesURL, effectName) {

			const loader = new PIXI.loaders.Loader()
			//loader.reset();
			const resources = PIXI.loader.resources;
			delete loader.resources[motionID];
			delete loader.resources[spritesID];
			//let templete
			loader.add(motionID, motionURL)
				.add(spritesID, spritesURL)
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
				//  console.log("All files loaded", loader.progress);
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
					//  console.log(spritesDataFrames[spritesImagesList[i]].frame)
					spritesImagesSize.push(spritesDataFrames[spritesImagesList[i]].frame);
				};

				loadEffect.effectDataTemplate.spritesImagesSize = spritesImagesSize;
				//console.log("spritesData",spritesData,spritesDataFrames,spritesImagesSize);




				//console.log("Sprites laoder", loader.resources[spritesID]);

				effectList[effectName] = loadEffect.effectDataTemplate;
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
			graphics.beginFill(0xFF9922, 0.3);
			graphics.lineStyle(1, 0xff22FF, 1);
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

var defineSpriteEvent = {

	createNew: function () {
		//console.log("effectList", effectList);
		var event = {};
		event.define = function (effectList, effectName, tick) {
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

			var animSpritesList = [];
			for (var i in frameList) {

				animSpritesList.push(PIXI.Texture.fromFrame(frameList[i]));
			};

			for (var i = 0; i < instancerCount; i++) { //複製pp到instancer中
				var effectContainer = new PIXI.Container();
				let containerList = {}
				effectContainer.name = "container_" + effectName;
				containerList[effectName] = effectContainer;
				app.stage.addChild(effectContainer);

				screenWidth = app.renderer.screen.width;
				screenHeight = app.renderer.screen.height;


				// container 置中

				effectContainer.pivot.x = containerWidth / 2 + effectContainer.width / 2 //freeze pivot and move to center
				effectContainer.pivot.y = containerHeight / 2 + effectContainer.height / 2
				effectContainer.x = screenWidth / 2;
				effectContainer.y = screenHeight / 2;
				/*
				let container_Graphic = new PIXI.Container();
				container_Graphic.name = "container_Grpahics";
				let draw = drawBox.createNew();
				let bb = draw.drawBB(0, 0, effectContainer.width, effectContainer.height)
				container_Graphic.addChild(bb);
				// container 置中  ^^^^^^
				app.stage.addChild(container_Graphic)
				*/
				var sideLength = containerWidth;


				for (var j = 0; j < ppCount; j++) { // <ppCount 為每個PP都建立一個anim event，< sampleCount 則為建立樣本數量
					var anim = new PIXI.extras.AnimatedSprite(animSpritesList);
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

					var scale = w / sourceImagesW;

					//	anim.pivot.x =w *pw;
					//	anim.pivot.y =h *ph
					//console.log("pivot w h",anim.pivot.x,anim.pivot.y,ppIDKey,pw,ph);
					//anim.animationSpeed = 1; //frameSpeed; 播放速度

					//anim.gotoAndPlay(0) //跳至sprites images中的 相對圖序

					anim.play();
					console.log("containerWH", effectContainer.width, effectContainer.height);
					/*
					var graphics = new PIXI.Graphics();
					graphics.beginFill(0xFF3300);
					graphics.lineStyle(2, 0xffd900, 1);
					graphics.moveTo(0,0);
					graphics.lineTo(effectContainer.width, 0);
					graphics.lineTo(effectContainer.width, effectContainer.height);
					graphics.lineTo(0, 0);
					graphics.endFill();

					effectContainer.addChild(graphics);
					*/

					effectContainer.addChild(anim);
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
				};
			};
		};
		event.getSpritesData = function (effectName) { //收集spritesData


			containerKeys = Object.keys(app.stage.children);
			var allContainer = app.stage.children;
			const allContainerList = {};
			var allEffectContainer = [];
			var allBGContainer = [];
			var allDrawContainer = [];
			var allUIContainer = [];


			for (var i in allContainer) {
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

		event.adjustAnimTransform = function (effectList, effectName, effectContainer, eventTick) {
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
					var offsetEventTick = eventTick - offset



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
					var w = motionData[ppIDKey].scale[offsetEventTick].w * adjustSize;
					var h = motionData[ppIDKey].scale[offsetEventTick].h * adjustSize;
					var rotation = motionData[ppIDKey].rotate[offsetEventTick].angle + adjustRotation;
					var trans = motionData[ppIDKey].translate[offsetEventTick].trans * adjustTrans;
					var vis = motionData[ppIDKey].translate[offsetEventTick].vis;
					var pw = motionData[ppIDKey].pivot_w;
					var ph = motionData[ppIDKey].pivot_h;
					var pp = effectContainer[i].children[j];


					pp.anchor.set(pw, ph); // set to pivot scale
					pp.x = x + (-0.5 * w + w * pw) // 0.5 * width + width*(pivot width scale)
					pp.y = y + (-0.5 * h + h * ph) // 0.5 * height + height*(pivot height scale)

					pp.width = w;
					pp.height = h;
					pp.alpha = trans;
					pp.rotation = -rotation / 57.3;
					pp.animationSpeed = adjustSpeed; //frameSpeed; 播放速度
					pp.gotoAndPlay(0)

					//console.log("adjustSpeed",adjustSpeed)



				};

			};


		};
		event.getStageData = function () {
			console.log("app.stage", app.stage);
		};
		event.runApp = function (effectList, effectName) {
			event.define(effectList, effectName);
			var callEffectList = effectList[effectName];

			var timeStart = callEffectList.motionData.metaData.frame_start;
			var timeEnd = callEffectList.motionData.metaData.frame_end;
			var timeLength = timeEnd - timeStart + 1;
			var getAllContainerList = event.getSpritesData(effectName);
			//  console.log("getAllContainerList", getAllContainerList["effect"][effectName]);
			var allAnimList = event.getAllAnimList(getAllContainerList["effect"][effectName]);
			console.log("getAllContainerList", getAllContainerList);
			var tick = 0;
			app.ticker.add(function () {

				var speed = PIXI_globalData[effectName].adjust.speed
				tick += Math.floor(speed);
				eventTick = tick % timeLength;
				event.adjustAnimTransform(effectList, effectName, getAllContainerList["effect"][effectName], eventTick)
			});

		};
		return event;
	}

};
