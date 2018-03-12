// PIXI IDE 介面事件定義


function call_PIXI_ideEvents(){
	console.log("read call_PIXI_ideEvents");
	var ideUI = {
			createNew: function(){
                var uiLayout = {};
				
				uiLayout.test = function(){
					console.log("start ideUI create");	
				};
				
				
				
                uiLayout.createStage = function(width,height,x,y,color) {
                   // console.log("selectObject", selectObject, selectObject.name);
				var ideApp = new PIXI.Application(width, height, {
							backgroundColor: color
						});
						ideApp.view.style.border = "2px solid brown";
						ideApp.view.style.position = 'absolute';
						let leftX = String(x)+ "px";
						let topY = String(y)+ "px";
						ideApp.view.style.left = leftX;
						ideApp.view.style.top = topY;
						


			
						document.body.appendChild(ideApp.view);
					
					
					
						let graphics = new PIXI.Graphics();

						// set a fill and line style
						graphics.beginFill(0xcc9999, 0.7);
						graphics.lineStyle(1, 0xffd900, 1);
						graphics.drawRect(0, 0, ideApp.renderer.screen.width, 30);
						graphics.endFill();
						
						graphics.interactive = true;
						graphics.buttonMode = true;
						//ideApp.interactive = true;
						//ideApp.buttonMode = true;
						ideApp.stage.addChild(graphics);
					return ideApp;
					
					
				};
				uiLayout.createStageInfo = function(appStage,x,y,w,h){
					let container_stageUI = new PIXI.Container();
					container_stageUI.name = "container_stageUI";
					appStage.addChild(container_stageUI);
					container_stageUI.x = x;
					container_stageUI.y = y;
					container_stageUI.width = w;
					container_stageUI.height =h;
					let graphics = new PIXI.Graphics();
					graphics.beginFill(0xcc9999, 1);
					graphics.lineStyle(2, 0xffd900, 1);
					graphics.drawRect(0, 0, w , 40);
					graphics.endFill();

					graphics.beginFill(0xEEEEEE, 1);
					graphics.lineStyle(2, 0xffd900, 1);
					graphics.drawRect(0, 41, w , 600);
					graphics.endFill();
					container_stageUI.addChild(graphics);
					let ideText = new PIXI.Text('stage info');
					ideText.x = 30;
					ideText.y = 2;
					container_stageUI.addChild(ideText);
					appStageContainers["ide"][container_stageUI.name]= [];
					appStageContainers["ide"][container_stageUI.name].push(container_stageUI);

					return container_stageUI;
					
				};
				
			return uiLayout;
			} //注意格式，後面別加上;
		};
	return ideUI;
};
