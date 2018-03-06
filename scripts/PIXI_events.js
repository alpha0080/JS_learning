function addParticleEffect() {
	tick += 1;
	eventTick = tick % timeLength;
	for (var c = 0; c < instancerCountMulti; c++) {

	};

};

//app.ticker.add(function(){
//     defineEffectInstancer("effect_A",tick)
//});

function addParticleEffectA() {
	for (var i = 1; i < instancerCount + 1; i++) {

		let instancerKey = "instancer_" + String(i - 1);
		let instancerData = motionData.instancer[instancerKey]
		let offset = instancerData.offset; //instancer frame offset

		//console.log(PIXI_globalData[effectName].adjust)
		var adjustTrans = PIXI_globalData[effectName].adjust.spritesTrans;
		var adjustSize = PIXI_globalData[effectName].adjust.spritesSize;
		var adjustRotation = PIXI_globalData[effectName].adjust.spritesRotation;
		var adjustSpeed = PIXI_globalData[effectName].adjust.speed;
		var adjustBlur = PIXI_globalData[effectName].adjust.spritesBlur;

		if ((offset - eventTick) > 0) {
			let offsetEventTick = 0;
			var trans = 0;
			//  console.log("instancerInfo",offsetEventTick,trans);
		} else {
			let offsetEventTick = eventTick - offset
			var containerX = instancerData.translate[offsetEventTick].x;
			var containerY = instancerData.translate[offsetEventTick].y;
			var containerTrans = instancerData.translate[offsetEventTick].trans;
			var containerW = instancerData.scale[offsetEventTick].w;
			var containerH = instancerData.scale[offsetEventTick].h;
			var containerRotation = instancerData.rotate[offsetEventTick].angle;
			// console.log("instancerInfo",containerX,containerY);

		};
		//instancer transforme
		//var instX = motionData[instancer]
		app.stage.children[i].x = containerX;
		app.stage.children[i].y = containerY;
		//app.stage.children[i].width = containerW;
		//app.stage.children[i].height = containerH;
		//app.stage.children[i].alpha = containerTrans;
		//app.stage.children[i].rotation = -containerRotation/57.3;
		//app.stage.children[i].rotation = 0.1*tick;
		//app.stage.children[i].scale.set(tick*0.01);

		//effectContainer.y += 1
		//console.log("effectContainer_child",containerX,containerY,containerTrans,containerW,containerH,containerRotation);

		for (var j = 0; j < ppCount; j++) {
			let ppIDKey = "pId_" + String(j)

			if ((offset - eventTick) > 0) {
				let offsetEventTick = 0;
				var trans = 0;
				var x = 0;
				var y = 0;
				var w = 0;
				var h = 0;
				var rotation = 0;
				let vis = false
				//console.log("instancerInfo",offsetEventTick,alpha);
			} else {
				let offsetEventTick = eventTick - offset;
				var x = motionData[ppIDKey].translate[offsetEventTick].x;
				var y = motionData[ppIDKey].translate[offsetEventTick].y;
				var w = motionData[ppIDKey].scale[offsetEventTick].w * adjustSize * 20;
				var h = motionData[ppIDKey].scale[offsetEventTick].h * adjustSize * 20;
				var rotation = motionData[ppIDKey].rotate[offsetEventTick].angle + adjustRotation;
				var trans = motionData[ppIDKey].translate[offsetEventTick].trans * adjustTrans;
				var vis = motionData[ppIDKey].translate[offsetEventTick].vis;
				//console.log("instancerInfo",containerX,containerY);

			};



			app.stage.children[i].children[j].x = x
			app.stage.children[i].children[j].y = y
			app.stage.children[i].children[j].width = w;
			app.stage.children[i].children[j].height = h;
			app.stage.children[i].children[j].alpha = trans;
			app.stage.children[i].children[j].rotation = -rotation / 57.3;

			//console.log("pp",x,y,w,h,trans,rotation);
		}

	};
};

function defineEffectInstancer(effectName) {

	var callEffectList = effectList[effectName]
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

	console.log("containerHeight", containerHeight, containerWidth);
	console.log("instancerCount", instancerCount, instancerID);


	//var instancerCount = 100;
	// console.log("effectList_effect_A_all","ppCount",ppCount,"ppID",ppID,"frameList",frameList,"motionData",motionData,"timeLength",timeLength,"instancerCount",instancerCount);

	var animSpritesList = [];
	for (var i in frameList) {

		animSpritesList.push(PIXI.Texture.fromFrame(frameList[i]));
	};

	for (var i = 0; i < instancerCount; i++) { //複製pp到instancer中
		var effectContainer = new PIXI.Container();
		effectContainer.name = "container_effect";

		app.stage.addChild(effectContainer);
		// effectContainer.removeChildren();
		// 設定instancer transformer
		effectContainer.width = containerWidth;
		effectContainer.Height = containerHeight;

		//effectContainer.x = Math.random() * 500;
		//effectContainer.y = Math.random() * 500;
		//effectContainer.rotation = Math.random() * 300;
		//effectContainer.scale.set(0.2);
		//繪製邊界
		var graphics = new PIXI.Graphics();
		graphics.lineStyle(2, 0x0000FF, 1);
		graphics.beginFill(0xFF700B, 0.1);
		var sideLength = containerWidth;
		graphics.drawRect(0, 0, sideLength, sideLength);
		graphics.endFill();
		//effectContainer.addChild(graphics);

		//effectContainer.x = 960;
		//effectContainer.x = 540;
		screenWidth = app.renderer.screen.width;
		screenHeight = app.renderer.screen.height;

		effectContainer.pivot.x = containerWidth / 2 + effectContainer.width / 2 //freeze pivot and move to center
		effectContainer.pivot.y = containerHeight / 2 + effectContainer.height / 2
		effectContainer.x = screenWidth / 2;
		effectContainer.y = screenHeight / 2;
		//effectContainer.scale.set(1);




		for (var j = 0; j < ppCount; j++) { // <ppCount 為每個PP都建立一個anim event，< sampleCount 則為建立樣本數量
			var anim = new PIXI.extras.AnimatedSprite(animSpritesList);

			let frameSpeed = PIXI_globalData[effectName].adjust.frameSpeed;
			let spritesFrameOffset = PIXI_globalData[effectName].adjust.spritesFrameOffset;
			let spritesSizeRandom = PIXI_globalData[effectName].adjust.spritesSizeRandom;
			let spritesRotationRandom = PIXI_globalData[effectName].adjust.spritesRotationRandom;
			// let spritesRotationRandom= PIXI_globalData[effectName].adjust.spritesRotationRandom;


			anim.gotoAndPlay(Math.random() * spritesFrameOffset);
			anim.animationSpeed = frameSpeed;
			anim.scale.set(Math.random() * spritesSizeRandom);


			anim.play();

			effectContainer.addChild(anim);

			//設定PP transformer
			anim.x = Math.random() * sideLength;
			anim.y = Math.random() * sideLength;
			// anim.scale.set(0.1);
		};
	};

};
