//PIXI_loaderData.js 讀取素材檔案


function PIXI_loader(id,url){
	
	var loader = PIXI.loader;
	loader.add(id,url)
			.load(setup);
	
	function setup(){
		console.log(loader)
	};
	return loader
}


/*
　　var Cat = {

　　　　sound : "喵喵喵",

　　　　createNew: function(){

　　　　　　var cat = {};

　　　　　　cat.makeSound = function(){ alert(Cat.sound); };

　　　　　　cat.changeSound = function(x){ Cat.sound = x; };

　　　　　　return cat;

　　　　}

　　};
*/
var testaa= function(){
	console.log("aassddff");
};


var name = "Jhon";
exports.getName = function() {
  return name;
}

var exports.loadEffect ={

	createNew:function(motionJson,spritesJson){
		hello: "hello world";
		var effectList ={};
		effectList.motionData = motionJson +"loading";
		effectList.spritesJson = spritesJson +"loading";
		return effectList;
	};
};