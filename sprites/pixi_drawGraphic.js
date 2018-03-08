//繪製背景 grid 圖像
function drawGrid(container, screenWidth, screenHeight) {

            container.removeChildren();

            console.log("drawContainer children", container);

            container.removeChild(this.children);
            var graphics = new PIXI.Graphics();
            var screenWidth = screenWidth;
            var screenHeight = screenHeight;
            var style = new PIXI.TextStyle({

                fontFamily: 'Arial',
                fontSize: 20,
                fontStyle: 'italic',
                fontWeight: 'bold',
                fill: ['#ffffff', '#00ff99'], // gradient
                stroke: '#4a1850',
                strokeThickness: 5,
                dropShadow: true,
                dropShadowColor: '#000000',
                dropShadowBlur: 2,
                dropShadowAngle: Math.PI / 6,
                dropShadowDistance: 2,
                wordWrap: true,
                wordWrapWidth: 440
            });
            var styleB = new PIXI.TextStyle({

                fontFamily: 'Arial',
                fontSize: 10,
                fill: ['#ffffff', '#00ff99'], // gradient
                stroke: '#4a1850',
                strokeThickness: 1,
                dropShadow: true,
                dropShadowColor: '#000000',
                dropShadowBlur: 1,
                dropShadowAngle: Math.PI / 6,
                dropShadowDistance: 1,
                wordWrap: true,
                wordWrapWidth: 440
            });


            graphics.beginFill(0xFF3300);
            graphics.lineStyle(2, 0xffd900, 1);

           // var gridStepW = screenWidth / 24
            for (var i = 0; i < 24; i ++) { //繪製水平線
              //  console.log("draw Grid")
                graphics.moveTo(0, i*(screenHeight/24));
                graphics.lineTo(screenWidth, i*(screenHeight/24));
                var cordXText = new PIXI.Text(i*parseInt(screenWidth/24), styleB);
                cordXText.x =  i*(screenWidth/24);
                cordXText.y = 10;
                container.addChild(cordXText);
            };

            //var gridStepH = screenHeight / 24

            for (var i = 0; i < 24; i ++) {
                graphics.moveTo(i*(screenWidth/24), 0);
                graphics.lineTo(i*(screenWidth/24), screenHeight);
                var cordXText = new PIXI.Text(i*parseInt(screenHeight/24), styleB);
                cordXText.x = 10;
                cordXText.y =  i*(screenHeight/24);
                container.addChild(cordXText);
            };
            graphics.endFill();

            graphics.lineStyle(0);
            graphics.beginFill(0xFF9999, 1);
            graphics.drawCircle(screenWidth / 2, screenHeight / 2, 10);
            graphics.endFill();



            container.addChild(graphics);



            var originText = new PIXI.Text("(0,0)", style);
            originText.x = 0;
            originText.y = 0;

            var centerText = new PIXI.Text("(" + screenWidth / 2 + "," + screenHeight / 2 + ")", style);
            centerText.x = screenWidth / 2;
            centerText.y = screenHeight / 2;

            var rightBottom = new PIXI.Text("(" + screenWidth + "," + screenHeight + ")", style);
            rightBottom.x = screenWidth - 100;
            rightBottom.y = screenHeight - 30;

            container.addChild(centerText);
            container.addChild(originText);
            container.addChild(rightBottom);
        };



//測試圖形 大量的四邊形
function drawTestGraphicA(screenWidth, screenHeight,randomRange, rectWidth, rectHeight, rectFilterR, rectCount) {
	//console.log("drawGraphicA start")
	var graphicsA = new PIXI.Graphics();
	//console.log("drawGraphicA start",centerX,centerY);
	graphicsA.beginFill(0xFF3300);
	graphicsA.lineStyle(1, 0xFF00FF, 0.01);

	graphicsA.beginFill(0xFF00BB, 1);
	for (var i = 0; i < rectCount; i++) {
		
		var square = graphicsA.drawRoundedRect(screenWidth+Math.random()*randomRange, screenHeight+Math.random()*randomRange, rectWidth, rectHeight, rectFilterR);
	};


	graphicsA.endFill();
	//console.log("drawGraphicA end")

	return graphicsA
};


function setBG() {
    
    var container_BG = new PIXI.Container();

    container_BG.name = "container_BG";
    app.stage.addChild(container_BG);

   // console.log("width", PIXI_globalData.BGA.width, PIXI_globalData.BGA.height);
   // console.log("PIXI_globalData", PIXI_globalData);

   // deleteAllChildrenInStage("event") //刪除所有名稱為 event的 container
    //deleteAllChildrenInStage("effect")
    //deleteAllChildrenInStage("container_BG") //刪除所有名稱為 event的 container
    app.renderer.clear();
    //app.renderer = null;

    app.start();
    let BGW = PIXI_globalData.BGA.width;
    let BGH = PIXI_globalData.BGA.height;
    let BGColor = "0x" + document.getElementById("colorBGA").value.split('#')[1];
    let BGAURL = document.getElementById("showBGA").value;
    let BGA_Scale = PIXI_globalData.BGA.screenScale;
    app.renderer.resize(BGW, BGH);

    app.renderer.backgroundColor = BGColor;
    //redrawRender(BG_stage);

    let background = PIXI.loader.resources.BGA_image;
    background = new Sprite(TextureCache[BGAURL]);
    background.scale.set(BGA_Scale)


    drawGrid(container_BG, BGW, BGH); //由 pixi_drawGraphic.js繪製 背景grid


};